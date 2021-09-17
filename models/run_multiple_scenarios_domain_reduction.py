# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 18:03:49 2021

@author: calle
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 14:18:54 2021

@author: calle
"""

import pandas as pd
import gurobipy as gp
from gurobipy import GRB
import os
import time
import openpyxl
#import sys
import rfep_model
import export_solution_rfep
#this reads all data for the problem
#from read_data_rfep import *
import read_data_rfep_function as rd_rfep
import reduce_stations_path

start_time = time.time()

#%%
ls_track_time = ('start_test', time.time())
ls_tables = ['MaeNodes', 'MaeVehicles', 'MaeSuppliers', 'MaeRanges', 'MaePaths', 
             'NodesNodes', 'SubStations', 'VehiclesPaths', 'NodesPaths', 
             'SuppliersRanges', 'NodesNodesPaths']

#Read generator tables
folder_path = "..\data\\"

#Each scenario generator change this
folder_name = "Path 2000"
folder_parent = folder_path + folder_name + '\\'

file_name = "Scenario Map.xlsx"
file = folder_parent + file_name
sh = 'Run Experiments'
df_scenario_map = pd.read_excel(file, sheet_name = sh)

folder_child = folder_parent + "Generated tables\\"

di_table_name = {}

ls_track_time = ('start_reading', time.time())

di_duration_event_scenario = {} 
for index_scenario in [0]:
    for t in ls_tables:
        di_table_name[t]=t+"-"+df_scenario_map[t][index_scenario]
    
    data_rfep = rd_rfep.read_data_rfep(folder_child, di_table_name, 
                                       is_to_generate_scenarios=False)
    #di_duration_event_scenario[index_scenario] =  data_rfep['di_time_event']
       
    output_domain_reduction = reduce_stations_path.reduce_stations_path(
                            factor_options = 1,
                            factor_price = 2,
                            slack_reduction = 2,
                            sVehiclesPaths=data_rfep["sVehiclesPaths"],
                            sNodesVehiclesPaths=data_rfep["sNodesVehiclesPaths"],
                            sStationsVehiclesPaths=data_rfep["sStationsVehiclesPaths"],
                            sOriginalStationsOwn=data_rfep["sOriginalStationsOwn"],
                            sOriginalStationsPotential=data_rfep["sOriginalStationsPotential"],
                            sSuppliers=data_rfep["sSuppliers"],
                            sSuppliersRanges=data_rfep["sSuppliersRanges"],
                            sOriginVehiclesPaths=data_rfep["sOriginVehiclesPaths"],
                            sDestinationVehiclesPaths=data_rfep["sDestinationVehiclesPaths"],
                            sSequenceNodesNodesVehiclesPaths=data_rfep["sSequenceNodesNodesVehiclesPaths"],
                            sFirstStationVehiclesPaths=data_rfep["sFirstStationVehiclesPaths"],
                            sNotFirstStationVehiclesPaths=data_rfep["sNotFirstStationVehiclesPaths"],
                            sNodesPotentialNodesOriginalVehiclesPaths=data_rfep["sNodesPotentialNodesOriginalVehiclesPaths"],
                            sOriginalStationsMirrorStations=data_rfep["sOriginalStationsMirrorStations"],
                            sStationsSuppliers=data_rfep["sStationsSuppliers"],
                            sSuppliersWithDiscount=data_rfep["sSuppliersWithDiscount"],
                            sRanges=data_rfep["sRanges"],
                            pStartInventory=data_rfep["pStartInventory"],
                            pTargetInventory=data_rfep["pTargetInventory"],
                            pSafetyStock=data_rfep["pSafetyStock"],
                            pTankCapacity=data_rfep["pTankCapacity"],
                            pMinRefuel=data_rfep["pMinRefuel"],
                            pConsumptionRate=data_rfep["pConsumptionRate"],
                            pDistance=data_rfep["pDistance"],
                            pConsumptionMainRoute=data_rfep["pConsumptionMainRoute"],
                            pConsumptionOOP=data_rfep["pConsumptionOOP"],
                            pQuantityVehicles=data_rfep["pQuantityVehicles"],
                            pPrice=data_rfep["pPrice"],
                            pOpportunityCost=data_rfep["pOpportunityCost"],
                            pVariableCost=data_rfep["pVariableCost"],
                            pDistanceOOP=data_rfep["pDistanceOOP"])                 
                     
    sNodesVehiclesPaths2=output_domain_reduction[0]
    sStationsVehiclesPaths2=output_domain_reduction[1]
    sSequenceNodesNodesVehiclesPaths2=output_domain_reduction[2]
    sFirstStationVehiclesPaths2=output_domain_reduction[3]
    sNotFirstStationVehiclesPaths2=output_domain_reduction[4]
    sNodesPotentialNodesOriginalVehiclesPaths2=output_domain_reduction[5]
    sStationsPaths2 = output_domain_reduction[6]
    pSubDistance = output_domain_reduction[7]
    pConsumptionMainRoute2=output_domain_reduction[8]

# output_rfep = rfep_model.solve_rfep(
#                 sNodesVehiclesPaths = sNodesVehiclesPaths2,
#                 sStationsVehiclesPaths = sStationsVehiclesPaths2,
#                 sOriginalStationsOwn = sOriginalStationsOwn,
#                 sOriginalStationsPotential = sOriginalStationsPotential,
#                 sSuppliers = sSuppliers,
#                 sSuppliersRanges = sSuppliersRanges,
#                 sOriginVehiclesPaths = sOriginVehiclesPaths,
#                 sDestinationVehiclesPaths = sDestinationVehiclesPaths,
#                 sSequenceNodesNodesVehiclesPaths = sSequenceNodesNodesVehiclesPaths2,
#                 sFirstStationVehiclesPaths = sFirstStationVehiclesPaths2,
#                 sNotFirstStationVehiclesPaths = sNotFirstStationVehiclesPaths2,
#                 sNodesPotentialNodesOriginalVehiclesPaths = sNodesPotentialNodesOriginalVehiclesPaths2,
#                 sOriginalStationsMirrorStations = sOriginalStationsMirrorStations,
#                 sStationsSuppliers = sStationsSuppliers,
#                 sSuppliersWithDiscount = sSuppliersWithDiscount,
#                 sRanges = sRanges,
#                 pStartInventory = pStartInventory,
#                 pTargetInventory = pTargetInventory,
#                 pSafetyStock = pSafetyStock,
#                 pTankCapacity = pTankCapacity,
#                 pMinRefuel = pMinRefuel,
#                 pConsumptionMainRoute = pConsumptionMainRoute2,
#                 pConsumptionOOP = pConsumptionOOP,
#                 pQuantityVehicles = pQuantityVehicles,
#                 pStationCapacity = pStationCapacity,
#                 pStationUnitCapacity = pStationUnitCapacity,
#                 pMinimumPurchaseQuantity = pMinimumPurchaseQuantity,
#                 pLowerQuantityDiscount = pLowerQuantityDiscount,
#                 pUpperQuantityDiscount = pUpperQuantityDiscount,
#                 pPrice = pPrice,
#                 pOpportunityCost = pOpportunityCost,
#                 pVariableCost = pVariableCost,
#                 pDistanceOOP = pDistanceOOP,
#                 pCostUnitCapacity = pCostUnitCapacity,
#                 pDiscount = pDiscount,
#                 pLocationCost = pLocationCost,
#                 isONvInventory = True,
#                 isONvRefuelQuantity = True,
#                 isONvRefuel = True,
#                 isONvQuantityUnitsCapacity = True,
#                 isONvLocate = True,
#                 isONvQuantityPurchased = True,
#                 isONvQuantityPurchasedRange = True,
#                 isONvPurchasedRange = True,
#                 isONcInitialInventory = True,
#                 isONcTargetInventory = True,
#                 isONcMinInventory = True,
#                 isONcLogicRefuel1 = True,
#                 isONcLogicRefuel2 = True,
#                 isONcMaxRefuel = True,
#                 isONcInventoryBalance1 = True,
#                 isONcInventoryBalance2 = True,
#                 isONcInventoryBalance3 = True,
#                 isONcLogicLocation = True,
#                 isONcLogicLocation2 = True,
#                 isONcStationCapacity = True,
#                 isONcQuantityPurchased = True,
#                 isONcMinimumQuantitySupplier = True,
#                 isONcMinQuantityRange = True,
#                 isONcMaxQuantityRange = True,
#                 isONcUniqueQuantityRange = True,
#                 isONcUniqueRange = True,
#                 isONtotalRefuellingCost= True,
#                 isONtotalLocationCost= True,
#                 isONtotalDiscount= True)

# output_file = os.path.join("..", "output", "outputRFEP_v2.xlsx")
# scenario_name = "RFEP after domain reduction"
# total_time = time.time()-start_time

# export_solution_rfep.export_solution_rfep(
#                                         excel_input_file = file,
#                                         excel_output_file = output_file,
#                                         scenario_name = scenario_name,
#                                         output_solve = output_rfep,
#                                         total_time = total_time,
#                                         b_domain_reduction = True,
#                                         b_print_solution_detail = True,
#                                         b_print_location = True,
#                                         b_print_statistics = True,
#                                         sVehiclesPaths = sVehiclesPaths,
#                                         sOriginalStationsPotential = sOriginalStationsPotential,
#                                         sSequenceNodesNodesVehiclesPaths = sSequenceNodesNodesVehiclesPaths2,
#                                         sStationsPaths = sStationsPaths2,
#                                         sOriginalStationsOwn = sOriginalStationsOwn,
#                                         sStationsVehiclesPaths = sStationsVehiclesPaths2,
#                                         sSuppliersRanges = sSuppliersRanges,
#                                         pStartInventory = pStartInventory,
#                                         pConsumptionRate = pConsumptionRate,
#                                         pSubDistance = pSubDistance,
#                                         pConsumptionMainRoute = pConsumptionMainRoute2,
#                                         pDistanceOOP = pDistanceOOP,
#                                         pConsumptionOOP = pConsumptionOOP,
#                                         pQuantityVehicles = pQuantityVehicles,
#                                         pVariableCost = pVariableCost,
#                                         pOpportunityCost = pOpportunityCost,
#                                         pLocationCost = pLocationCost,
#                                         pStationCapacity = pStationCapacity,
#                                         pStationUnitCapacity = pStationUnitCapacity,
#                                         pCostUnitCapacity = pCostUnitCapacity,
#                                         pPrice = pPrice,
#                                         pDiscount = pDiscount)
