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

class FamilyInfo(object):
    def __init__(self,_family_index):
        self.family_index = _family_index
        self.id = Database.last_id()+1
        # self.younger = _younger_person_obj
        # self.relation = _relation
        # self.elderName = _older_person_obj

    def insert_family_info(self,_young_name,_young_gender,_relation,_old_name,_old_gender):
        Database.insert_family_info(self.id,self.family_index,_young_name,_young_gender,_relation,_old_name,_old_gender)

    def savePersonInfo(self):
        pass

    def saveRelationshipInfo(self):
        pass

    def saveDemandInfo(self):
        pass

class Demand(object):
    pass




