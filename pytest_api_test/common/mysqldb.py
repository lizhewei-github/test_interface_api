#encoding:utf-8
import sys
import pymysql
from utils import read_data


class My_Db():
    def __init__(self):
        self.data = read_data.Read_Data().get_yaml_data(yaml_path='../config/config.yaml')['result'][0]['DB1']
        print(self.data)

        #打开数据库连接（ip/端口/数据库用户名/登录密码/数据库名/编码）
        try:
            self.dbconn = pymysql.connect(**self.data)
        except Exception as e:
            print('初始化数据连接失败：%s' %e)
            sys.exit()

    def create_table(self,query):
        '''创建数据库表'''
        db_cursor = self.dbconn.cursor()
        try:
            db_cursor.execute(query)
            db_cursor.execute('commit')
            return True
        except Exception as e:
            print('创建数据库表失败：%s' %e)
            db_cursor.execute('rollback')
            db_cursor.close()
            exit()

    def select_record(self,query,data=''):
        '''返回结果只包含多条记录'''
        db_cursor = self.dbconn.cursor()
        try:
            if data:
                db_cursor.execute(query,data)
            else:
                db_cursor.execute(query)
            query_result = db_cursor.fetchall()
            for i in query_result:
                print(i)
            #return query_result
        except Exception as e:
            print('查询数据库失败: %s' %e)
            db_cursor.close()
            exit()
if __name__ =='__main__':
    query= 'select %s from %s where %s' \
            %('xml_data',\
              '10001_standard_medical_record',\
              '"doc_type" ="EMR050105"')
    My_Db().select_record(query)

