from bs4 import BeautifulSoup
import urllib.request as req

import re

hdr = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1'}

f = open('clien.txt', 'wt', encoding='utf-8')
for i in range(0, 10):
    url = 'https://www.clien.net/service/board/sold?&od=T31&category=0&po=' + str(i)
    print('페이지 : ', str(i))
    
    req = re.Request(url, headers=hdr)
    #주소를 입력
    response = req.urlopen(url)
    page = response.read().decode('utf-8')
    page = page.decode('utf-8', 'ignore')
    #검색이 용이한 객체 생성
    soup = BeautifulSoup(page, "html.parser")

    list = soup.find_all('a', attrs={'class':'list_subject'})

    for item in list:
        try:
            title = item.find("span", attrs={'data-role':'list-title-text'})
            title = title.text.strip()
            if re.search('아이폰', title):
                print(title)
                f.write(title + '\n')
        except:
            # print(item)
            pass
    print(' ')
    print(' ')
f.close()

# <td class="subject"><a href="/board/view.php?table=bestofbest&amp;no=477648&amp;s_no=477648&amp;page=1" target="_top">약국 타짜</a><span class="list_memo_count_span"> [20]</span>  <span style="margin-left:4px;"><img src="http://www.todayhumor.co.kr/board/images/list_icon_photo.gif" style="vertical-align:middle; margin-bottom:1px;"> </span> </td>