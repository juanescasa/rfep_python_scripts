# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 15:13:48 2021

@author: calle
"""
import time
import csv
import random


di_event={}
di_event['start_print_iteratively'] = time.time()
rows = 10000

for row in range(rows):
    tuple1 = (random.randint(1,3), "", random.randint(1,3), random.randint(1,3))
    with open("output_test7.csv", "a", newline = "") as f:
        cw = csv.writer(f, delimiter=",")
        cw.writerow(tuple1)

di_event['start_print_from_memmory'] = time.time()

ls_tuples= []
for row in range(rows):
    tuple2 = (random.randint(1,3), random.randint(1,3), random.randint(1,3))
    ls_tuples.append(tuple2) 

with open("output_test5.csv", "a", newline = "") as f:
    cw = csv.writer(f, delimiter=",")
    cw.writerows(ls_tuples)

di_event['finish_print_from_memmory'] = time.time()

di_process_events = {"print_iteratively": ('start_print_iteratively', 'start_print_from_memmory'),
                     "print_from_memmory": ('start_print_from_memmory', 'finish_print_from_memmory')}

di_process_duration = {process: di_event[di_process_events[process][1]] - \
                       di_event[di_process_events[process][0]] \
                       for process in di_process_events}



