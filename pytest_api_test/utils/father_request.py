# encoding:utf-8
import requests


class Father_Request:

    def send_request(self, method, url, data, headers=None, cookies=None):
        if method == 'get':
            res = requests.get(url=url, params=data, headers=headers, cookies=cookies)
            return res

        elif method == 'post':
            res = requests.post(url=url, data=data, headers=headers, cookies=cookies)
            return res


if __name__ == '__main__':
    ss = Father_Request()
    url = 'http://ystwt.zyshow.cc'
    data = {
        "username": "admin",
        "password": 'password'
    }
    ss.send_request('post', url, data)
