# encoding:utf-8
import hashlib


def get_signature(params_list):
    '''获取数字签名'''
    s = "".join(sorted(params_list))
    signature = hashlib.sha1(s.encode('utf-8')).hexdigest().upper().strip()
    # print signature
    return signature
