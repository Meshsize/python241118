#DemoFile.py

#쓰기
f = open('demo.txt', 'wt', encoding='utf-8')
f.write('첫번째\n두번째\n세번째\n')
f.close()

#읽기
f = open('demo.txt', 'rt', encoding='utf-8')
result = f.read()
print(result)
f.close()

#문자열 처리
strA = 'python is vary powerful'
strB = '파이썬은 강력해'
print(len(strA))
print(len(strB))
print(strA.capitalize())
print('MBC250'.isalnum())
print('2580'.isdecimal())

data = '<<<  spam and ham >>>'
result = data.strip('<> ')
print(data)
print(result)

print('---리스트로 변환 ---')
result2 = result.replace('spam', 'sapm egg')
result2 = result.replace('and ', ' ')
print(result)
lst = result2.split()
print(lst)
print(" -> ".join(lst))


#정규표현식
import re
result = re.search('[0-9]=*th', '35th')
print(result)
print(result.group())

result = re.search('apple', 'this is an apple')
print(result.group())

result = re.search('\d{4}', '올해는 2024년 입니다. 5464')
print(result.group())

result = re.search('\d{5}', '우리 집 우편번호는 42250')
print(result.group())