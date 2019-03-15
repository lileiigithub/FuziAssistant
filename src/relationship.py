# -*- coding: utf-8 -*-
from fuziLog import FzLog
import argparse

class Person(object):

    def __init__(self):
        self.name = None
        self.gender = None
        # self.father = None
        # self.mother = None
        # self.mate = None


class Relationship(object):

    def __init__(self, _younger_person_obj, _older_person_obj, _relation):
        self.younger = _younger_person_obj
        self.relation = _relation
        self.elderName = _older_person_obj

    def savePersonInfo(self):
        pass

    def saveRelationshipInfo(self):
        pass

    def saveDemandInfo(self):
        pass


class Demand(object):
    pass


class FamilyInfo(object):
    pass



