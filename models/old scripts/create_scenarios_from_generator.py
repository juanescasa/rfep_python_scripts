# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 11:26:24 2021

@author: calle
"""
import pandas as pd

#Read generator tables
folder = "C:\OneDrive - Deakin University\OD\calle test\Disun Applications\Gurobi Applications\data\Toy instance"
#ls_tables = ['\\MaeVehicles.csv', '\\MaeSuppliers.csv', '\\MaeRanges.csv', '\\NodesNodes.csv',
#             '\\SubStations.csv', '\\VehiclesPaths.csv', '\\NodesPaths.csv', '\\SuppliersRanges.csv', 
#             '\\NodesNodesPaths.csv']

ls_tables = ['MaeNodes', 'MaeVehicles', 'MaeSuppliers', 'MaeRanges', 'MaePaths', 
             'NodesNodes', 'SubStations', 'VehiclesPaths', 'NodesPaths', 
             'SuppliersRanges', 'NodesNodesPaths']

df_table = {}
for t in ls_tables:
    table_name = t
    table_path = folder + '\\' + table_name + ".csv"
    df_table[t]=pd.read_csv(table_path)

#read scenario map
file = "C:\OneDrive - Deakin University\OD\calle test\Disun Applications\Gurobi Applications\data\Scenario Map Toy 1.xlsx"
sh = 'Sheet1'
df_scenario_map = pd.read_excel(file, sheet_name = sh)

#read levels of factors
sr_level_vehicles = df_scenario_map['Type of vehicles'].unique()
sr_level_paths = df_scenario_map['Quantity of paths'].unique()

folder = folder + "\\Generated tables\\"
di_cod_vehicle = {}
for v_level in sr_level_vehicles:
    di_cod_vehicle[v_level] = df_table["MaeVehicles"]["COD_VEHICLE"][:v_level]
    export_string = folder + "MaeVehicles-tv" + str(v_level) + ".csv"
    df_table["MaeVehicles"][:v_level].to_csv(export_string, index = False)
    
    
di_cod_path = {}
for p_level in sr_level_paths:
    di_cod_path[p_level] = df_table["MaePaths"]["COD_PATH"][:p_level]
    export_string = folder + "MaePaths-pa" + str(p_level) + ".csv"
    df_table["MaePaths"][:p_level].to_csv(export_string, index = False)
    
    export_string = folder + "NodesNodesPaths-pa"+str(p_level) + ".csv"
    pd.merge(df_table["NodesNodesPaths"], di_cod_path[p_level], how="inner", \
             on = ["COD_PATH"]).to_csv(export_string, index=False)
        
    export_string = folder + "NodesPaths-pa"+str(p_level) + ".csv"
    df_nodes_paths = pd.merge(df_table["NodesPaths"], di_cod_path[p_level], how="inner", \
             on = ["COD_PATH"])
    df_nodes_paths.to_csv(export_string, index=False)
    
    export_string = folder + "MaeNodes-pa"+str(p_level) + ".csv"
    df_mae_nodes = pd.DataFrame(df_nodes_paths["COD_NODE1"].unique(), columns=["COD_NODE"])
    df_mae_nodes.to_csv(export_string, index=False)
    
    export_string = folder + "NodesNodes-pa"+str(p_level) + ".csv"
    df_nodes_nodes = pd.merge(df_table["NodesNodes"], df_mae_nodes, \
                              left_on= "COD_NODE2", right_on = "COD_NODE", \
                                  how="inner")[["COD_NODE1","COD_NODE2"]]
    df_nodes_nodes.to_csv(export_string, index=False)
    
    export_string = folder + "SubStations-pa"+str(p_level) + ".csv"
    df_stations = pd.DataFrame(df_nodes_nodes["COD_NODE1"].unique(), columns=["COD_NODE"])
    df_substations = pd.merge(df_table["SubStations"], df_stations, how = 'inner', on = ['COD_NODE'])
    df_substations.to_csv(export_string, index=False)
    
    export_string = folder + "MaeSuppliers-pa"+str(p_level) + ".csv"
    df_mae_suppliers = pd.DataFrame(df_substations["COD_SUPPLIER"].unique(), columns=["COD_SUPPLIER"])
    df_mae_suppliers2 = pd.merge(df_table["MaeSuppliers"], df_mae_suppliers, how = 'inner', on = ['COD_SUPPLIER'])
    
    df_mae_suppliers2.to_csv(export_string, index=False)
    

for v_level in sr_level_vehicles:
    for p_level in sr_level_paths:
        export_string = folder + "VehiclesPaths-tv" \
            + str(v_level) + "-pa" + str(p_level) + ".csv" 
        df_1 = pd.merge(df_table["VehiclesPaths"], di_cod_vehicle[v_level], \
                        how = "inner", on = ["COD_VEHICLE"] )
        df_2 = pd.merge(df_1, di_cod_path[p_level], how = "inner", \
                        on = ["COD_PATH"])
        df_2.to_csv(export_string, index=False)
        
        

"""
set_level_vehicles = set()
set_level_paths = set()


for row in range(df_scenario_map.shape[0]):
    set_level_vehicles.append(df_scenario_map['Type of vehicles'][row])
    set_level_paths.append(df_scenario_map['Quantity of paths'][row])
"""


    
    

