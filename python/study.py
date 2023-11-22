b= 'jakarta'
a= 'a'
fp= 4
x=input('warna awan....')

status = a in b
print (str(status))
diatadict={
    'udin':'jump',
    'samsu': x
}

bb= b.isalpha()
print( bb)
if b or a== "jakarta":
    print('benar')
count= 1
for i in range(fp):
    print('*')
while True:
    print('*'*count)
    count += 1
    if count > 10:
        break 

j0= input('dukun viral...')
if j0 =='samsu':
    print(diatadict.get('samsu'))
else:
    print ('-')



ken={
    'ho':'hover',
    'no':'noode'
}
for key in ken.keys():
    print (ken.get(key))


value= ken.keys()
print(value)
for values in ken.values():
    print(values)

items = ken.items()
print(items)
for item in ken.items():
    print(item)
for key,values in ken.items():
    print(key,values)

j=8
p=2
c=j & p 
if c == 1:
    while True:
        x=int(input('angka'))
        if x == 5:
            break
else:
    for n in ken.items():
        print(n)





print(diatadict.get('udin'))

