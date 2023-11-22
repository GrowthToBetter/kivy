from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from plyer import gps
from jnius import autoclass
import requests

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [50, 100]
        self.spacing = 20

        self.permission_label = Label(text='Izin lokasi belum diberikan')
        self.add_widget(self.permission_label)

        self.gps_location = None

    def on_permission_granted(self):
        try:
            gps.configure(on_location=self.on_gps_location)
            gps.start(minTime=1000, minDistance=0)
        except Exception as e:
            self.permission_label.text = f'Gagal mengaktifkan GPS: {str(e)}'

    def on_permission_denied(self, error):
        self.permission_label.text = f'Izin lokasi ditolak: {error}'

    def on_gps_location(self, **kwargs):
        try:
            latitude = kwargs['lat']
            longitude = kwargs['lon']
            self.gps_location = (latitude, longitude)
            self.permission_label.text = f'Lokasi: {latitude}, {longitude}'
            self.send_location_to_server(latitude, longitude)
        except Exception as e:
            self.permission_label.text = f'Gagal mendapatkan lokasi: {str(e)}'

    def send_location_to_server(self, latitude, longitude):
        try:
            url = 'http://localhost:5000/location'
            payload = {'latitude': latitude, 'longitude': longitude}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print('Location sent successfully')
            else:
                print('Failed to send location')
        except Exception as e:
            print(f'Failed to send location: {str(e)}')

class MyApp(App):
    def build(self):
        layout = MainLayout()
        self.request_location_permission(layout)
        return layout

    def request_location_permission(self, layout):
    
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        ActivityCompat = autoclass('android.support.v4.app.ActivityCompat')
        Permission = autoclass('android.Manifest$permission')

        def callback(requestCode, permissions, grantResults):
            if grantResults[0] == 0:  # 0 means PERMISSION_GRANTED
                self.root.on_permission_granted()
            else:
                self.root.on_permission_denied('Izin lokasi tidak diberikan')
        activity = PythonActivity.mActivity
        permission = Permission.ACCESS_FINE_LOCATION
        ActivityCompat.requestPermissions(activity, [permission], 1, callback)

    def on_pause(self):
        return True

if __name__ == '__main__':
    MyApp().run()
