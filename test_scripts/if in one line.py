# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 16:28:53 2021

@author: calle
"""
fruit = 'apple'
fruit_value = 'banana'

a = 'Yes' if fruit == 'Apple' else 'No'

print(a)

ls_stations = ['s1', 's2']

di_capacity = {'s1': 5000}

index_station = 's3'
b = di_capacity['s3'] if index_station in ls_stations else 50

print(b)
