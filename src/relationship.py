# -*- coding: utf-8 -*-
from fuziLog import FzLog
import argparse
from database import Database

class Person(object):

    def __init__(self):
        self.name = None
        self.gender = None
        # self.father = None
        # self.mother = None
        # self.mate = None

class Relationship(object):
    pass

class AFamily(object):
    # class about a family
    def __init__(self,_family_index):
        self.family_index = _family_index

    def insert_family_info(self,_young_name,_young_gender,_relation,_old_name,_old_gender):
        id = Database.last_id() + 1
        Database.insert_family_info(id,self.family_index,_young_name,_young_gender,_relation,_old_name,_old_gender)

    def savePersonInfo(self):
        pass

    def saveRelationshipInfo(self):
        pass

    def saveDemandInfo(self):
        pass

class Demand(object):
    pass




