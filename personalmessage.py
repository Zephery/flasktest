# encoding=utf8
import time
import pytesseract

from PIL import Image
from selenium import webdriver
from models import *


def setperson(u0, p0):
    driver = webdriver.PhantomJS(executable_path='D:\phantomjs-2.1.1-windows\phantomjs.exe')
    # driver = webdriver.Firefox()
    url = 'http://ssfw.tjut.edu.cn/ssfw/login/ajaxlogin.do'
    driver.get(url)
    driver.maximize_window()
    driver.save_screenshot('static\images\i2.jpg')
    image = Image.open('static\images\i2.jpg')
    box = (703, 149, 766, 170)
    # box = (700, 130, 766, 150)
    image = image.crop(box)
    image = image.convert('L')
    image = image.convert('RGB')
    image.save('static\images\i4.jpg')
    print pytesseract.image_to_string(image).replace('\t', '')
    y0 = pytesseract.image_to_string(image).replace('\t', '')
    driver.find_element_by_id('j_username').send_keys(u0)
    driver.find_element_by_id('j_password').send_keys(p0)
    driver.find_element_by_id('validateCode').send_keys(y0)
    driver.find_element_by_id('loginBtn').click()
    time.sleep(2)
    js = 'window.location.href="http://ssfw.tjut.edu.cn/ssfw/xjgl/jbxx.do"'
    driver.execute_script(js)
    print driver.current_url
    try:
        # print driver.find_element_by_id('form1').find_element_by_id('yxdm').getText()
        print driver.find_element_by_id('xh').get_attribute('value')  # 学号
        student_id = driver.find_element_by_id('xh').get_attribute('value')
        print driver.find_element_by_id('xm').get_attribute('value')  # 姓名
        student_name = driver.find_element_by_id('xm').get_attribute('value')
        print driver.find_element_by_id('xbdm').get_attribute('value')  # 性别
        sex = driver.find_element_by_id('xbdm').get_attribute('value')
        print driver.find_element_by_id('njdm').get_attribute('value')  # 年级
        grade = driver.find_element_by_id('njdm').get_attribute('value')
        print driver.find_element_by_id('yxdm').get_attribute('value')  # 院系college
        college = driver.find_element_by_id('yxdm').get_attribute('value')
        print driver.find_element_by_id('zydm').get_attribute('value')  # 专业major
        major = driver.find_element_by_id('zydm').get_attribute('value')
        print driver.find_element_by_id('bjh').get_attribute('value')  # 所在班级
        inclass = driver.find_element_by_id('bjh').get_attribute('value')
        print driver.find_element_by_id('xzdm').get_attribute('value')  # 学制
        length_of_schooling = driver.find_element_by_id('xzdm').get_attribute('value')
        driver.close()
        try:
            print "................."
            u = User(student_id=student_id, student_name=student_name, sex=sex, grade=grade, college=college,
                     major=major,
                     inclass=inclass, length_of_schooling=length_of_schooling)
            db.session.add(u)
            db.session.commit()
        except Exception, e:
            print e
            pass
    except Exception, e:
        driver.close()
        print e
        setperson(u0, p0)
