# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 14:34:27 2021

@author: calle
"""
import numpy as np
from sys import getsizeof


a = np.array([1, 2, 3, 4])
stations = np.array(['st1', 'st2'], dtype = 'S')
print(getsizeof(stations))
print(stations)

stations = np.array(['st1', 'st2'])
print(getsizeof(stations))
print(stations)
