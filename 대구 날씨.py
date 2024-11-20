# 대구 고산2동 날씨 정보 추출
import requests
from bs4 import BeautifulSoup
# 기상청 날씨 API URL (예시)
url = 'https://www.weather.go.kr/weather/observation/currentweather.jsp'
params = {'stn': '108', 'page': '1'}  # 대구 고산2동의 스테이션 코드와 페이지 번호  

response = requests.get(url, params=params)
soup_weather = BeautifulSoup(response.text, 'html.parser')

#1981년 이후의 날씨 추출
weather_info = soup_weather.find_all('td', class_='txt')
for info in weather_info:
    print(info.text.strip())    
