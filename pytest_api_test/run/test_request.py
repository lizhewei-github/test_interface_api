# encoding:utf-8

import unittest
import ddt
import pytest
import allure

from utils.father_request import Father_Request
from utils.read_data import Read_Data
from config.config import Get_Config
from test_case.test_data import data
from common.my_log import My_Log

yaml_test_data = Read_Data().get_yaml_data(yaml_path="../test_case/yaml_data.yaml")['result']
print(yaml_test_data)
# print('123')
excel_test_data = Read_Data().get_excel_data(excel_path='../test_case/excel_data.xlsx', sheet_name='Sheet1')
# print(excel_test_data)

'''
def setup_module(self):
    print("setup_module：整个.py模块只执行一次")
    print("比如：所有用例开始前只打开一次浏览器")


def teardown_module(self):
    print("teardown_module：整个.py模块只执行一次")
    print("比如：所有用例结束只最后关闭浏览器")

def setup_function(self):
    print('每个用例执行前执行！')

def teardown_function(self):
    print('每个用例执行后执行！')
'''


@ddt.ddt
class Test_Yaml_Class(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @ddt.data(*yaml_test_data)
    def test_01(self, item):
        url = Get_Config().get_config('URL', 'server')
        method = 'get'
        res = Father_Request().send_request(method, url, eval(str(item['params'])))
        # 日志输入
        My_Log().info('================开始测试【{}】用例======【{}】==============='.format(item['case_id'], item['case_name']))
        My_Log().info('【请求url】:{}'.format(url))
        My_Log().info('【请求方式】:{}'.format(method))
        My_Log().info('【请求headers】:{}'.format(item['headers']))
        My_Log().info('【请求参数】:{}'.format(item['params']))
        My_Log().info('【响应参数】:{}'.format(res.text))
        My_Log().info('【Response code】:{}'.format(res.status_code))
        My_Log().info('【checkpoint】:{}'.format(item['checkpoint']))

        try:
            self.assertEqual(res.status_code, 200)
            self.assertIn(item['checkpoint']['reason'], res.text)
            test_result = 'Pass'
        except AssertionError as e:
            test_result = 'Failed'
            My_Log().error('断言出错了{}'.format(e))
            raise e
        finally:
            My_Log().info('本条用例的测试结论是:{}'.format(test_result))


@ddt.ddt
class Test_Excel_Class(unittest.TestCase):

    @ddt.data(*excel_test_data)
    def test_02(self, item):
        res = Father_Request().send_request(item['method'], item['url'], eval(str(item['params'])))
        # 日志输入
        My_Log().info('================开始测试【{}】用例======【{}】==============='.format(item['case_id'], item['case_name']))
        My_Log().info('【请求url】:{}'.format(item['url']))
        My_Log().info('【请求方式】:{}'.format(item['method']))
        My_Log().info('【请求headers】:{}'.format(item['headers']))
        My_Log().info('【请求参数】:{}'.format(item['params']))
        My_Log().info('【响应参数】:{}'.format(res.text))
        My_Log().info('【Response code】:{}'.format(res.status_code))
        My_Log().info('【checkpoint】:{}'.format(item['checkpoint']))

        try:
            self.assertEqual(res.status_code, 200)
            self.assertIn(item['checkpoint'], res.text)
            test_result = 'Pass'
        except AssertionError as e:
            test_result = 'Failed'
            My_Log().error('断言出错了{}'.format(e))
            raise e
        finally:
            My_Log().info('本条用例的测试结论是:{}'.format(test_result))

    @pytest.mark.skip(reason="未开发完成！")
    def test_03(self):
        assert (1 == 2)

    @allure.feature('测试用例3')
    def test_04(self):
        assert (3 == 4)
