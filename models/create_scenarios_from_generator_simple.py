# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 14:47:39 2021

@author: calle
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 11:26:24 2021

@author: calle
"""
import pandas as pd
import read_data_rfep_function as rd_rfep
import solve_multiple_frvrp
import time
import os
import random

#This silence a warning from pandas when assigning elements of DataFrames. 
#The best option to assign is using iloc, but this makes the code less readable, 
#since we must use the index of rows and columns
pd.options.mode.chained_assignment = None

def export_mae_suppliers(folder, df_substations, df_generator_mae_suppliers, p_level, l_level):
    export_string = folder + "MaeSuppliers-pa"+str(p_level) + "-su" + str(l_level) + ".csv"
    df_mae_suppliers = pd.DataFrame(df_substations["COD_SUPPLIER"].unique(), columns=["COD_SUPPLIER"])
    df_mae_suppliers2 = pd.merge(df_generator_mae_suppliers, df_mae_suppliers, how = 'inner', on = ['COD_SUPPLIER'])
    df_mae_suppliers2.to_csv(export_string, index=False)
    return(df_mae_suppliers, df_mae_suppliers2)

def export_suppliers_ranges(folder, df_generator_suppliers_ranges, df_mae_suppliers, p_level, l_level):
    export_string = folder + "SuppliersRanges-pa"+str(p_level) + "-su" + str(l_level) + ".csv"
    df_suppliers_ranges = pd.merge(df_generator_suppliers_ranges, df_mae_suppliers, \
                                    how = 'inner', on = ['COD_SUPPLIER'])
    df_suppliers_ranges.to_csv(export_string, index=False)
    return(df_suppliers_ranges)

def export_substations(folder, sr_level_own, sr_level_candidate, df_substations, 
                        survivor_supplier, l_level, set_valid_l_ow_cl):
    df_substations_aux = df_substations.copy()
    for ow_level in sr_level_own:
        for cl_level in sr_level_candidate:
            if (l_level, ow_level, cl_level) in set_valid_l_ow_cl:
                if (l_level, ow_level, cl_level)==(1,0,0):
                    export_string = folder + "SubStations-pa"+str(p_level) + \
                        "-ow"+ str(ow_level) + "-cl" + str(cl_level) + "-su" + \
                            str(l_level) + ".csv"
                    df_substations_aux.to_csv(export_string, index=False)
                else:
                        
                    qty_current_stations_supplier = df_substations_aux['COD_SUPPLIER'].value_counts()
                    qty_current_own = qty_current_stations_supplier['OWN']
                    stations_to_select = qty_current_own - ow_level
                    stations_selected = 0
                    row_substations = 0
                    while stations_selected < stations_to_select:
                        row_substations +=1
                        if df_substations_aux['COD_SUPPLIER'][row_substations]=='OWN':
                            df_substations_aux['COD_SUPPLIER'][row_substations] = survivor_supplier
                            stations_selected +=1
                        
                                                     
                    stations_selected = 0
                    row_substations = 0
                    while stations_selected < cl_level:
                        row_substations +=1
                        if df_substations_aux['COD_SUPPLIER'][row_substations]== 'OWN':
                            df_substations_aux['isPotential'][row_substations] = 1
                            stations_selected +=1
                    export_string = folder + "SubStations-pa"+str(p_level) + \
                        "-ow"+ str(ow_level) + "-cl" + str(cl_level) + "-su" + \
                            str(l_level) + ".csv"
                    
                    df_substations_aux.to_csv(export_string, index=False)
                    df_substations_aux = df_substations.copy()

ls_start_time = []
ls_start_time.append(("Gen Inititial tables", time.time()))

#Read generator tables
#folder_path = "C:\OneDrive - Deakin University\OD\calle test\Disun Applications\Gurobi Applications\data\\"
folder_path = "..\\data\\"
#Each scenario generator change this

folder_name = "Toy 2"
folder_parent = folder_path + folder_name + '\\'

ls_tables = ['MaeNodes', 'MaeVehicles', 'MaeSuppliers', 'MaeRanges', 'MaePaths', 
              'NodesNodes', 'SubStations', 'VehiclesPaths', 'NodesPaths', 
              'SuppliersRanges', 'NodesNodesPaths']
di_df_tables = {}
for t in ls_tables:
    table_name = t
    table_path = folder_parent + table_name + ".csv"
    di_df_tables[t]=pd.read_csv(table_path)

#read parameters to generate tables
file_name = "Generation parameters.xlsx"
file =  folder_parent + file_name
sh = 'Sheet1'
df_generation_parameters = pd.read_excel(file, sheet_name = sh)
#Read capacity_cost
capacity_cost = df_generation_parameters['Value'][0]
#Read fuel consumption
total_fuel_consumption = df_generation_parameters['Value'][1]
#Read percentage allocation to minimum quantity supplier
allocation_min_qty_supplier = df_generation_parameters['Value'][2]

#read scenario map
file_name = "Scenario Map.xlsx"
file = folder_parent + file_name
sh = 'Generate Tables'
df_scenario_map = pd.read_excel(file, sheet_name = sh)

#define folder to output the tables
folder_child = folder_parent + "Generated tables\\"

#read levels of factors
sr_level_vehicles = df_scenario_map['Type of vehicles'].unique()
sr_level_paths = df_scenario_map['Quantity of paths'].unique()
sr_level_suppliers = df_scenario_map['Quantity suppliers'].unique()
sr_level_own = df_scenario_map['Quantity own stations'].unique()
sr_level_candidate = df_scenario_map['Quantity candidate locations'].unique()

ls_valid_l_ow_cl = []
#read valid combinations own stations * candidate locations
for row_sm in range(df_scenario_map.shape[0]):
    l_level = df_scenario_map['Quantity suppliers'][row_sm]
    ow_level = df_scenario_map['Quantity own stations'][row_sm]
    cl_level = df_scenario_map['Quantity candidate locations'][row_sm]
    ls_valid_l_ow_cl.append((l_level, ow_level, cl_level))

#I convert into set to get unique tuples
set_valid_l_ow_cl = set(ls_valid_l_ow_cl)

survivor_supplier = 'VIVA'

#generate tables

di_cod_vehicle = {}
for v_level in sr_level_vehicles:
    #It chooses as many vehicles as the v_level indicates. This could be improved to be a random selection
    di_cod_vehicle[v_level] = di_df_tables["MaeVehicles"]["COD_VEHICLE"][:v_level]
    export_string = folder_child + "MaeVehicles-tv" + str(v_level) + ".csv"
    df_vehicles = di_df_tables["MaeVehicles"][:v_level]
    df_vehicles.to_csv(export_string, index = False)
  
di_cod_path = {}
for p_level in sr_level_paths:
    di_cod_path[p_level] = di_df_tables["MaePaths"]["COD_PATH"][:p_level]
    export_string = folder_child + "MaePaths-pa" + str(p_level) + ".csv"
    df_paths = di_df_tables["MaePaths"][:p_level]
    df_paths.to_csv(export_string, index = False)
    
    export_string = folder_child + "NodesNodesPaths-pa"+str(p_level) + ".csv"
    df_nodes_nodes_paths = pd.merge(di_df_tables["NodesNodesPaths"], di_cod_path[p_level], how="inner", \
              on = ["COD_PATH"])
    df_nodes_nodes_paths.to_csv(export_string, index=False)
    
    export_string = folder_child + "NodesPaths-pa"+str(p_level) + ".csv"
    df_nodes_paths = pd.merge(di_df_tables["NodesPaths"], di_cod_path[p_level], how="inner", \
              on = ["COD_PATH"])
    df_nodes_paths.to_csv(export_string, index=False)
    
    export_string = folder_child + "MaeNodes-pa"+str(p_level) + ".csv"
    df_mae_nodes = pd.DataFrame(df_nodes_paths["COD_NODE1"].unique(), columns=["COD_NODE"])
    df_mae_nodes.to_csv(export_string, index=False)
    
    export_string = folder_child + "NodesNodes-pa"+str(p_level) + ".csv"
    df_nodes_nodes = pd.merge(di_df_tables["NodesNodes"], df_mae_nodes, \
                              left_on= "COD_NODE2", right_on = "COD_NODE", \
                                  how="inner")[["COD_NODE1","COD_NODE2"]]
    df_nodes_nodes.to_csv(export_string, index=False)
    
    
    df_stations = pd.DataFrame(df_nodes_nodes["COD_NODE1"].unique(), columns=["COD_NODE"])
    df_substations = pd.merge(di_df_tables["SubStations"], df_stations, how = 'inner', on = ['COD_NODE'])
    #df_substations will be updated each iteration, but at the beginning of the iteration, 
    #we need to return to work with the original
    df_substations_aux = df_substations.copy()
    for l_level in sr_level_suppliers:
        if l_level == 3:
            #Create mae_suppliers
            output_export_mae_suppliers = export_mae_suppliers(folder_child, df_substations, di_df_tables["MaeSuppliers"], p_level, l_level)
            df_mae_suppliers = output_export_mae_suppliers[0]
            df_mae_suppliers2 = output_export_mae_suppliers[1]
            #Create suppliers_ranges
            df_suppliers_ranges= export_suppliers_ranges(folder_child,di_df_tables["SuppliersRanges"],df_mae_suppliers, p_level, l_level)
            #Create all variations of SubStations
            export_substations(folder_child, sr_level_own, sr_level_candidate, 
                                df_substations, survivor_supplier, l_level, set_valid_l_ow_cl)
        if l_level ==2:
            #change BP stations to Viva
            df_substations.loc[(df_substations.COD_SUPPLIER == 'BP'), 'COD_SUPPLIER'] = survivor_supplier
            output_export_mae_suppliers = export_mae_suppliers(folder_child, df_substations, di_df_tables["MaeSuppliers"], p_level, l_level)
            df_mae_suppliers = output_export_mae_suppliers[0]
            df_mae_suppliers2 = output_export_mae_suppliers[1]
            #Create suppliers_ranges
            df_suppliers_ranges= export_suppliers_ranges(folder_child,di_df_tables["SuppliersRanges"],df_mae_suppliers, p_level, l_level)
            #Create all variations of SubStations
            export_substations(folder_child, sr_level_own, sr_level_candidate, 
                                df_substations, survivor_supplier, l_level, set_valid_l_ow_cl)
            df_substations = df_substations_aux.copy()
        if l_level ==1:
            df_substations.loc[(df_substations.COD_SUPPLIER == 'BP'), 'COD_SUPPLIER']=survivor_supplier
            df_substations.loc[(df_substations.COD_SUPPLIER == 'OWN'), 'COD_SUPPLIER']=survivor_supplier
            output_export_mae_suppliers = export_mae_suppliers(folder_child, df_substations, di_df_tables["MaeSuppliers"], p_level, l_level)
            df_mae_suppliers = output_export_mae_suppliers[0]
            df_mae_suppliers2 = output_export_mae_suppliers[1]
            #Create suppliers_ranges
            df_suppliers_ranges= export_suppliers_ranges(folder_child,di_df_tables["SuppliersRanges"],df_mae_suppliers, p_level, l_level)
            #Create all variations of SubStations
            export_substations(folder_child, sr_level_own, sr_level_candidate, 
                                df_substations, survivor_supplier, l_level, set_valid_l_ow_cl)
            df_substations = df_substations_aux.copy()
            
         
    #I think this definition of ranges should be inside the loop of suppliers. 
    #Since all suppliers has the same ranges, the definition here should not be a problem
    #I am not going to explore this further.
    #211004
    export_string = folder_child + "MaeRanges-pa"+str(p_level) + ".csv"
    df_ranges = pd.DataFrame(df_suppliers_ranges["COD_RANGE"].unique(), columns=["COD_RANGE"])
    df_ranges.to_csv(export_string, index=False)  

#Check if vehicle path is a feasible combination
di_df_tables["VehiclesPaths"].loc[:, 'isFeasible'] = 1


#Calculate vehicles autonomy
di_consumption_rate = {}
di_vehicle_autonomy = {}
for row in range(di_df_tables["MaeVehicles"].shape[0]):
    v = di_df_tables["MaeVehicles"]["COD_VEHICLE"][row]
    di_consumption_rate[v] = di_df_tables["MaeVehicles"]["pConsumptionRate"][row]
    di_vehicle_autonomy[v] = di_df_tables["MaeVehicles"]["pTankCapacity"][row] / di_df_tables["MaeVehicles"]["pConsumptionRate"][row]

#calculate segment of max length
sr_max_segment_path = di_df_tables["NodesNodesPaths"].groupby('COD_PATH')['pDistance'].max()
di_max_segment_path = sr_max_segment_path.to_dict()

sr_path_length = di_df_tables["NodesNodesPaths"].groupby('COD_PATH')['pDistance'].sum()
di_path_length = sr_path_length.to_dict()

di_consumption_vehicle_path = {}


for row in range(di_df_tables["VehiclesPaths"].shape[0]):
    v = di_df_tables["VehiclesPaths"]["COD_VEHICLE"][row]
    p = di_df_tables["VehiclesPaths"]["COD_PATH"][row]
    di_consumption_vehicle_path[v,p] = di_path_length[p]*di_consumption_rate[v]
    if di_vehicle_autonomy[v] < di_max_segment_path[p]:
        di_df_tables["VehiclesPaths"]['isFeasible'][row] = 0

#export_string = folder_child + "TestVehiclesPath.csv"
#di_df_tables["VehiclesPaths"].to_csv(export_string, index=False)

df_vehicles_paths0 = di_df_tables["VehiclesPaths"][di_df_tables["VehiclesPaths"]['isFeasible']==1]
df_vehicles_paths0 = df_vehicles_paths0[['COD_VEHICLE', 'COD_PATH', 'Start Inventory', 'Target Inventory', 'pQuantityVehicles']]

df_vehicles_paths0.loc[:, 'randomWeight'] = 0.0
for row in range(df_vehicles_paths0.shape[0]):
    df_vehicles_paths0['randomWeight'][row] = random.random()

total_random_weight =  df_vehicles_paths0['randomWeight'].sum()





#export_string = folder_child + "TestVehiclesPath2.csv"
#df_vehicles_paths0.to_csv(export_string, index=False)
di_quantity_vehicles = {}
di_fraction_vehicle_path = {}
di_fuel_fraction_vehicle_path = {}

for v_level in sr_level_vehicles:
    for p_level in sr_level_paths:
        export_string = folder_child + "VehiclesPaths-tv" \
            + str(v_level) + "-pa" + str(p_level) + ".csv"
        df_vehicles_paths = pd.merge(df_vehicles_paths0, di_cod_vehicle[v_level], \
                        how = "inner", on = ["COD_VEHICLE"] )
        df_vehicles_paths2 = pd.merge(df_vehicles_paths, di_cod_path[p_level], how = "inner", \
                        on = ["COD_PATH"])
        #Calculate Quantity of Type of Vehicles in Path 
        total_random_weight =  df_vehicles_paths2['randomWeight'].sum()
        for row in range(df_vehicles_paths2.shape[0]):
            v = df_vehicles_paths2["COD_VEHICLE"][row]
            p = df_vehicles_paths2["COD_PATH"][row]
            di_fraction_vehicle_path[v, p] = df_vehicles_paths2['randomWeight'][row]/total_random_weight
            di_fuel_fraction_vehicle_path[v,p] = di_fraction_vehicle_path[v,p]*total_fuel_consumption
            di_quantity_vehicles[v,p] = round(di_fuel_fraction_vehicle_path[v,p] / di_consumption_vehicle_path[v,p] + 0.5,0)
            if di_quantity_vehicles[v,p]==0:
                di_quantity_vehicles[v,p] = 1
            df_vehicles_paths2['pQuantityVehicles'][row] = di_quantity_vehicles[v,p]
        
        #add quantity vehicles to df_vehicles_paths
        #aux_validation = sum(di_fuel_fraction_vehicle_path[v,p] for (v,p) in di_fuel_fraction_vehicle_path.keys())                            
                
        df_vehicles_paths2.to_csv(export_string, index=False)

ls_start_time.append(('read_scenario', time.time()))

#%%



#%%
#read instance of the RFEP
#Stores the name of each table in each scenario. This data is in the scenario map
di_table_name = {}

for index_scenario in range(df_scenario_map.shape[0]):
#for index_scenario in [0]:
    for t in ls_tables:
        di_table_name[t]=t+"-"+df_scenario_map[t][index_scenario]
    ls_start_time.append(('read_data_scenario', time.time()))
    data_rfep = rd_rfep.read_data_rfep(folder_child, di_table_name, 
                                        is_to_generate_scenarios=True)
    
    ls_start_time.append(('redefine_price_scenario', time.time()))
    #Make the price of own stations high, so the model avoid refuelling there. 
    #So we can calculate an interesting number for minimum refuelling
    factor_price = 50
    sSuppliersOwn = ['OWN']
    sStationsOwn = [i for i in data_rfep["sStations"] for (ii, l) in data_rfep["sStationsSuppliers"] if i==ii if l in sSuppliersOwn]
    pPrice2 = {i: factor_price*data_rfep["pPrice"][i] if i in sStationsOwn else data_rfep["pPrice"][i] for i in data_rfep["sStations"]}
    
    ls_start_time.append(('solve_multiple_FRVP', time.time()))
    
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
        pPrice = pPrice2,
        pOpportunityCost = data_rfep["pOpportunityCost"],
        pVariableCost = data_rfep["pVariableCost"],
        pDistanceOOP = data_rfep["pDistanceOOP"])
    
    ls_start_time.append(('redefine_parameters', time.time()))
    
    #Calculate refuelling quantity per supplier
    
    #What is output_multiple_frvrp?
    #It is a dictionary, each key is a combination v,p
    #Each value is a tuple with all the outputs from solving a version of the rfep, in this case the frvrp
    #the third element (index=2) of the tuple is the refuelling quantity variable
    di_refuel_qty = {(i,v,p): output_multiple_frvrp[(v, p)][2][(i,v,p)] for (i,v,p) in data_rfep["sStationsVehiclesPaths"]}
    
    di_refuel_qty_supplier = {l: sum(di_refuel_qty[i,v,p]*data_rfep["pQuantityVehicles"][v,p]
                                      for (i,v,p) in data_rfep["sStationsVehiclesPaths"]
                                      if (i,l) in data_rfep["sStationsSuppliers"]) 
                              for l in data_rfep["sSuppliers"]}
    
    factor_min_supplier = {"VIVA": 0.2, "BP": 0.2, "OWN": 0}
    factor_lower_discount_range = {'g1': 0, 'g2': 0.200000001}
    factor_upper_discount_range= {'g1': 0.2, 'g2': 50}
    
    di_min_refuel_qty = {l: di_refuel_qty_supplier[l] * factor_min_supplier[l] for l in data_rfep["sSuppliers"]}
    di_lower_qty_discount = {(l,g): di_refuel_qty_supplier[l]*factor_lower_discount_range[g] for (l,g) in data_rfep["sSuppliersRanges"]}
    di_upper_qty_discount = {(l,g): di_refuel_qty_supplier[l]*factor_upper_discount_range[g] for (l,g) in data_rfep["sSuppliersRanges"]}
    
    #I must read mae_suppliers from the scenario
    table_name = "\\" + di_table_name["MaeSuppliers"] + ".csv"
    table_path = folder_child + table_name
    df_mae_suppliers = pd.read_csv(table_path)
    
    df_mae_suppliers.loc[:,'pMinimumPurchaseQuantity'] = 0.0
    
    for row in range(df_mae_suppliers.shape[0]):
        l = df_mae_suppliers['COD_SUPPLIER'][row]
        #iloc is a more efficient method to access data in the dataFrame. 2 is the column pMinimumPurchaseQuantity
        df_mae_suppliers.iloc[row, 2] = di_min_refuel_qty[l]
    
    export_string = folder_child + "MaeSuppliers-" + df_scenario_map['COD_SCENARIO'][index_scenario] + ".csv"
    df_mae_suppliers.to_csv(export_string, index=False)
    
    table_name = "\\" + di_table_name["SuppliersRanges"] + ".csv"
    table_path = folder_child + table_name
    df_suppliers_ranges = pd.read_csv(table_path)
    
    df_suppliers_ranges.loc[:, 'pLowerQuantityDiscount'] = 0.0
    df_suppliers_ranges.loc[:, 'pUpperQuantityDiscount'] = 0.0
    
    for row in range(df_suppliers_ranges.shape[0]):
        l = df_suppliers_ranges['COD_SUPPLIER'][row]
        g = df_suppliers_ranges['COD_RANGE'][row]
        df_suppliers_ranges['pLowerQuantityDiscount'][row] = di_lower_qty_discount[(l,g)]
        df_suppliers_ranges['pUpperQuantityDiscount'][row] = di_upper_qty_discount[(l,g)]
    
    export_string = folder_child + "SuppliersRanges-" + df_scenario_map['COD_SCENARIO'][index_scenario] + ".csv"
    df_suppliers_ranges.to_csv(export_string, index=False)
    
    #update substations
    
    #Calculate the refuelling in each station. Take into account the mirror concept
    di_refuel_qty_station = {i: sum(di_refuel_qty[j,v,p]*data_rfep["pQuantityVehicles"][v,p]
                                      for (j,v,p) in data_rfep["sStationsVehiclesPaths"]
                                      if (i,j) in data_rfep["sOriginalStationsMirrorStations"]) 
                              for i in data_rfep["sOriginalStationsOwn"]}
    
    total_refuel_qty = sum(di_refuel_qty_supplier[l] for l in data_rfep["sSuppliers"])
    
    #Count the existing own stations
    table_name = "\\" + di_table_name["SubStations"] + ".csv"
    table_path = folder_child + table_name
    df_substations = pd.read_csv(table_path)
    
    ls_potential_stations = [i for i in data_rfep["sStations"] for (j, ii, v, p) in data_rfep["sNodesPotentialNodesOriginalVehiclesPaths"] if i==ii]
    n_own_existing_stations = df_scenario_map["Quantity own stations"][index_scenario] - df_scenario_map["Quantity candidate locations"][index_scenario]
    
    proportion_own_station = 0.5
    proportion_station_unit_capacity = 0.1
    factor_cost_unit_capacity = 1.1
    if n_own_existing_stations >0:
        initial_station_capacity = (total_refuel_qty* proportion_own_station)/n_own_existing_stations
    else:
        initial_station_capacity = total_refuel_qty
    
    di_station_capacity = {i: max(initial_station_capacity, di_refuel_qty_station[i]) if i in data_rfep["sOriginalStationsOwn"] else 0
                            for i in df_substations['COD_NODE']}
    di_location_cost = {i: initial_station_capacity * capacity_cost if i in ls_potential_stations  else 0
                            for i in df_substations['COD_NODE']}
    di_station_unit_capacity = {i: di_station_capacity[i]*proportion_station_unit_capacity if i in data_rfep["sOriginalStationsOwn"] else 0
                            for i in df_substations['COD_NODE']}
    di_cost_unit_capacity = {i: di_station_unit_capacity[i]*factor_cost_unit_capacity*capacity_cost if i in data_rfep["sOriginalStationsOwn"] else 0
                            for i in df_substations['COD_NODE']}
    
    for row in range(df_substations.shape[0]):
        i = df_substations['COD_NODE'][row]
        df_substations['pLocationCost'][row] = di_location_cost[i]
        df_substations['pStationCapacity'][row] = di_station_capacity[i]
        df_substations['pStationUnitCapacity'][row] = di_station_unit_capacity[i]
        df_substations['pCostUnitCapacity'][row] = di_cost_unit_capacity[i]
    
    export_string = folder_child + "Substations-" + df_scenario_map['COD_SCENARIO'][index_scenario] + ".csv"
    df_substations.to_csv(export_string, index=False)
    
    ls_start_time.append(("finish_scenario_gen", time.time()))

