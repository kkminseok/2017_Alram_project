#-*- encoding:utf8 -*-
import pymysql
import sys
import main as data
from pyfcm import FCMNotification
import time
#___DB부분 변수
ip = 'localhost'
id = 'root'
pw = 'autoset'
name = 'kmsprj'
sql = "select * FROM lecture where id =" + data.login_query['user_id'] + " AND flag = 'Y';"

#firebase부분 변수
push_service = FCMNotification(api_key="AAAAWLONtIU:APA91bEPHZpoG1RBlgyIOTmz0gzDju-FHHDYLX8PAkGKblmclRLi5m61hKEbnI6S7mkWjXQzOcBA3-oxbMbFWLAo6EOTPCY8N1D1DuMrpl1l-Kv8revzPmiz8C5A6Iyo-PGm7qcW3Vyq")
registration_id = "ehXnubmOlRo:APA91bG__TljbAyIZ1Qo0kd4knYxQz9xC7Y_iZclVLMvrrlQRhl8D_c-C3pfA8XVfiHRx4A4i9pf4JT-6dcIL5TaSOgtzXaHPU9yF-mA480rBszFO1BOvvRMyrsyFo9PaXPHCRwCuKNz"
daylist = ['월','화','수','목','금','토','일']

def push_message(titlemsg, bodymsg):
    # Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging
    message_title = titlemsg
    message_body = bodymsg
    result = push_service.notify_topic_subscribers(topic_name="news",message_title=message_title, message_body=message_body,sound="Default")
    #result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body,sound="Default")
    print (result)
def calcmin(src, beforemin):
    _src = int(src)
    _bmin = int(beforemin)
    if _src - _bmin < 0: #음수야
        return 60 + (_src - _bmin) , -1
    else:
        return _src - _bmin, 0
if __name__ =="__main__":
    now = time.localtime()
    s = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    print("시작시간 :: ", s)
    while 1:
        time.sleep(1)
        now = time.localtime()
        if now.tm_sec == 0:
            s = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
            print("현재시간 :: ", s)
            conn = pymysql.connect(ip, id, pw, name, charset="utf8")
            curs = conn.cursor()
            curs.execute(sql)
            rs = curs.fetchall()
            conn.commit()
            conn.close()
            for row in rs:
                print (row)
                stime = str(row[6])
                shour,smin = stime.split(':')
                smin, carry = calcmin(smin, row[11])
                shour = int(shour) + int(carry)
                #print("시작시간 -> ::",str(int(shour)-row[10]) )
                #print("시작분 -> ::", smin)
                #if daylist[ now.tm_wday ] == row[5]:#요일체크
                if daylist[0] == row[5]: #0은 월요일 일단은 월요일 수업인거를 확인을 한다
                    if int(now.tm_hour) == int(int(shour)-row[10]): #시작시간이 같은경우
                        if int(now.tm_min) == int(smin): #완전히 딱걸린경우
                            title = row[3] + '-' + row[4] + '(' + row[5] + ')'
                            bodymsg = "수업시작 " + str(row[10]) +"시간 " + str(row[11]) + "분 전입니다"
                            push_message(title,bodymsg)