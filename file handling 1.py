Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
>>> f=open('football.txt','w+')
>>> f=open('football.txt','r')
>>> f
<_io.TextIOWrapper name='football.txt' mode='r' encoding='cp1252'>
>>> 
>>> f.read()
'Ronaldo\nmessi\nNeymar\nmarcelo\nramos\nhaaland\nmbappe\nsalah'
>>> 
>>> f.read()
''
>>> f.close()
>>> f=open('football.txt')
>>> f
<_io.TextIOWrapper name='football.txt' mode='r' encoding='cp1252'>
>>> f.read()
'Ronaldo\nmessi\nNeymar\nmarcelo\nramos\nhaaland\nmbappe\nsalah'
>>> f.close()
>>> f=open('football.txt')
>>> f
<_io.TextIOWrapper name='football.txt' mode='r' encoding='cp1252'>
>>> f.read(5)
'Ronal'
>>> f.read(5)
'do\nme'
>>> f.read(5)
'ssi\nN'


f.read(5)
'eymar'
f.read(5)
'\nmarc'
f.read(5)
'elo\nr'

f.read(5)
'amos\n'

f.read(10)
'haaland\nmb'
f.read(10)
'appe\nsalah'
f.read(10)
''
f.close()
f
<_io.TextIOWrapper name='football.txt' mode='r' encoding='cp1252'>

f=open('football.txt')
f.readline()
'Ronaldo\n'
f.readline()
'messi\n'
f.readline()
'Neymar\n'
f.readline()
'marcelo\n'
f.readline()
'ramos\n'
f.readline()
'haaland\n'
f.readline()
'mbappe\n'
f.readline()
'salah'
f.readline()
''
f.close()

f=open('football.txt')
f.readlines()
['Ronaldo\n', 'messi\n', 'Neymar\n', 'marcelo\n', 'ramos\n', 'haaland\n', 'mbappe\n', 'salah']
''
''
for i in f:
    print(i)

    

f.close()
f
<_io.TextIOWrapper name='football.txt' mode='r' encoding='cp1252'>
f=open('football.txt')
for i in f.readlines():
    print()

    









for i in f.readlines():
    print()

    

f.close()
f=open('football.txt')
for i in f.readlines():
    print(i)

    
Ronaldo

messi

Neymar

marcelo

ramos

haaland

mbappe

salah
f.close()

f=open('football.txt')
for i in f.readline():
    print(i)

    
R
o
n
a
l
d
o


f.close()

f=open('football.txt','w+')
f.write('ronaldo\nmessi\nneymar\nmarcelo\nramos\nsuraz')
40
f.close()

with open('football.txt','a') as f:
    f.writelines('\nbeckham\nkaka')

    
f=open('football.txt')
f.tell()
0
f.read(5)
'ronal'
f.tell()
5
f.seek(10)
10
f.tell()
10
f.read()
'essi\nneymar\nmarcelo\nramos\nsuraz\nbeckham\nkaka'
f.read()
''
f.seek(0)
0
f.read()
'ronaldo\nmessi\nneymar\nmarcelo\nramos\nsuraz\nbeckham\nkaka'

