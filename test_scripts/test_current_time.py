# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 19:02:13 2021

@author: calle
"""
# importing datetime module for now() 
import datetime 
    
# using now() to get current time 
current_time = datetime.datetime.now() 
    
# Printing value of now. 
print ("Time now at greenwich meridian is : "
                                    , end = "") 
print (current_time)

#get the node name
import platform
my_system = platform.uname()[1]

empty_dict = {}
print(len(empty_dict))
