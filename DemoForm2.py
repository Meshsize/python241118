#DemoForm2.py
#DomoForm2.ui 화면 + DemoForm2.py 로직

import sys  
from PyQt5.QtWidgets import *
from PyQt5 import uic

from bs4 import BeautifulSoup
import urllib.request as req
import re

from_class = uic.loadUiType("DemoForm2.ui")[0]

#윈도우 클래스 정의 (QMainWindow)
class DemoForm(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    #슬롯 메소드 추가
    def firstClick(self):
        f = open('clien.txt', 'wt', encoding='utf-8')
        for i in range(0, 10):
            url = 'https://www.clien.net/service/board/sold?&od=T31&category=0&po=' + str(i)
            print('페이지 : ', str(i))
            
            # req 객체를 사용하여 요청을 보냅니다.
            # request = req.Request(url, headers=hdr)
            response = req.urlopen(url)  # 수정된 부분
            page = response.read().decode('utf-8', 'ignore')  # 중복된 decode 제거
            # 검색이 용이한 객체 생성
            soup = BeautifulSoup(page, "html.parser")

            list = soup.find_all('a', attrs={'class':'list_subject'})

            for item in list:
                try:
                    title = item.find("span", attrs={'class':'subject_fixed'})
                    title = title.text.strip()
                    if re.search('아이폰', title):
                        print(title)
                        f.write(title + '\n')
                except AttributeError:  # 명확한 예외 처리
                    pass
            print(' ')
            print(' ')
        f.close()

        self.label.setText("클리앙 중고장터 크롤링 완료!!!")
    def secondClick(self):
        self.label.setText("두번째 버튼 클릭~~")
    def thirdClick(self):
        self.label.setText("세번째 버튼 클릭~~~")   


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()