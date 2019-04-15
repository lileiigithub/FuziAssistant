# -*- coding: utf-8 -*-
from fuziLog import FzLog
import argparse
from database import Database

class Person(object):

    def __init__(self):
        self.name = None
        self.gender = None


class Relationship(object):
    pass

class AFamily(object):
    # class about a family

    def __init__(self,_family_index):
        self.family_index = _family_index   # 家庭标识号

    def insert_family_info(self, _young_name,_young_gender,_relation,_old_name,_old_gender):
        id = Database.last_id() + 1  #  操作 id
        Database.insert_a_family_info(id,self.family_index,_young_name,_young_gender,_relation,_old_name,_old_gender)

    def insert_family_info_list(self,infoList):
        for aInfo in infoList:
            self.insert_family_info(aInfo["young_name"],int(aInfo["young_isMan"]),
                                    aInfo["relation"],aInfo["old_name"],int(aInfo["old_isMan"]))

    def savePersonInfo(self):
        pass

    def saveRelationshipInfo(self):
        pass

    def saveDemandInfo(self):
        pass

class Demand(object):
    pass




