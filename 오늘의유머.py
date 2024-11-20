from bs4 import BeautifulSoup
import urllib.request
import re

hdr = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1'}

f = open('todayhumor.txt', 'wt', encoding='utf-8')
for i in range(1, 11):
    #오늘의 유머 베스트게시판
    data = 'https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(i)
    print('페이지 : ', str(i))
    
    req = urllib.request.Request(data, headers=hdr)
    data = urllib.request.urlopen(req).read()
    page = data.decode('utf-8', 'ignore')
    soup = BeautifulSoup(page, "html.parser")
    list = soup.find_all('td', attrs={'class':'subject'})

    for item in list:
        try:
            title = item.find("a")
            title = title.text.strip()
            if (re.search('명태균', title)):
                print(title)
                f.write('페이지 : ' + str(i) + '\n')
                f.write(title + '\n')
        except:
            # print(item)
            pass
    # print(' ')
    # print(' ')
f.close()

# <td class="subject"><a href="/board/view.php?table=bestofbest&amp;no=477648&amp;s_no=477648&amp;page=1" target="_top">약국 타짜</a><span class="list_memo_count_span"> [20]</span>  <span style="margin-left:4px;"><img src="http://www.todayhumor.co.kr/board/images/list_icon_photo.gif" style="vertical-align:middle; margin-bottom:1px;"> </span> </td>