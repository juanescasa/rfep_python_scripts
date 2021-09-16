# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 16:06:37 2021

@author: calle
"""
import pandas as pd
import read_data_rfep_function as rd_rfep
import solve_multiple_frvrp
import time
import os

folder_relative_path = os.path.join("..", "data")
folder_name = "Path 2000"
folder_parent = folder_relative_path + folder_name + '\\'
file_name = "Scenario Map.xlsx"
file = folder_parent + file_name
sh = 'Generate Tables'
df_scenario_map = pd.read_excel(file, sheet_name = sh)

#%%

ls_track_time = ('start_test', time.time())
ls_tables = ['MaeNodes', 'MaeVehicles', 'MaeSuppliers', 'MaeRanges', 'MaePaths', 
             'NodesNodes', 'SubStations', 'VehiclesPaths', 'NodesPaths', 
             'SuppliersRanges', 'NodesNodesPaths']

#Read generator tables
folder_path = "C:\OneDrive - Deakin University\OD\calle test\Disun Applications\Gurobi Applications\data\\"
#Each scenario generator change this
folder_name = "Path 2000"
folder_parent = folder_path + folder_name + '\\'

file_name = "Scenario Map.xlsx"
file = folder_parent + file_name
sh = 'Generate Tables'
df_scenario_map = pd.read_excel(file, sheet_name = sh)

folder_child = folder_parent + "Generated tables\\"

di_table_name = {}

ls_track_time = ('start_reading', time.time())

di_duration_event_scenario = {} 
for index_scenario in [55]:
    for t in ls_tables:
        di_table_name[t]=t+"-"+df_scenario_map[t][index_scenario]
    
    data_rfep = rd_rfep.read_data_rfep(folder_child, di_table_name, 
                                       is_to_generate_scenarios=True)
    di_duration_event_scenario[index_scenario] =  data_rfep['di_time_event']
   
  
    
ls_track_time = ('finish_reading', time.time())