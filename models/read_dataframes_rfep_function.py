# -*- coding: utf-8 -*-
"""
Created on Wed May 26 20:23:22 2021

@author: calle
Alejandro Calderon will work on this script
"""
import pandas as pd
import time

#Read tables as dataframes
#file = os.path.join("..", "data", "Data Model Generated Network-13.xlsm")
def read_dataframes_rfep(folder_path, dict_tables_name):
    """
    Parameters
    ----------
    folder_path : the path where all files csv are located
    
    dict_tables_name : dictionary which keys are the generic names of the tables 
    and values the table names for the given scenario (extensions denoting scenario)
    
    is_to_generate_scenarios: if we are reading tables to generate scenarios,
    it must be true, since it does not expect to find min refuelling and bounds 
    of the ranges of discounts. it must be false if we are reading to solve the problem
    
    -----
    
    """
    
    ls_tables = ['MaeNodes', 'MaeVehicles', 'MaeSuppliers', 'MaeRanges', 'MaePaths', 
              'NodesNodes', 'SubStations', 'VehiclesPaths', 'NodesPaths', 
              'SuppliersRanges', 'NodesNodesPaths']
    di_df_table = {}
    for table in ls_tables:        
        table_name = "\\" + dict_tables_name[table] + ".csv"
        table_path = folder_path + table_name
        di_df_table[table] = pd.read_csv(table_path)      
    return(di_df_table)