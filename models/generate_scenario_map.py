# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 15:52:04 2021

@author: calle
"""
import pandas as pd
import random as random

ls_sheets = ["Type of vehicles",
            "Quantity of paths",
            "Quantity own stations",
            "Quantity candidate locations",
            "Quantity suppliers"]
#file =  "C:\OneDrive - Deakin University\OD\calle test\Disun Applications\Gurobi Applications\data\Toy instance\Factors to generate scenarios.xlsx"

folder_path = "C:\OneDrive - Deakin University\OD\calle test\Disun Applications\Gurobi Applications\data\\"
folder_name = "Path 2000\\"
name_file1 = "Factors to generate scenarios.xlsx"
name_file2 = "Scenario Map.xlsx"
file_to_import = folder_path + folder_name + name_file1
file_to_export = folder_path + folder_name + name_file2
combination_percentage = 0.5



di_df_factor_levels = {}

for e in ls_sheets:
    sh = e
    di_df_factor_levels[e]=pd.read_excel(file_to_import, sheet_name=sh)

ls_col_cod_scenario = []
ls_col_type_vehicles = []
ls_col_quantity_paths = []
ls_col_quantity_own_stations = []
ls_col_quantity_candidate_locations = []
ls_col_quantity_suppliers = []
ls_col_MaeNodes= []
ls_col_MaeSuppliers= []
ls_col_MaeVehicles= []
ls_col_MaeRanges= []
ls_col_MaePaths= []
ls_col_SubStations= []
ls_col_NodesPaths= []
ls_col_VehiclesPaths= []
ls_col_SuppliersRanges= []
ls_col_NodesNodes= []
ls_col_NodesNodesPaths= []

ls_col_MaeSuppliers2= []
ls_col_SuppliersRanges2 = []
ls_col_SubStations2 = []

for v in di_df_factor_levels['Type of vehicles']['Type of vehicles']:
    for p in di_df_factor_levels['Quantity of paths']['Quantity of paths']:
        for ow in di_df_factor_levels['Quantity own stations']['Quantity own stations']:
            for cl in di_df_factor_levels['Quantity candidate locations']['Quantity candidate locations']:
                for l in di_df_factor_levels['Quantity suppliers']['Quantity suppliers']:
                    rnd_num = random.random()
                    if rnd_num < combination_percentage:
                        
                        if (l == 1 and (ow + cl)==0) or (l>1 and ow > 0 and cl>0 and cl<=ow):
                            str_all_factors ="tv"+str(v)+"-pa"+str(p)+"-ow"+str(ow)+"-cl"+str(cl)+"-su"+str(l)
                            ls_col_cod_scenario.append(str_all_factors)
                            ls_col_type_vehicles.append(v)
                            ls_col_quantity_paths.append(p)
                            ls_col_quantity_own_stations.append(ow)
                            ls_col_quantity_candidate_locations.append(cl)
                            ls_col_quantity_suppliers.append(l)
                            ls_col_MaeNodes.append("pa"+str(p))
                            ls_col_MaeSuppliers.append("pa"+str(p)+"-su"+str(l))
                            ls_col_MaeVehicles.append("tv"+str(v))
                            ls_col_MaeRanges.append("pa"+str(p))
                            ls_col_MaePaths.append("pa"+str(p))
                            ls_col_SubStations.append("pa"+str(p)+"-ow"+str(ow)+"-cl"+str(cl)+"-su"+str(l))
                            ls_col_NodesPaths.append("pa"+str(p))
                            ls_col_VehiclesPaths.append("tv"+str(v)+"-pa"+str(p))
                            ls_col_SuppliersRanges.append("pa"+str(p)+"-su"+str(l))
                            ls_col_NodesNodes.append("pa"+str(p))
                            ls_col_NodesNodesPaths.append("pa"+str(p))
                            
                            ls_col_MaeSuppliers2.append(str_all_factors)
                            ls_col_SuppliersRanges2.append(str_all_factors)
                            ls_col_SubStations2.append(str_all_factors)

df_scenario_map1=pd.DataFrame({"COD_SCENARIO" : ls_col_cod_scenario,
                                "Type of vehicles" : ls_col_type_vehicles,
                                "Quantity of paths" : ls_col_quantity_paths,
                                "Quantity own stations" : ls_col_quantity_own_stations,
                                "Quantity candidate locations" : ls_col_quantity_candidate_locations,
                                "Quantity suppliers" : ls_col_quantity_suppliers,
                                "MaeNodes" : ls_col_MaeNodes,
                                "MaeSuppliers" : ls_col_MaeSuppliers,
                                "MaeVehicles" : ls_col_MaeVehicles,
                                "MaeRanges" : ls_col_MaeRanges,
                                "MaePaths" : ls_col_MaePaths,
                                "SubStations" : ls_col_SubStations,
                                "NodesPaths" : ls_col_NodesPaths,
                                "VehiclesPaths" : ls_col_VehiclesPaths,
                                "SuppliersRanges" : ls_col_SuppliersRanges,
                                "NodesNodes" : ls_col_NodesNodes,
                                "NodesNodesPaths" : ls_col_NodesNodesPaths})

df_scenario_map2=pd.DataFrame({"COD_SCENARIO" : ls_col_cod_scenario,
                                "Type of vehicles" : ls_col_type_vehicles,
                                "Quantity of paths" : ls_col_quantity_paths,
                                "Quantity own stations" : ls_col_quantity_own_stations,
                                "Quantity candidate locations" : ls_col_quantity_candidate_locations,
                                "Quantity suppliers" : ls_col_quantity_suppliers,
                                "MaeNodes" : ls_col_MaeNodes,
                                "MaeSuppliers" : ls_col_MaeSuppliers2,
                                "MaeVehicles" : ls_col_MaeVehicles,
                                "MaeRanges" : ls_col_MaeRanges,
                                "MaePaths" : ls_col_MaePaths,
                                "SubStations" : ls_col_SubStations2,
                                "NodesPaths" : ls_col_NodesPaths,
                                "VehiclesPaths" : ls_col_VehiclesPaths,
                                "SuppliersRanges" : ls_col_SuppliersRanges2,
                                "NodesNodes" : ls_col_NodesNodes,
                                "NodesNodesPaths" : ls_col_NodesNodesPaths})



with pd.ExcelWriter(file_to_export) as writer:  
    df_scenario_map1.to_excel(writer, sheet_name='Generate Tables', index=False)
    df_scenario_map2.to_excel(writer, sheet_name='Run Experiments', index=False)