# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 11:26:24 2021

@author: calle
"""
import pandas as pd
import read_data_rfep_function as rd_rfep
import solve_multiple_frvrp

#This silence a warning from pandas when assigning elements of DataFrames. 
#The best option to assign is using iloc, but this makes the code less readable, 
#since we must use the index of rows and columns
pd.options.mode.chained_assignment = None



#Read generator tables
folder = "C:\OneDrive - Deakin University\OD\calle test\Disun Applications\Gurobi Applications\data\Toy instance"


ls_tables = ['MaeNodes', 'MaeVehicles', 'MaeSuppliers', 'MaeRanges', 'MaePaths', 
             'NodesNodes', 'SubStations', 'VehiclesPaths', 'NodesPaths', 
             'SuppliersRanges', 'NodesNodesPaths']

di_df_tables = {}
for t in ls_tables:
    table_name = t
    table_path = folder + '\\' + table_name + ".csv"
    di_df_tables[t]=pd.read_csv(table_path)

#read scenario map
file = "C:\OneDrive - Deakin University\OD\calle test\Disun Applications\Gurobi Applications\data\Toy instance\Scenario Map Toy 1.xlsx"
sh = 'Generate Tables'
df_scenario_map = pd.read_excel(file, sheet_name = sh)

#read levels of factors
sr_level_vehicles = df_scenario_map['Type of vehicles'].unique()
sr_level_paths = df_scenario_map['Quantity of paths'].unique()

#generate tables
folder = folder + "\\Generated tables\\"
di_cod_vehicle = {}
for v_level in sr_level_vehicles:
    #It chooses as many vehicles as the v_level indicates. This could be improved to be a random selection
    di_cod_vehicle[v_level] = di_df_tables["MaeVehicles"]["COD_VEHICLE"][:v_level]
    export_string = folder + "MaeVehicles-tv" + str(v_level) + ".csv"
    df_vehicles = di_df_tables["MaeVehicles"][:v_level]
    df_vehicles.to_csv(export_string, index = False)
  
di_cod_path = {}
for p_level in sr_level_paths:
    di_cod_path[p_level] = di_df_tables["MaePaths"]["COD_PATH"][:p_level]
    export_string = folder + "MaePaths-pa" + str(p_level) + ".csv"
    df_paths = di_df_tables["MaePaths"][:p_level]
    df_paths.to_csv(export_string, index = False)
    
    export_string = folder + "NodesNodesPaths-pa"+str(p_level) + ".csv"
    df_nodes_nodes_paths = pd.merge(di_df_tables["NodesNodesPaths"], di_cod_path[p_level], how="inner", \
             on = ["COD_PATH"])
    df_nodes_nodes_paths.to_csv(export_string, index=False)
        
    export_string = folder + "NodesPaths-pa"+str(p_level) + ".csv"
    df_nodes_paths = pd.merge(di_df_tables["NodesPaths"], di_cod_path[p_level], how="inner", \
             on = ["COD_PATH"])
    df_nodes_paths.to_csv(export_string, index=False)
    
    export_string = folder + "MaeNodes-pa"+str(p_level) + ".csv"
    df_mae_nodes = pd.DataFrame(df_nodes_paths["COD_NODE1"].unique(), columns=["COD_NODE"])
    df_mae_nodes.to_csv(export_string, index=False)
    
    export_string = folder + "NodesNodes-pa"+str(p_level) + ".csv"
    df_nodes_nodes = pd.merge(di_df_tables["NodesNodes"], df_mae_nodes, \
                              left_on= "COD_NODE2", right_on = "COD_NODE", \
                                  how="inner")[["COD_NODE1","COD_NODE2"]]
    df_nodes_nodes.to_csv(export_string, index=False)
    
    export_string = folder + "SubStations-pa"+str(p_level) + ".csv"
    df_stations = pd.DataFrame(df_nodes_nodes["COD_NODE1"].unique(), columns=["COD_NODE"])
    df_substations = pd.merge(di_df_tables["SubStations"], df_stations, how = 'inner', on = ['COD_NODE'])
    df_substations.to_csv(export_string, index=False)
    
    export_string = folder + "MaeSuppliers-pa"+str(p_level) + ".csv"
    df_mae_suppliers = pd.DataFrame(df_substations["COD_SUPPLIER"].unique(), columns=["COD_SUPPLIER"])
    df_mae_suppliers2 = pd.merge(di_df_tables["MaeSuppliers"], df_mae_suppliers, how = 'inner', on = ['COD_SUPPLIER'])
    df_mae_suppliers2.to_csv(export_string, index=False)
    
    export_string = folder + "SuppliersRanges-pa"+str(p_level) + ".csv"
    df_suppliers_ranges = pd.merge(di_df_tables["SuppliersRanges"], df_mae_suppliers, \
                                   how = 'inner', on = ['COD_SUPPLIER'])
    df_suppliers_ranges.to_csv(export_string, index=False)
    
    export_string = folder + "MaeRanges-pa"+str(p_level) + ".csv"
    df_ranges = pd.DataFrame(df_suppliers_ranges["COD_RANGE"].unique(), columns=["COD_RANGE"])
    df_ranges.to_csv(export_string, index=False)  
    
for v_level in sr_level_vehicles:
    for p_level in sr_level_paths:
        export_string = folder + "VehiclesPaths-tv" \
            + str(v_level) + "-pa" + str(p_level) + ".csv"
        df_1 = pd.merge(di_df_tables["VehiclesPaths"], di_cod_vehicle[v_level], \
                        how = "inner", on = ["COD_VEHICLE"] )
        df_2 = pd.merge(df_1, di_cod_path[p_level], how = "inner", \
                        on = ["COD_PATH"])
        df_2.to_csv(export_string, index=False)

#read instance of the RFEP
#Stores the name of each table in each scenario. This data is in the scenario map
di_table_name = {}

for index_scenario in range(df_scenario_map.shape[0]):
    for t in ls_tables:
        di_table_name[t]=t+"-"+df_scenario_map[t][index_scenario]
    
    data_rfep = rd_rfep.read_data_rfep(folder, di_table_name, 
                                       is_to_generate_scenarios=True)
    
    
    #Make the price of own stations high, so the model avoid refuelling there. 
    #So we can calculate an interesting number for minimum refuelling
    factor_price = 50
    sSuppliersOwn = ['OWN']
    sStationsOwn = [i for i in data_rfep["sStations"] for (ii, l) in data_rfep["sStationsSuppliers"] if i==ii if l in sSuppliersOwn]
    pPrice2 = {i: factor_price*data_rfep["pPrice"][i] if i in sStationsOwn else data_rfep["pPrice"][i] for i in data_rfep["sStations"]}
    
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
    
    factor_min_supplier = 0.2
    factor_lower_discount_range = {'g1': 0, 'g2': 0.200000001}
    factor_upper_discount_range= {'g1': 0.2, 'g2': 50}
    
    di_min_refuel_qty = {l: di_refuel_qty_supplier[l] * factor_min_supplier for l in data_rfep["sSuppliers"]}
    di_lower_qty_discount = {(l,g): di_refuel_qty_supplier[l]*factor_lower_discount_range[g] for (l,g) in data_rfep["sSuppliersRanges"]}
    di_upper_qty_discount = {(l,g): di_refuel_qty_supplier[l]*factor_upper_discount_range[g] for (l,g) in data_rfep["sSuppliersRanges"]}
    
    df_mae_suppliers3 = df_mae_suppliers2
    df_mae_suppliers3.loc[:,'pMinimumPurchaseQuantity'] = 0.0
    
    for row in range(df_mae_suppliers3.shape[0]):
        l = df_mae_suppliers3['COD_SUPPLIER'][row]
        #iloc is a more efficient method to access data in the dataFrame. 2 is the column pMinimumPurchaseQuantity
        df_mae_suppliers3.iloc[row, 2] = di_min_refuel_qty[l]
    
    export_string = folder + "MaeSuppliers-" + df_scenario_map['COD_SCENARIO'][index_scenario] + ".csv"
    df_mae_suppliers3.to_csv(export_string, index=False)
    
    df_suppliers_ranges2 = df_suppliers_ranges
    df_suppliers_ranges2.loc[:, 'pLowerQuantityDiscount'] = 0.0
    df_suppliers_ranges2.loc[:, 'pUpperQuantityDiscount'] = 0.0
    
    for row in range(df_suppliers_ranges2.shape[0]):
        l = df_suppliers_ranges2['COD_SUPPLIER'][row]
        g = df_suppliers_ranges2['COD_RANGE'][row]
        df_suppliers_ranges2['pLowerQuantityDiscount'][row] = di_lower_qty_discount[(l,g)]
        df_suppliers_ranges2['pUpperQuantityDiscount'][row] = di_upper_qty_discount[(l,g)]
    
    export_string = folder + "SuppliersRanges-" + df_scenario_map['COD_SCENARIO'][index_scenario] + ".csv"
    df_suppliers_ranges2.to_csv(export_string, index=False)

    
