#DemoRandom.py
import random as r

print(r.random())
print(r.random())

print(r.sample(range(20), 10))
print(r.sample(range(20), 10))

#로또번호 생성
print(r.sample(range(1,46), 5))
print(r.sample(range(1,46), 5))


#파일명, 파일정보
from os.path import *
print(abspath('python.exe'))
print(basename('c:\\work\\python.exe')) ##\ 뒤에 t, n이 오면 특수문자로 인식 하므로 \\로 사용한다.

filename = r'c:\python310\text.exe' #r(raw string notation)
filename = f'c:\python310\text.exe'

if exists(filename):
    print('파일크기:{0}'.format(getsize(filename)))
else:
    print('파일없음')

#운영체제 정보
import os
print('OS Name : ', os.name)
#print('환경변수 : ', os.environ)

#외부 프로세스 실행
#os.system('calc.exe')

import glob
result = glob('c:\\Data\\')

print(result)