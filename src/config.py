# -*- coding: utf-8 -*-
from database import Database

class Config(object):
    # 各个全局参数,以及流动的数据
    # 类属性
    RELATIONSHIP = ["爷爷","婆婆","外爷","外婆","父亲","母亲"]
    # lastFamilyNumber = None
    pass

class GlobalData(object):
    # AFamilyInfo = {"young_name":None,"young_isMan":None,"relation":None,"old_name":None,"old_isMan":None}
    familyInfosList = []  # 存放新建的家庭成员们信息, 存放字典 AFamilyInfo
    searchInfoList = []
    @staticmethod #  装饰器
    def lastID():
        return Database.last_id()

    @staticmethod
    def lastFamilyIndex():
        return Database.last_familyIndex()

    @staticmethod
    def searchFamilyInfo(_word):
        GlobalData.searchInfoList = Database.search(_word)

if __name__ == '__main__':
    # db = Database()
    # db.insert_a_family_info(2,1,"赵",1,"爷爷","钱",1)
    print(type(GlobalData.lastID()),GlobalData.lastID())

