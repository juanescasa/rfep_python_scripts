# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 14:50:00 2021

@author: calle
"""
import pandas as pd
import read_data_rfep_function as rd_rfep
import rfep_model
import export_solution_rfep_csv
import time

ls_tables = ['MaeNodes', 'MaeVehicles', 'MaeSuppliers', 'MaeRanges', 'MaePaths', 
             'NodesNodes', 'SubStations', 'VehiclesPaths', 'NodesPaths', 
             'SuppliersRanges', 'NodesNodesPaths']

folder_path = "..\data\\"
#Each scenario generator change this
folder_name = "Toy instance"
folder_parent = folder_path + folder_name + '\\'
folder_child = folder_parent + "\\Generated tables"

#read scenario map
file_name = "Scenario Map.xlsx"
sh = 'Run Experiments'
file = folder_parent + file_name
df_scenario_map = pd.read_excel(file, sheet_name = sh)

di_table_name = {}


solution_algorithm="RFEP"
b_print_refuelling_detail = True


#Create list to store the results
ls_data_rfep = []
ls_scenario_name = []
ls_output_rfep = []
ls_total_time = []
ls_solution_algorithm = []

#for index_scenario in range(df_scenario_map.shape[0]):
#for index_scenario in range(23,150,1):
for index_scenario in [0]:
#for index_scenario in [0]:
    start_time = time.time()
    #read name of tables of scenario
    for t in ls_tables:
        di_table_name[t]=t+"-"+df_scenario_map[t][index_scenario]
    
    scenario_name = df_scenario_map["COD_SCENARIO"][index_scenario] + "-toy"
    
    #Read tables of the scenario and build the model
    data_rfep = rd_rfep.read_data_rfep(folder_child, di_table_name, 
                                       is_to_generate_scenarios=False)
    
    output_rfep = rfep_model.solve_rfep(
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
        retrieveSolutionDetail = True)
    
    total_time = time.time()-start_time
    
    if b_print_refuelling_detail:
        ls_data_rfep.append(data_rfep)
        
    ls_scenario_name.append(scenario_name)
    ls_output_rfep.append(output_rfep)
    ls_total_time.append(total_time)
    ls_solution_algorithm.append(solution_algorithm)
    
    
export_solution_rfep_csv.export_solution_rfep(ls_data_rfep = ls_data_rfep,
        ls_solution_algorithm = ls_solution_algorithm,
        ls_scenario_name = ls_scenario_name,
        ls_output_solve = ls_output_rfep,
        ls_total_time = ls_total_time,
        b_domain_reduction = False,
        b_print_refuelling_detail = b_print_refuelling_detail,
        b_print_refuelling_summary = True, 
        b_print_location_detail = True,
        b_print_location_summary = True,
        b_print_suppliers = True,
        b_print_statistics = True,
        b_retrieve_solve_ouput = True
        )


