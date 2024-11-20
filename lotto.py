import requests
from bs4 import BeautifulSoup

# 로또 1등 당첨 번호를 가져오는 함수
def fetch_lotto_numbers():
    url = 'https://www.nlotto.co.kr/gameResult.do?method=byWin'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 로또 번호를 저장할 리스트
    lotto_numbers = []

    # 로또 번호 추출
    for row in soup.select('.tbl_data tbody tr'):
        numbers = row.select('td:nth-child(n+3)')  # 3번째 열부터 번호 추출
        if numbers:
            lotto_numbers.append([num.text.strip() for num in numbers])

    return lotto_numbers

# 로또 번호를 파일에 저장하는 함수
def save_lotto_numbers_to_file(lotto_numbers):
    with open('lotto.txt', 'w') as file:
        for numbers in lotto_numbers:
            file.write(', '.join(numbers) + '\n')

# 메인 실행 부분
if __name__ == '__main__':
    lotto_numbers = fetch_lotto_numbers()
    save_lotto_numbers_to_file(lotto_numbers)