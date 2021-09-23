# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 16:53:24 2021

@author: calle
"""
di_locate={'st1':1,
           'st2':1,
           'st5':1}

ls_stations = list(di_locate.keys())

for i in di_locate.keys():
    print(i)

di_refuel = {('st1', 'v1'): 5,
           ('st1', 'v2'): 5,
           ('st5', 'v3'): 5,
           ('st2', 'v4'): 5,}

sStationsVehiclesTest = list(di_refuel.keys())

for (i,v) in sStationsVehiclesTest:
    print((i,v))

