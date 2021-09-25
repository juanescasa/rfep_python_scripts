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
import export_solution_rfep_csv
#this reads all data for the problem
#from read_data_rfep import *
import read_data_rfep_function as rd_rfep
import reduce_stations_path



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
#Create list to store the results
ls_data_rfep = []
ls_scenario_name = []
ls_output_rfep = []
ls_total_time = []
ls_solution_algorithm = []
#create dictionary to store the variables values after the domain reduction
mip_start = {} 
#for index_scenario in [0,1]:
#for index_scenario in range(50):
for index_scenario in range(20):
    start_time = time.time()    
    for t in ls_tables:
        di_table_name[t]=t+"-"+df_scenario_map[t][index_scenario]
    
    data_rfep = rd_rfep.read_data_rfep(folder_child, di_table_name, 
                                       is_to_generate_scenarios=False)
    #di_duration_event_scenario[index_scenario] =  data_rfep['di_time_event']
       
    output_domain_reduction = reduce_stations_path.reduce_stations_path(
                            factor_options = 3,
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
    
    #redefine the sets and parameters after domain reduction               
    sNodesVehiclesPaths2=output_domain_reduction[0]
    sStationsVehiclesPaths2=output_domain_reduction[1]
    sSequenceNodesNodesVehiclesPaths2=output_domain_reduction[2]
    sFirstStationVehiclesPaths2=output_domain_reduction[3]
    sNotFirstStationVehiclesPaths2=output_domain_reduction[4]
    sNodesPotentialNodesOriginalVehiclesPaths2=output_domain_reduction[5]
    sStationsPaths2 = output_domain_reduction[6]
    pSubDistance = output_domain_reduction[7]
    pConsumptionMainRoute2=output_domain_reduction[8]

    output_rfep = rfep_model.solve_rfep(
                sNodesVehiclesPaths = sNodesVehiclesPaths2,
                sStationsVehiclesPaths = sStationsVehiclesPaths2,
                sOriginalStationsOwn = data_rfep["sOriginalStationsOwn"],
                sOriginalStationsPotential = data_rfep["sOriginalStationsPotential"],
                sSuppliers = data_rfep["sSuppliers"],
                sSuppliersRanges = data_rfep["sSuppliersRanges"],
                sOriginVehiclesPaths = data_rfep["sOriginVehiclesPaths"],
                sDestinationVehiclesPaths = data_rfep["sDestinationVehiclesPaths"],
                sSequenceNodesNodesVehiclesPaths = sSequenceNodesNodesVehiclesPaths2,
                sFirstStationVehiclesPaths = sFirstStationVehiclesPaths2,
                sNotFirstStationVehiclesPaths = sNotFirstStationVehiclesPaths2,
                sNodesPotentialNodesOriginalVehiclesPaths = sNodesPotentialNodesOriginalVehiclesPaths2,
                sOriginalStationsMirrorStations = data_rfep["sOriginalStationsMirrorStations"],
                sStationsSuppliers = data_rfep["sStationsSuppliers"],
                sSuppliersWithDiscount = data_rfep["sSuppliersWithDiscount"],
                sRanges = data_rfep["sRanges"],
                pStartInventory = data_rfep["pStartInventory"],
                pTargetInventory = data_rfep["pTargetInventory"],
                pSafetyStock = data_rfep["pSafetyStock"],
                pTankCapacity = data_rfep["pTankCapacity"],
                pMinRefuel = data_rfep["pMinRefuel"],
                pConsumptionMainRoute = pConsumptionMainRoute2,
                pConsumptionOOP = data_rfep["pConsumptionOOP"],
                pQuantityVehicles = data_rfep["pQuantityVehicles"],
                pStationCapacity = data_rfep["pStationCapacity"],
                pStationUnitCapacity = data_rfep["pStationUnitCapacity"],
                pMinimumPurchaseQuantity = data_rfep["pMinimumPurchaseQuantity"],
                pLowerQuantityDiscount = data_rfep["pLowerQuantityDiscount"],
                pUpperQuantityDiscount = data_rfep["pUpperQuantityDiscount"],
                pPrice = data_rfep["pPrice"],
                pOpportunityCost = data_rfep["pOpportunityCost"],
                pVariableCost = data_rfep["pVariableCost"],
                pDistanceOOP = data_rfep["pDistanceOOP"],
                pCostUnitCapacity = data_rfep["pCostUnitCapacity"],
                pDiscount = data_rfep["pDiscount"],
                pLocationCost = data_rfep["pLocationCost"],
                isONvInventory = True,
                isONvRefuelQuantity = True,
                isONvRefuel = True,
                isONvQuantityUnitsCapacity = True,
                isONvLocate = True,
                isONvQuantityPurchased = True,
                isONvQuantityPurchasedRange = True,
                isONvPurchasedRange = True,
                isONcInitialInventory = True,
                isONcTargetInventory = True,
                isONcMinInventory = True,
                isONcLogicRefuel1 = True,
                isONcLogicRefuel2 = True,
                isONcMaxRefuel = True,
                isONcInventoryBalance1 = True,
                isONcInventoryBalance2 = True,
                isONcInventoryBalance3 = True,
                isONcLogicLocation = True,
                isONcLogicLocation2 = True,
                isONcStationCapacity = True,
                isONcQuantityPurchased = True,
                isONcMinimumQuantitySupplier = True,
                isONcMinQuantityRange = True,
                isONcMaxQuantityRange = True,
                isONcUniqueQuantityRange = True,
                isONcUniqueRange = True,
                isONtotalRefuellingCost = True,
                isONtotalLocationCost = True,
                isONtotalDiscount = True,
                timeLimit = 3600)
    #store the value of the variables
    mip_start["vInventory"]=output_rfep[1]
    mip_start["vRefuelQuantity"]=output_rfep[23]
    mip_start["vRefuel"]=output_rfep[24]
    mip_start["vQuantityUnitsCapacity"]=output_rfep[4]
    mip_start["vLocate"]=output_rfep[5]
    mip_start["vQuantityPurchased"]=output_rfep[6]
    mip_start["vQuantityPurchasedRange"]=output_rfep[7]
    mip_start["vPurchasedRange"]=output_rfep[8]    

    
    output_rfep2 = rfep_model.solve_rfep(
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
                pConsumptionMainRoute = data_rfep["pConsumptionMainRoute"],
                pConsumptionOOP = data_rfep["pConsumptionOOP"],
                pQuantityVehicles = data_rfep["pQuantityVehicles"],
                pStationCapacity = data_rfep["pStationCapacity"],
                pStationUnitCapacity = data_rfep["pStationUnitCapacity"],
                pMinimumPurchaseQuantity = data_rfep["pMinimumPurchaseQuantity"],
                pLowerQuantityDiscount = data_rfep["pLowerQuantityDiscount"],
                pUpperQuantityDiscount = data_rfep["pUpperQuantityDiscount"],
                pPrice = data_rfep["pPrice"],
                pOpportunityCost = data_rfep["pOpportunityCost"],
                pVariableCost = data_rfep["pVariableCost"],
                pDistanceOOP = data_rfep["pDistanceOOP"],
                pCostUnitCapacity = data_rfep["pCostUnitCapacity"],
                pDiscount = data_rfep["pDiscount"],
                pLocationCost = data_rfep["pLocationCost"],
                isONvInventory = True,
                isONvRefuelQuantity = True,
                isONvRefuel = True,
                isONvQuantityUnitsCapacity = True,
                isONvLocate = True,
                isONvQuantityPurchased = True,
                isONvQuantityPurchasedRange = True,
                isONvPurchasedRange = True,
                isONcInitialInventory = True,
                isONcTargetInventory = True,
                isONcMinInventory = True,
                isONcLogicRefuel1 = True,
                isONcLogicRefuel2 = True,
                isONcMaxRefuel = True,
                isONcInventoryBalance1 = True,
                isONcInventoryBalance2 = True,
                isONcInventoryBalance3 = True,
                isONcLogicLocation = True,
                isONcLogicLocation2 = True,
                isONcStationCapacity = True,
                isONcQuantityPurchased = True,
                isONcMinimumQuantitySupplier = True,
                isONcMinQuantityRange = True,
                isONcMaxQuantityRange = True,
                isONcUniqueQuantityRange = True,
                isONcUniqueRange = True,
                isONtotalRefuellingCost = True,
                isONtotalLocationCost = True,
                isONtotalDiscount = True,
                timeLimit = 3600,
                mip_start = mip_start)
    
    

    
    
    total_time = time.time()-start_time
    scenario_name = df_scenario_map["COD_SCENARIO"][index_scenario] + "-lenPath2000"
    solution_algorithm = "drx3-mipstart-RFEP"
    
    
    
    #Create the list to store results, statistics and inputs from the scenarios        
    ls_output_rfep.append(output_rfep2)
    ls_scenario_name.append(scenario_name)
    ls_total_time.append(total_time)
    ls_solution_algorithm.append(solution_algorithm)
    #Comment line below when you do not need to export details of the scenario
    #it just creates the parameters to export with the outputs
    # data_rfep["sNodesVehiclesPaths"] = sNodesVehiclesPaths2
    # data_rfep["sStationsVehiclesPaths"] = sStationsVehiclesPaths2
    # data_rfep["sSequenceNodesNodesVehiclesPaths"] = sSequenceNodesNodesVehiclesPaths2
    # data_rfep["sFirstStationVehiclesPaths"] = sFirstStationVehiclesPaths2
    # data_rfep["sNotFirstStationVehiclesPaths"]=sNotFirstStationVehiclesPaths2
    # data_rfep["sNodesPotentialNodesOriginalVehiclesPaths"]=sNodesPotentialNodesOriginalVehiclesPaths2
    # data_rfep["sStationsPaths"] = sStationsPaths2
    # data_rfep["pSubDistance"] = pSubDistance
    # data_rfep["pConsumptionMainRoute"]=pConsumptionMainRoute2
    # ls_data_rfep.append(data_rfep)
    
export_solution_rfep_csv.export_solution_rfep(#ls_data_rfep = ls_data_rfep,
        ls_solution_algorithm = ls_solution_algorithm,
        ls_scenario_name = ls_scenario_name,
        ls_output_solve = ls_output_rfep,
        ls_total_time = ls_total_time,
        b_domain_reduction = True,
        b_print_refuelling_detail = False,
        b_print_refuelling_summary = True,        
        b_print_location = True,
        b_print_location_summary = True,
        b_print_statistics = True,
        b_retrieve_solve_ouput = True,
        )    
    
