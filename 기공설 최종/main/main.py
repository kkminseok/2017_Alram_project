#-*- encoding:utf8 -*-
import requests
import lxml
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup
class lecture:
    def __init__(self,_type,_name,_prop,_day,_stime,_etime,_location):
        self.type =_type.strip() #이수구분
        self.name =_name.strip() #교과목명
        self.propessor = _prop.strip() #교수이름
        self.day = _day.strip() #요일
        self.startTime = _stime.strip()#시작강의시간
        self.endTime = _etime.strip()#끝나는시간
        self.location = _location.strip() #장소
    def printinfo(self):
        print "이수구분::",self.type
        print "교과목명::", self.name
        print "담당교수::", self.propessor
        print "강의요일::", self.day
        print "강의시작::", self.startTime
        print "강의끝  ::", self.endTime
        print "강의실  ::", self.location
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Content-Length':'44',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'ORA_WX_SESSION="163.180.96.225:80-0";JSESSIONID=a3b460e2ce548a4f424e280486696c6c8f6aca349d3.nQjPpkrvpArtmwTFo7iImkaIoR8UaNaKahD3lN4QaMSLc30IchmIax8Q-x4TakeSmN4Iah0Kn3zAmhqSmA4I-huKa30xoQvPolaInQjPpkrvpArtmwTFo7iImkaIoR8xah8LaN4NchyRagb48QHCrkzN8QfznA5Pp7ftolbGmkTy;',
    'Host':'khuis.khu.ac.kr',
    'Origin':'https://khuis.khu.ac.kr',
    'Referer':'https://khuis.khu.ac.kr/java/servlet/controllerHssu',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

query ={
'action':'655',
'auto':'on',
'lectYear':'2017',
'lectTerm':'10'
}
login_query = {
    'user_id': '2012104091',
    'password': 'g2820480G!',
    'RequestData':''
}
controll_query={
'action':'19',
'menuId':'hsip',
'parentWindowId':'hsip1000',
'ifurl':'controllerCosy^action=17|WID=hsip1004|Pkg=JSP|URL=JSP./jsp/hssu/infospace/SugangSearchPrintList.jsp[(QUES)]auto=off',
'windowId2':'hsip1100'
}
controll_headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4',
    'Connection':'keep-alive',
    'Host':'khuis.khu.ac.kr',
    'Referer':'https://khuis.khu.ac.kr/java/servlet/controllerCosy?action=20&parentWindowId=hsip1000',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
}
if __name__ == "__main__":
    loginurl = "https://khuis.khu.ac.kr/java/servlet/khu.cosy.login.loginCheckAction"
    loginres = requests.post(loginurl, data=login_query)
    cookies_ =  loginres.cookies

    url = "http://khuis.khu.ac.kr/java/servlet/controllerHssu"
    res = requests.post(url,data =query,headers=headers)
    soup = BeautifulSoup(res.text,"lxml")
    # print table[2] # 수강신청
    # print table[3] # 재수강
    # 11 전공기초, 04 전공필수, 05 전공선택, 06 교직과, 14 중핵교과, 15 배분이수교과, 16 기초교과, 17 자유이수,
    # 20 교직전선, 08 자유선택교과[배움학점제,군사학,취업스쿨,학점교류 과목등]
    lecturelist = []
    prevType = "" #이전 타입 (연강인 애들잡기위해서 만든변수)
    prevName = "" #이전 교과목명
    table = soup.find_all("table",class_="adTB")
    trlist = table[2].find_all('tr')
    for data in trlist[2:-1]:
        type = data.find('td').get_text()
        tdlist = data.find_all('td')
        name = tdlist[2].get_text() #강의제목
        propessor = tdlist[6].get_text() #교수명
        dateinfo = tdlist[7].get_text()  # 강의시간& 강의실
        #info쪼개기
        day, datetime,location =  dateinfo.split('||')
        stime,etime = datetime.split('-')

        if type == ' ': #연강인경우
            #print prevType, prevName, propessor, dateinfo
            lecturelist.append(lecture(prevType,prevName,propessor,day,stime,etime,location))
        else:#연강이 아닌경우
            prevType = type
            prevName = name
            #print type, name, propessor, dateinfo
            lecturelist.append(lecture(type, name, propessor, day, stime, etime, location))
    for lecdata in lecturelist:
        print '_' * 20
        lecdata.printinfo()
        print '_' * 20


