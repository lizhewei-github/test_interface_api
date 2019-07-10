# encoding:utf-8
import configparser
import os


class Get_Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        if not os.path.exists(self.config_path):
            raise FileNotFoundError("请确保配置文件存在！")
        self.config.read(self.config_path, encoding='utf-8')

    def get_config(self, section, key):
        '''读取配置'''
        return self.config.get(section, key)
        # print(self.config.get(section,key))

    def set_config(self, section, key, text):
        '''修改配置文件'''
        self.config.set(section, key, text)
        with open(self.config_path, 'w+') as f:
            self.config.write(f)

    def add_config(self, section, key, value):
        '''新增配置文件'''
        self.config.add_section(section)
        self.config.set(section, key, value)
        with open(self.config_path, 'w+') as f:
            self.config.write(f)

    def main(self):
        section = "URL"
        key = "server"
        self.get_config(section, key)


if __name__ == '__main__':
    ss = Get_Config()
    ss.main()
