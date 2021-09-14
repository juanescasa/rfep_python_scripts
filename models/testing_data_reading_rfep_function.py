# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 16:06:37 2021

@author: calle
"""
import pandas as pd
import read_data_rfep_function as rd_rfep
import solve_multiple_frvrp
import time

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
    
    output_multiple_frvrp = solve_multiple_frvrp.solve_multiple_frvrp(
        sVehiclesPaths = data_rfep["sVehiclesPaths"],
        sNodesVehiclesPaths = data_rfep["sNodesVehiclesPaths"],
        sStationsVehiclesPaths = data_rfep["sStationsVehiclesPaths"],
        sOriginalStationsOwn = data_rfep["sOriginalStationsOwn"],
        sOriginalStationsPotential = data_rfep["sOriginalStationsPotential"],
        sSuppliers = data_rfep["sSuppliers"],
        sSuppliersRanges = data_rfep["sSuppliersRanges"],
        sOriginVehiclesPaths = data_rfep["sOriginVehiclesPaths"],
        sDestinationVehiclesPaths = data_rfep["sDestinationVehiclesPaths"],
        sSequenceNodesNodesVehiclesPaths = data_rfep["sSequenceNodesNodesVehiclesPaths"],
        sFirstStationVehiclesPaths = data_rfep["sFirstStationVehiclesPaths"],
        sNotFirstStationVehiclesPaths = data_rfep["sNotFirstStationVehiclesPaths"],
        sNodesPotentialNodesOriginalVehiclesPaths = data_rfep["sNodesPotentialNodesOriginalVehiclesPaths"],
        sOriginalStationsMirrorStations = data_rfep["sOriginalStationsMirrorStations"],
        sStationsSuppliers = data_rfep["sStationsSuppliers"],
        sSuppliersWithDiscount = data_rfep["sSuppliersWithDiscount"],
        sRanges = data_rfep["sRanges"],
        pStartInventory = data_rfep["pStartInventory"],
        pTargetInventory = data_rfep["pTargetInventory"],
        pSafetyStock = data_rfep["pSafetyStock"],
        pTankCapacity = data_rfep["pTankCapacity"],
        pMinRefuel = data_rfep["pMinRefuel"],
        pConsumptionRate = data_rfep["pConsumptionRate"],
        pDistance = data_rfep["pDistance"],
        pConsumptionMainRoute = data_rfep["pConsumptionMainRoute"],
        pConsumptionOOP = data_rfep["pConsumptionOOP"],
        pQuantityVehicles = data_rfep["pQuantityVehicles"],
        pPrice = data_rfep["pPrice"],
        pOpportunityCost = data_rfep["pOpportunityCost"],
        pVariableCost = data_rfep["pVariableCost"],
        pDistanceOOP = data_rfep["pDistanceOOP"])
    
    
ls_track_time = ('finish_reading', time.time())