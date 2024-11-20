#web1.py
#웹크롤링 예제

from bs4 import BeautifulSoup

#페이지 로딩
page = open('Chap09_test.html', 'rt', encoding='utf-8').read()

soup = BeautifulSoup(page, 'html.parser')

#전체 문서를 출력
# print(soup.prettify())

# <p> 태그 전부 출력
print(soup.find_all('p'))

# links = soup.find_all('a')
# for a in links:
#     print(a.attrs['href'])

# <p> 태그 중에서 class 속성이 inner-text인 것만 출력
# print(soup.find_all('p', class_='inner-text'))

#태그 내부에 존재하는 텍스트만 출력
#<p> 내부 문자열 </p>
for tag in soup.find_all('p'):
    title = tag.text.strip()
    title = title.replace('\n', '')
    print(title)


