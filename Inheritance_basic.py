# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 13:50:02 2020

@author: Manpreet Kour
"""

class Parent:        # define parent class
   def __init__(self):
      print("Calling parent constructor")

   def parentMethod(self):
      print('Calling parent method')

class Child(Parent): # define child class
   def __init__(self):
      print("Calling child constructor")

   def childMethod(self):
      print('Calling child method')

c = Child()          # instance of child

c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
