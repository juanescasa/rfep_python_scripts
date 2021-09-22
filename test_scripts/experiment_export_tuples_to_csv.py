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
rows = 10

for row in range(rows):
    tuple1 = (random.randint(1,3), "", random.randint(1,3), random.randint(1,3))
    "newline makes that there are not spaces with the following line"
    with open("output_test7.csv", "w", newline = "") as f:
        cw = csv.writer(f, delimiter=",")
        cw.writerow(tuple1)

di_event['start_print_from_memmory'] = time.time()

ls_tuples= []
for row in range(rows):
    tuple2 = (random.randint(1,3), random.randint(1,3), random.randint(1,3))
    ls_tuples.append(tuple2) 

with open("output_test5.csv", "w", newline = "") as f:
    cw = csv.writer(f, delimiter=",")
    cw.writerows(ls_tuples)

di_event['finish_print_from_memmory'] = time.time()

di_process_events = {"print_iteratively": ('start_print_iteratively', 'start_print_from_memmory'),
                     "print_from_memmory": ('start_print_from_memmory', 'finish_print_from_memmory')}

di_process_duration = {process: di_event[di_process_events[process][1]] - \
                       di_event[di_process_events[process][0]] \
                       for process in di_process_events}

#print dictionaries
header = ['process', 'duration']
with open('process_duration_iter_vs_mem.cv', 'w', newline = "") as f:
    cw = csv.writer(f, delimiter = "," )
    cw.writerow(header)
    for key in di_process_duration:
        cw.writerow([key, di_process_duration[key]])

#print dictionaries with tuple keys

di_quantity = {('st1', 'viva'):10,
                ('st2', 'gecs'):100,
                ('st3', 'terp'):5}

header2 = ['station', 'supplier', 'quantity']
with open('dic_tuple_index_print.cv', 'w', newline = "") as f:
    cw = csv.writer(f, delimiter = "," )
    cw.writerow(header2)
    for key in di_quantity:
        cw.writerow([key[0], key[1], di_quantity[key]])

#Experimenting exporting lists as columns

ls_col1 = ['Juan', 'Nico', 'Joha', 'Jime']
ls_col2 = [1989, 1992, 1989, 1993]
with open('print_list_col.cv', 'w', newline = "") as f:
    cw = csv.writer(f, delimiter = "," )
    cw.writerows((ls_col1, ls_col2))


