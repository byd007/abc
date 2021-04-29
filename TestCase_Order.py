#coding=UTF-8
from public.pages.Place_Order import Place_Order
import unittest
from public.common.LoginData import LoginData
from time import sleep

class TestCase_Order(unittest.TestCase):

    def setUp(self):
        self.base_url =LoginData.get_base_url()

    def tearDown(self):
        pass

    def test01_place_order(self):
        try:
            #创建一个对象
            place_order = Place_Order()
            #打开了一个网址
            place_order.open(self.base_url)
            place_order.login('18617162994','qweqwe123')
            sleep(3)
            text = place_order.get_text('login')   #期望值：进入下单平台
            self.assertEqual(text,u'进入下单平台')
        except Exception as c:
            raise ValueError("testcase failed!!!")

if __name__ == '__main__':
    unittest.main()
