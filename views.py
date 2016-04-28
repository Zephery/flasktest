# encoding=utf8
import cookielib
import urllib2
import urllib
import MySQLdb
import chengji
import xuehao
import personalmessage
import personclass

from flask import request, render_template
from models import Flask

app = Flask(__name__)
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
conn = MySQLdb.Connect(host='localhost', user='root', passwd='root', db='kebiao', port=3306, charset='utf8')
cur = conn.cursor()
username = ''


@app.route("/login", methods=['POST', 'GET'])
def login():  # 首页代码
    error = None
    global username
    if request.method == 'POST':
        try:
            u0 = str(request.form['username'])  # 获取的用户名
            p0 = str(request.form['password'])  # 密码
            y0 = str(request.form['validatecode'])
            username = u0
            xuehao.xuehao = u0
            chuli(u0, p0, y0)  # 提交给后台处理
            personalmessage.setperson(u0, p0)
            return render_template('hello.html')
        except Exception, e:
            print e
            return
    else:
        f = open('static\images\y0.jpg', 'wb')
        f.write(opener.open(urllib2.Request("http://ssfw.tjut.edu.cn/ssfw/jwcaptcha.do")).read())
        f.flush()
        f.close()
        return render_template('login.html', error=error)


@app.route("/")
def index():
    return render_template('index.html')


def chuli(u0, p0, y0):  # 后台处理函数
    try:
        global opener
        print "====="
        opener.addheaders[0] = (
            'User-Agent',
            'Mozilla/5.0 (Windows NT 6.3;WOW64) Applewebkit/537.36(KHTML, like Gecko) Chrome/35.0.1916.114')
        opener.addheaders.append(('Referer', 'http://ssfw.tjut.edu.cn/ssfw/index.do'))
        opener.addheaders.append(('Accept-Language', 'zh-cn,zh;q=0.8'))
        opener.addheaders.append(('Host', 'ssfw.tjut.edu.cn'))
        opener.addheaders.append(('Connection', 'Keep-Alive'))
        value = {'j_username': u0, 'j_password': p0, 'validateCode': y0}  # 表单的数据
        urlcontent = opener.open(
            urllib2.Request("http://ssfw.tjut.edu.cn/ssfw/j_spring_ids_security_check", urllib.urlencode(value)))

        # personal class data
        classdata = opener.open(
            urllib2.Request('http://ssfw.tjut.edu.cn/ssfw/pkgl/kcbxx/4/2015-2016-2.do?xnxqdm=2015-2016-2&flag=4'))
        f = open('class.html', 'wb')
        f.write(classdata.read())
        f.flush()
        f.close()
        personclass.setclass(classdata)

        # score
        try:
            value2 = {'qXndm_ys': '2015-2016', 'qXqdm_ys': 1}  # 选取学期
            chengji_data = opener.open(
                urllib2.Request("http://ssfw.tjut.edu.cn/ssfw/zhcx/cjxx.do", urllib.urlencode(value2))).read(50000)
            chengji.adddata(chengji_data)

            value2 = {'qXndm_ys': '2014-2015', 'qXqdm_ys': 2}  # 选取学期
            chengji_data2 = opener.open(
                urllib2.Request("http://ssfw.tjut.edu.cn/ssfw/zhcx/cjxx.do", urllib.urlencode(value2))).read(50000)
            chengji.adddata(chengji_data2)

            value2 = {'qXndm_ys': '2014-2015', 'qXqdm_ys': 1}  # 选取学期
            chengji_data3 = opener.open(
                urllib2.Request("http://ssfw.tjut.edu.cn/ssfw/zhcx/cjxx.do", urllib.urlencode(value2))).read(50000)
            chengji.adddata(chengji_data3)

            value2 = {'qXndm_ys': '2013-2014', 'qXqdm_ys': 2}  # 选取学期
            chengji_data4 = opener.open(
                urllib2.Request("http://ssfw.tjut.edu.cn/ssfw/zhcx/cjxx.do", urllib.urlencode(value2))).read(50000)
            chengji.adddata(chengji_data4)

            value2 = {'qXndm_ys': '2013-2014', 'qXqdm_ys': 1}  # 选取学期
            chengji_data5 = opener.open(
                urllib2.Request("http://ssfw.tjut.edu.cn/ssfw/zhcx/cjxx.do", urllib.urlencode(value2))).read(50000)
            chengji.adddata(chengji_data5)

            value2 = {'qXndm_ys': '2012-2013', 'qXqdm_ys': 2}  # 选取学期
            chengji_data6 = opener.open(
                urllib2.Request("http://ssfw.tjut.edu.cn/ssfw/zhcx/cjxx.do", urllib.urlencode(value2))).read(50000)
            chengji.adddata(chengji_data6)

            value2 = {'qXndm_ys': '2012-2013', 'qXqdm_ys': 1}  # 选取学期
            chengji_data7 = opener.open(
                urllib2.Request("http://ssfw.tjut.edu.cn/ssfw/zhcx/cjxx.do", urllib.urlencode(value2))).read(50000)
            chengji.adddata(chengji_data7)
        except Exception, e:
            print e
            return

    except Exception, e:
        print e
        chuli(u0, p0, y0)


@app.route('/chengji', methods=['POST', 'GET'])
def show_entries():
    global username
    if request.method == 'POST':
        # print "su"
        qXndm_ys = request.form['qXndm_ys']  # 学年
        qXqdm_yx = request.form['qXqdm_ys']  # 学期
        # value_post = {'qXndm_ys': qXndm_ys, 'qXqdm_ys': qXqdm_yx}
        print qXndm_ys, qXqdm_yx
        print xuehao.xuehao
        try:
            sql0 = "select class_name,score from hello.score where " \
                   "school_year='" + qXndm_ys + "' and semester=(%s) and student_id=(%s)" % (
                str(qXqdm_yx), username)
            cur.execute(sql0)
            conn.commit()
        except Exception, e:
            print e
        entries0 = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
        # entries0=[dict(title=row[0], text=row[1]) for row in Score.query.all()]
        return render_template('chengji.html', entries=entries0)
    else:
        print xuehao.xuehao
        sql = "select class_name,score from hello.score where student_id=%s" % xuehao.xuehao
        cur.execute(sql)
        conn.commit()
        entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
        return render_template('chengji.html', entries=entries)


@app.route('/personalmessage', methods=['POST', 'GET'])
def person():
    print "person=========="
    person_sql = "select * from hello.users where student_id=%s" % xuehao.xuehao
    cur.execute(person_sql)
    conn.commit()
    entries = [
        dict(sid=row[0], sname=row[1], sex=row[2], grade=row[3], college=row[4], major=row[5], inclass=row[6],
             len=row[7])
        for row in cur.fetchall()]
    return render_template('personalmessage.html', entries=entries)


if __name__ == "__main__":
    app.run(debug=True)
