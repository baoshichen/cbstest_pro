#!/user/bin/python
# -*- coding:UTF-8 -*-

from selenium import webdriver
import time
from HTMLTestRunner import HTMLTestRunner
import unittest

class Chaomo25(unittest.TestCase):
    u'''超模网站自动化'''
    def setUp(self):
        self.browser = webdriver.Firefox()
#        self.browser.implicitly_wait(10)
        self.base_url = "http://www.chaomo25.com"

    def test_open_chaomo25(self):
        u'''打开超模网站'''
        browser = self.browser
        browser.get(self.base_url)
        time.sleep(2)
        browser.maximize_window()
        time.sleep(2)
        browser.find_element_by_link_text("产品").click()
        time.sleep(1)
        browser.find_element_by_link_text("故事").click()
        time.sleep(1)
        
#        js="var q=document.documentElement.scrollTop=200"
#        browser.execute_script(js)
#        time.sleep(3)
        
#        browser.find_element_by_xpath("//[@class='grid_item']/img[@alt='不要减了又减，我要减肥不反弹']").click()
        browser.find_element_by_xpath("/html/body/main/div/div/div[1]/div[1]/div/a/img").click()  
#        /html/body/main/div/div/div[1]/div[1]/div/a/img      

        


    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Chaomo25("test_open_chaomo25"))
#    testunit.addTest(Chaomo25("test_chaomo25_click"))
now = time.strftime("%Y-%m-%d %H_%M_%S")
filename = 'E:/python_examles/report/' + now + 'report.html'
fp = open(filename,'wb')
runner = HTMLTestRunner(stream=fp,title=u'超模25自动化测试结果',description=u'这里目前是空。。。。。。。')
runner.run(testunit)
fp.close()