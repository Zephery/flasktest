# encoding=utf8
import xuehao

from bs4 import BeautifulSoup
from models import *


def adddata(data):
    uu = xuehao.xuehao
    # print uu
    # print "Testing"
    soup = BeautifulSoup(data, "html.parser")
    # i0=0
    school_year0 = soup.find(id='xndm_ys')["value"]  # 获取学年
    semester0 = soup.find(id='xqdm_ys')['value']  # 获取学期
    for i in soup.find_all('table')[7].find_all('tr'):
        # class_name0=str(uu)+'课程名称'+str(i0)
        class_id0 = ''
        class_name0 = ''
        # i0+=1
        # score0='成绩'
        score0 = ''
        for j0 in i.find_all('td')[2:3]:
            class_id0 = j0.get_text().strip()
        for j in i.find_all('td')[3:4]:
            # print j.get_text().strip()
            class_name0 = j.get_text().strip()
        for j1 in i.find_all('td')[8:9]:
            # print j1.get_text().strip()
            score0 = j1.get_text().strip()
        print class_id0, class_name0, score0
        try:
            if class_id0 == '':
                print
            else:
                s = Score(class_id=class_id0+'_'+str(xuehao.xuehao), class_name=class_name0, score=score0, school_year=
                school_year0, semester=semester0, student_id=uu)
                db.session.add(s)
                db.session.commit()
                # print "========GO========="

        except Exception, e:
            print e
            pass
