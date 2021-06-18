#-*- encoding:utf8 -*-
import pymysql
import sys
import requests
from bs4 import BeautifulSoup
#___DB부분 변수
ip = 'localhost'
id = 'root'
pw = 'autoset'
name = 'kmsprj'
conn = pymysql.connect(ip, id, pw, name, charset="utf8")
curs = conn.cursor()
sql = """insert into user(id,pw) values (%s, %s)"""
lecturesql = """insert into lecture(id,type,name,propessor,day,starttime,endtime,location,flag) values (%s, %s,%s,%s,%s,%s,%s,%s,%s)"""
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
        print( "이수구분::",self.type)
        print ("교과목명::", self.name)
        print ("담당교수::", self.propessor)
        print ("강의요일::", self.day)
        print ("강의시작::", self.startTime)
        print ("강의끝  ::", self.endTime)
        print ("강의실  ::", self.location)
#a3b460e1ce6a0e1f69ba4eb48178d339e1cd5f789f2.nQjPpkrvpArtmgTFo7iImkaIoR8UaNaKaxD3lN4QaMSLc30IchmIax8P-x4TakeSmN4Iah0Kn3zvmQ8Lbx4I-huKa30xoQvPolaInQjPpkrvpArtmgTFo7iImkaIoR8xahaSbN8QbNaRa2b48QHCrkzN8QfznA5Pp7ftolbGmkTy;
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Content-Length':'44',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'ORA_WX_SESSION="163.180.96.225:80-0";JSESSIONID=a3b460e1ce6a0e1f69ba4eb48178d339e1cd5f789f2.nQjPpkrvpArtmgTFo7iImkaIoR8UaNaKaxD3lN4QaMSLc30IchmIax8P-x4TakeSmN4Iah0Kn3zvmQ8Lbx4I-huKa30xoQvPolaInQjPpkrvpArtmgTFo7iImkaIoR8xahaSbN8QbNaRa2b48QHCrkzN8QfznA5Pp7ftolbGmkTy;',
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
    'user_id': '2015110473',
    'password': 'test',
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
    table = soup.find_all("table",class_="adTB")        #soup 라이브러리를 사용하여, table과 class이름이 adTB인 태그를 찾아 리스트로 반환한다.

    trlist = table[2].find_all('tr')                    #trlist는 table[2]에서 tr을 가진 태그를 찾아 리스트로 반환

    for data in trlist[2:-1]:                          #data에 순차적으로 trlist를 넣는다
        type = data.find('td').get_text()              #type은 data에 있는 td태그의 텍스트를 넣는다.
        tdlist = data.find_all('td')                   #tdlist는 data에있는 td태그의 내용을 넣는다.
        name = tdlist[2].get_text() #강의제목           #name은 강의제목을 넣는다
        propessor = tdlist[6].get_text() #교수명       #propessor는  교수명을 넣는다
        dateinfo = tdlist[7].get_text()  # 강의시간& 강의실   #datainfo는 강의시간,강의실을 넣는다
        #info쪼개기
        day, datetime,location =  dateinfo.split('||')  #강의시간 ,강의실을 '||'을 기준으로 나눈다.
        stime,etime = datetime.split('-')               #stime은 starttime 이고 etime은 endtime으로 '-'을 기준으로 나눠준다.
        if type == ' ': #연강인경우
            #print prevType, prevName, propessor, dateinfo
            lecturelist.append(lecture(prevType,prevName,propessor,day,stime,etime,location))   #앞에서 선언한 lecturelist 빈 리스트에 앞의 내용을 추가
        else:#연강이 아닌경우
            prevType = type                           #prevPype이라는 곳에 type을 넣는다
            prevName = name                          #prevName이라는 곳에 강의제목을 넣는다.
            #print type, name, propessor, dateinfo
            lecturelist.append(lecture(type, name, propessor, day, stime, etime, location)) #lecturelist에 넣는다
    #전체리스트를 돌면서
    curs.execute(sql, (login_query['user_id'], login_query['password']))  # user table채우기 #데이터베이스에 정보를 넣는다.
    for lecdata in lecturelist:                   #저장된 리스트를 돌면서
        print ('_' * 20)                          #출력하고
        lecdata.printinfo()                        #저장된 lecturelist에 들어있는 정보들을 출력한다.
        #id, type name prop, day st, et , location
        curs.execute(lecturesql, (login_query['user_id'], lecdata.type, lecdata.name,lecdata.propessor,lecdata.day,lecdata.startTime,lecdata.endTime,lecdata.location,'N',0,5))  # user table 채우기
        print ('_' * 20)   #▲데이터 베이스에 정보를 넣는다.
    #내꺼넌다

conn.commit()
conn.close()