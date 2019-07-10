# encoding:utf-8
import logging
import time
import sys
import os
from logging.handlers import HTTPHandler
from utils.read_data import Read_Data


# 日志的级别：debug--info重要信息--waring警告信息-error错误信息-critical严重错误信息
# log_path = Read_Data().get_yaml_data(yaml_path='../config/config.yaml')
class My_Log:
    def my_log(self, level, msg):
        # 创建一个logger
        log_name = 'Auto_api_test.log'
        my_logger = logging.getLogger(log_name)

        # 设置logger的level
        my_logger.setLevel(level=logging.DEBUG)

        # 创建一个formatter,格式化输出
        formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S')
        # StreamHandler，输出至控制台
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(level=logging.DEBUG)
        stream_handler.setFormatter(formatter)
        my_logger.addHandler(stream_handler)

        # FileHandler,写入文件
        rq = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
        log_dir = (rq + ' auto_api_test.log')
        file_handler = logging.FileHandler('../log/{}'.format(log_dir))
        file_handler.setLevel(level=logging.INFO)
        file_handler.setFormatter(formatter)
        my_logger.addHandler(file_handler)

        # HTTPHandler
        # http_handler = HTTPHandler(host='localhost:8001', url='log', method='POST')
        # logger.addHandler(http_handler)

        if level == "DEBUG":
            my_logger.debug(msg)
        elif level == "INFO":
            my_logger.info(msg)
        elif level == "WARING":
            my_logger.warning(msg)
        elif level == "ERROR":
            my_logger.error(msg)
        elif level == "CRITICAL":
            my_logger.critical(msg)
        # 日志信息移除，防止重复
        my_logger.removeHandler(file_handler)
        my_logger.removeHandler(stream_handler)

    def debug(self, msg):
        self.my_log("DEBUG", msg)

    def info(self, msg):
        self.my_log("INFO", msg)

    def waring(self, msg):
        self.my_log("WARING", msg)

    def error(self, msg):
        self.my_log("ERROR", msg)

    def critical(self, msg):
        self.my_log("CRITICAL", msg)
