import requests
from bs4 import BeautifulSoup

# 네이버 검색 결과 페이지 URL
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4"

# 요청 헤더 설정 (필요할 경우)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

# 페이지 요청
response = requests.get(url, headers=headers)

# BeautifulSoup을 이용한 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 신문기사 제목을 크롤링
# 기사 제목은 네이버 검색 결과에서 다양한 형태로 나타날 수 있으므로, 적합한 CSS 선택자를 찾아야 합니다.
# 예시: 기사 제목이 특정 클래스명으로 감싸져 있을 경우
titles = soup.select('.news_tit')  # '.news_tit'는 일반적으로 뉴스 제목의 클래스명입니다.

# 제목 출력
for title in titles:
    print(title.get_text())  # 제목 텍스트 출력
    print(title['href'])  # 제목의 링크 출력
