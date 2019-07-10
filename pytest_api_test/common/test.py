# -*- coding: utf-8 -*-
import pytest
import requests


class Test_Class:
    def test_one(self):
        url1 = 'http://v.juhe.cn/telecode/to_telecodes.php'
        data = {'chars': '北京', 'key': 'e23273293b709acd3be5b9d66598179b'}
        res = requests.post(url1, data)
        print(res.status_code)
        print(res.text)
