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

excel_test_data = Read_Data().get_excel_data(excel_path='../test_case/excel_data.xlsx', sheet_name='Sheet1')


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
