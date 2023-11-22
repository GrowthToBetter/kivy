from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///locations.db'

db = SQLAlchemy(app)

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def to_dict(self):
        return {'id': self.id, 'latitude': self.latitude, 'longitude': self.longitude}

@app.route('/location', methods=['POST'])
def save_location():
    try:
        data = request.get_json()
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        if latitude is not None and longitude is not None:
            location = Location(latitude=latitude, longitude=longitude)
            db.session.add(location)
            db.session.commit()
            return jsonify({'message': 'Location saved successfully'}), 200
        else:
            return jsonify({'message': 'Invalid location data'}), 400
    except Exception as e:
        return jsonify({'message': f'Failed to save location: {str(e)}'}), 500

@app.route('/locations', methods=['GET'])
def get_locations():
    try:
        locations = Location.query.all()
        locations_dict = [location.to_dict() for location in locations]
        return jsonify(locations_dict), 200
    except Exception as e:
        return jsonify({'message': f'Failed to get locations: {str(e)}'}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
