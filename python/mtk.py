print ('\nKONVERSI TEMPERATUREn')

#celcius = float (input('masukkan suhu dlm celcius: '))
fahrenheit_input= float (input('masukkan suhu untuk diubah menjadi kelvin: '))
kelvin_input= float(input('masukkan suhu untuk diubah menjadi fahreinheit: '))
#print ('suhu = ', celcius,'celcius')
#reamur = (4/5) * celcius
#print("suhu dlm reamur", reamur, "reamur")
#fahrenheit=(((9/5)*celcius)+32)
#print('suhu dalam fahrenheit',fahrenheit,'fahrenheit')
#kelvin = celcius+273
#print('suhu dalam kelvin',kelvin,'kelvin')

fahrenheit_kelvin= ((5/9)*(fahrenheit_input-32))+273
print (fahrenheit_kelvin,"kelvin")
kelvin_fahreinheit= ((kelvin_input-273)*(9/5))+32
print (kelvin_fahreinheit,"fahrenheit")