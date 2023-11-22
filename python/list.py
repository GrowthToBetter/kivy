nama =["bara", "jean", "richnerd"]
print (len (nama))
a=nama.copy()
print(a)
nama[2]='sugeng'
print (nama)
hh=['ga guna']
test= [nama,hh]
from copy import deepcopy
gabung= deepcopy(test)
nama[0]='rich'
print (test)
print (gabung)
k= input()
if k != nama[0]:
    print('salah' )
else:
    print('benar')
