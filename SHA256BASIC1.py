from hashlib import sha256
import codecs
header = codecs.decode("04000000b9e2784a84e5d2468cee60ad14e08d0fee5dda49a37148040000000000000000e9dd2b13157508891880ef68729a1e5ecdde58062ebfa214a89f0141e5a4717faefd2b577627061880564bec",'hex')
ho=codecs.encode(sha256(sha256(header).digest()).digest()[::-1],'hex')
print (ho)
print(codecs.decode(ho,'hex')<codecs.decode('0000000000000000062776000000000000000000000000000000000000000000','hex'))

#output
'''
>>> 
========================================= RESTART: C:/Users/durga/AppData/Local/Programs/Python/Python37/my programs/hash1.py =========================================
b'0000000000000000040199a6c7b922f711ee7e98cd58863b8b981b02d2b83e13'
True
>>>
'''

name='durga'
encodename=sha256(name.encode())
print('sha256 code is:',encodename.hexdigest())
print(len(encodename.hexdigest()))
#output
'''
sha256 code is: 6df5086153853ea46fb866bff10c9adad7b242ddd5e3983d5c0dbc4a9b5d701f
64
>>>
'''
