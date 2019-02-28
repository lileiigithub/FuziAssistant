# -*- coding: utf-8 -*-

class Person(object):
    def __init__(self):
        self.name = None
        self.gender = None
        self.father = None
        self.mother = None
        self.mate = None

class MatchPerson(object):
    def __init__(self):
        self.youngerName = None
        self.relationUp = None
        self.elderName = None
        self.relationDown = None

    def saveToDatabase(self):
        pass


