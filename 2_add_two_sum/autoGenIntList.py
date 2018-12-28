#!/usr/bin/python3
from random import randint
from node import Node
from listnode import ListNode

def checkInt(val):
    if type(val) is not int:
        raise TypeError("type should be int")
    else:
        return val

class AutoGenIntList(ListNode):
    def __init__(self, bottomBound, upBound):
        self.list = ListNode()
        self.botBound = checkInt(bottomBound)
        self.upBound = checkInt(upBound)
        self.defNum = None

    def setNumber(self, num):
        self.defNum = num

    def genIntList(self):
        val = self.defNum if self.defNum is not None else randint(self.botBound, self.upBound)
        print("val is: " + str(val))
        while val is not 0:
            self.list.addNode(val % 10)
            val = int(val / 10)


"""Test Code"""
AgList = AutoGenIntList(0, 100)
AgList.genIntList()
print(AgList.list)
