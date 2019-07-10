# encoding:utf-8
import time


class Get_time:

    def get_int_str_time(self):
        '''范回字符串类型不包含小数的时间戳'''
        return str(int(time.time()))

    def get_int_time(self):
        '''返回int类型不包含小数的时间'''
        return int(time.time())

    def get_normal_time(self):
        '''返回正常时间'''
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    def main(self):
        print(self.get_int_str_time())
        print(self.get_int_time())
        print(self.get_normal_time())


if __name__ == '__main__':
    ss = Get_time()
    ss.main()
