#coding=UTF-8
import unittest
import time
from run_all.HTMLTestRunnerCN import HTMLTestRunner
from TestCase.TestCase_Order import TestCase_Order
from config.globalconfig import report_path
from config.globalconfig import testcase_path
from public.common.mail import SendMail

now = time.strftime("%Y-%m-%d_%H_%M_%S")  #当前系统的时间
filename =report_path +"\\"+str(now)+"_ui_report.html"  #生成报告的路径
print (filename)

def AutoRun(TestCaseName):
    discover = unittest.defaultTestLoader.discover(
        testcase_path,pattern=TestCaseName)

    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title=u'UI自动化测试报告',description=
                            "用例执行情况如下：",tester='xiaowang')
    runner.run(discover)
    fp.close()

def send_mail():
    sm = SendMail(filename,attachment=filename)
    sm.send_mail()

if __name__ == '__main__':
    AutoRun("TestCas*.py")
    send_mail()  #调用send_mail方法进行邮件的发送

