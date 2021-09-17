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
def read_data_rfep(folder_path, dict_tables_name, is_to_generate_scenarios = False):
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
    di_event = {}
    di_event['start_read_df_vehicles']=time.time()
    table_name = "\\" + dict_tables_name["MaeVehicles"] + ".csv"
    table_path = folder_path + table_name
    df_vehicles = pd.read_csv(table_path)
        
    #Read inputs of mathematical model
    ##Define the elements of the mathematical model (sets and parameters)
    di_event['start_assignment_df_vehicles']= time.time()
    sVehicles=[]
    pSafetyStock = {}
    pTankCapacity = {}
    pConsumptionRate = {}
    pMinRefuel = {}
    pVariableCost = {}
    pOpportunityCost = {}
    
    ##Assign the values from dataframes to elements of mathematical model
    for index in range(df_vehicles.shape[0]):
        v = df_vehicles['COD_VEHICLE'][index]
        sVehicles.append(v)
        pSafetyStock[v]=df_vehicles['pSafetyStock'][index]
        pTankCapacity[v]=df_vehicles['pTankCapacity'][index]
        pConsumptionRate[v]=df_vehicles['pConsumptionRate'][index]
        pMinRefuel[v]=df_vehicles['pMinRefuel'][index]
        pVariableCost[v]=df_vehicles['pVariableCost'][index]
        pOpportunityCost[v]=df_vehicles['pOpportunityCost'][index]
    
    di_event['start_read_df_suppliers']= time.time()
    table_name = "\\" + dict_tables_name["MaeSuppliers"] + ".csv"
    table_path = folder_path + table_name
    df_suppliers = pd.read_csv(table_path)
    
    di_event['start_assigment_df_suppliers']= time.time()
    sSuppliers=[]
    sSuppliersWithDiscount = []
    pMinimumPurchaseQuantity = {}
    
    for index in range(df_suppliers.shape[0]):
        l = df_suppliers['COD_SUPPLIER'][index]
        sSuppliers.append(l)
        if df_suppliers['pSuppliersWithDiscount'][index] ==1:
            sSuppliersWithDiscount.append(l)
        if not is_to_generate_scenarios:
            pMinimumPurchaseQuantity[l]=df_suppliers['pMinimumPurchaseQuantity'][index]
    
    di_event['start_read_df_ranges']= time.time()
    table_name = "\\" + dict_tables_name["MaeRanges"] + ".csv"
    table_path = folder_path + table_name
    df_ranges = pd.read_csv(table_path)
    di_event['start_assignment_df_ranges']= time.time()
    sRanges=[]
        
    for index in range(df_ranges.shape[0]):
        l = df_ranges['COD_RANGE'][index]
        sRanges.append(l)
    di_event['start_read_df_NodesNodes']= time.time()
    table_name = "\\" + dict_tables_name["NodesNodes"] + ".csv"
    table_path = folder_path + table_name
    df_nodes_nodes = pd.read_csv(table_path)
    di_event['start_assignment_df_NodesNodes']= time.time()
    sOriginalStationsMirrorStations = []
    
    for index in range(df_nodes_nodes.shape[0]):
        i = df_nodes_nodes['COD_NODE1'][index]
        j = df_nodes_nodes['COD_NODE2'][index]
        sOriginalStationsMirrorStations.append((i,j))
    
    di_event['start_read_df_SubStations']= time.time()
    table_name = "\\" + dict_tables_name["SubStations"] + ".csv"
    table_path = folder_path + table_name
    df_substations = pd.read_csv(table_path)
    di_event['start_assignment_df_SubStations']= time.time()
    sOriginalStationsOwn = []
    sOriginalStationsPotential = []
    sAuxStationsSuppliers = []
    sAuxStations = []
    
    pStationCapacity = {}
    pStationUnitCapacity = {}
    pCostUnitCapacity = {}
    pLocationCost = {}
    pAuxPrice = {}
    
    for index in range(df_substations.shape[0]):
        i = df_substations['COD_NODE'][index]
        l = df_substations['COD_SUPPLIER'][index]
        if df_substations['COD_SUPPLIER'][index] == 'OWN':
            sOriginalStationsOwn.append(i)
            pStationCapacity[i]= df_substations['pStationCapacity'][index]
            pStationUnitCapacity[i] = df_substations['pStationUnitCapacity'][index]
            pCostUnitCapacity[i] = df_substations['pCostUnitCapacity'][index]
            if df_substations['isPotential'][index] == 1:
                sOriginalStationsPotential.append(i)
                pLocationCost[i] = df_substations['pLocationCost'][index]
        
        sAuxStations.append(i)
        sAuxStationsSuppliers.append((i,l))
        pAuxPrice[i]=df_substations['pPriceOriginal'][index]
    
    di_event['start_read_df_VehiclesPaths']= time.time()
    table_name = "\\" + dict_tables_name["VehiclesPaths"] + ".csv"
    table_path = folder_path + table_name
    df_vehicles_paths = pd.read_csv(table_path)
    di_event['start_assignment_df_VehiclesPaths']= time.time()
    sVehiclesPaths = []
    
    pAuxStartInventory = {}
    pTargetInventory = {}
    pAuxQuantityVehicles = {}
    
    for index in range(df_vehicles_paths.shape[0]):
        v = df_vehicles_paths['COD_VEHICLE'][index]
        p = df_vehicles_paths['COD_PATH'][index]
        sVehiclesPaths.append((v,p))
        pAuxStartInventory[v,p] = df_vehicles_paths['Start Inventory'][index]
        pTargetInventory[v,p] = df_vehicles_paths['Target Inventory'][index]
        pAuxQuantityVehicles[v,p] = df_vehicles_paths['pQuantityVehicles'][index]
        
    di_event['start_read_df_NodesPaths']= time.time()
    table_name = "\\" + dict_tables_name["NodesPaths"] + ".csv"
    table_path = folder_path + table_name
    df_nodes_paths = pd.read_csv(table_path)
    di_event['start_assignment_df_NodesPaths']= time.time()
    sAuxNodesPaths = []
    sAuxOriginPaths = []
    sAuxDestinationPaths = []
    sAuxFirstStationPaths = []
    
    pDistanceOOP = {}
    
    for index in range(df_nodes_paths.shape[0]):
        i = df_nodes_paths['COD_NODE1'][index]
        p = df_nodes_paths['COD_PATH'][index]
        sAuxNodesPaths.append((i,p))
        if df_nodes_paths['pOriginPath'][index]==1:
            sAuxOriginPaths.append((i,p))
        if df_nodes_paths['pDestinationPath'][index]==1:
            sAuxDestinationPaths.append((i,p))
        if df_nodes_paths['pFirstStation'][index]==1:
            sAuxFirstStationPaths.append((i,p))
        if df_nodes_paths['pOriginPath'][index]==0 and df_nodes_paths['pDestinationPath'][index]==0:
            pDistanceOOP[i,p]=df_nodes_paths['pDistanceOOP'][index]
    
    di_event['start_read_df_SuppliersRange']= time.time()
    table_name = "\\" + dict_tables_name["SuppliersRanges"] + ".csv"
    table_path = folder_path + table_name
    df_suppliers_ranges = pd.read_csv(table_path)
    di_event['start_assignment_df_SuppliersRange']= time.time()
    sSuppliersRanges = []
    
    pLowerQuantityDiscount = {}
    pUpperQuantityDiscount = {}
    pDiscount = {}
    
    for index in range(df_suppliers_ranges.shape[0]):
        l = df_suppliers_ranges['COD_SUPPLIER'][index]
        g = df_suppliers_ranges['COD_RANGE'][index]
        sSuppliersRanges.append((l,g))
        if not is_to_generate_scenarios:
            pLowerQuantityDiscount[l,g] = df_suppliers_ranges['pLowerQuantityDiscount'][index]
            pUpperQuantityDiscount[l,g] = df_suppliers_ranges['pUpperQuantityDiscount'][index]
        pDiscount[l,g] = df_suppliers_ranges['pDiscount'][index]
    
    di_event['start_read_df_NodesNodesPaths']= time.time()
    table_name = "\\" + dict_tables_name["NodesNodesPaths"] + ".csv"
    table_path = folder_path + table_name
    df_nodes_nodes_paths = pd.read_csv(table_path)
    di_event['start_assignment_df_NodesNodesPaths']= time.time()
    sAuxNodesNodesPaths = []
    pDistance = {}
    
    for index in range(df_nodes_nodes_paths.shape[0]):
        i = df_nodes_nodes_paths['COD_NODE1'][index]
        j = df_nodes_nodes_paths['COD_NODE2'][index]
        p = df_nodes_nodes_paths['COD_PATH'][index]
        sAuxNodesNodesPaths.append((i,j,p))
        pDistance[i,j,p] = df_nodes_nodes_paths['pDistance'][index]
    
    
    
    #%%
    #calculated sets
    di_event['start_calculate_sStations']= time.time()
    sStations = [i for (ii,i) in sOriginalStationsMirrorStations]
    di_event['start_calculate_sStationsPaths']= time.time()
    sStationsPaths = [(i,p) for (i,p) in sAuxNodesPaths if i in sStations]
    di_event['start_calculate_sNodesVehiclesPaths']= time.time()
    sNodesVehiclesPaths = [(i,v,p) for (i,p) in sAuxNodesPaths for (v,pp) in sVehiclesPaths  if p == pp]
    di_event['start_calculate_sStationsVehiclesPaths']= time.time()
    sStationsVehiclesPaths = [(i,v,p) for (i,p) in sAuxNodesPaths for (v,pp) in sVehiclesPaths  if p == pp if i in sStations]
    di_event['start_calculate_sDestinationVehiclesPaths']= time.time()
    sDestinationVehiclesPaths = [(i,v,p) for (i,p) in sAuxDestinationPaths for(v,pp) in sVehiclesPaths  if p == pp]
    di_event['start_calculate_sOriginVehiclesPaths']= time.time()
    sOriginVehiclesPaths = [(i,v,p) for (i,p) in sAuxOriginPaths for(v,pp) in sVehiclesPaths  if p == pp]
    di_event['start_calculate_sFirstStationVehiclesPaths']= time.time()
    sFirstStationVehiclesPaths = [(i,v,p) for (i,p) in sAuxFirstStationPaths for(v,pp) in sVehiclesPaths  if p == pp]
    di_event['start_calculate_sAuxNotFirstStationVehiclesPaths']= time.time()
    sAuxNotFirstStationVehiclesPaths = ((set(sNodesVehiclesPaths)-set(sFirstStationVehiclesPaths))-set(sOriginVehiclesPaths))-set(sDestinationVehiclesPaths)
    di_event['start_calculate_sNotFirstStationVehiclesPaths']= time.time()
    sNotFirstStationVehiclesPaths =  list(sAuxNotFirstStationVehiclesPaths)
    di_event['start_calculate_sNodesPotentialNodesOriginalVehiclesPaths']= time.time()
    sNodesPotentialNodesOriginalVehiclesPaths = [(j,i,v,p) for (i,j) in sOriginalStationsMirrorStations for (jj,v,p) in sNodesVehiclesPaths if j==jj if i in sOriginalStationsPotential]
    di_event['start_calculate_sSequenceNodesNodesVehiclesPaths']= time.time()
    sSequenceNodesNodesVehiclesPaths = [(i,j,v,p) for (i,j,p) in sAuxNodesNodesPaths for (v,pp) in sVehiclesPaths if p == pp]
    di_event['start_calculate_sStationsSuppliers']= time.time()
    sStationsSuppliers = [(j,l) for (i,j) in sOriginalStationsMirrorStations for (ii,l) in sAuxStationsSuppliers if i == ii]
    #%%
    #Auxiliar parameters
    pFlowFactor = 1
    pPercentageStartInventory = 1
    di_event['start_calculate_pPrice']= time.time()
    #calculated parameters
    #This is called dictionary comprehension: https://www.netguru.com/codestories/python-list-comprehension-dictionary
    pPrice={i: pAuxPrice[ii] for (ii,i) in sOriginalStationsMirrorStations}
    di_event['start_calculate_pConsumptionOOP']= time.time()
    pConsumptionOOP = {(i,v,p): pDistanceOOP[i,p]*pConsumptionRate[v] for (i,p) in sStationsPaths for (v,pp) in sVehiclesPaths if p == pp}
    di_event['start_calculate_pConsumptionMainRoute']= time.time()
    pConsumptionMainRoute = {(i,j,v,p): pDistance[i,j,p] * pConsumptionRate[v] for (i,j,v,p) in sSequenceNodesNodesVehiclesPaths}
    di_event['start_calculate_pQuantityVehicles']= time.time()
    pQuantityVehicles = {(v,p): pFlowFactor*pAuxQuantityVehicles[v,p] for (v,p) in sVehiclesPaths}
    di_event['start_calculate_pStartInventory']= time.time()
    pStartInventory =  {(v,p): pPercentageStartInventory*pAuxStartInventory[v,p] for (v,p) in sVehiclesPaths}
    di_event['end_process']= time.time()
   
    
    #Define the dictionary to define the processes. This defintion is made in excel to make it easier
    di_process_events = {"read_df_vehicles": ("start_read_df_vehicles", "start_assignment_df_vehicles"),
        "assignment_df_vehicles": ("start_assignment_df_vehicles", "start_read_df_suppliers"),
        "read_df_suppliers": ("start_read_df_suppliers", "start_assigment_df_suppliers"),
        "assigment_df_suppliers": ("start_assigment_df_suppliers", "start_read_df_ranges"),
        "read_df_ranges": ("start_read_df_ranges", "start_assignment_df_ranges"),
        "assignment_df_ranges": ("start_assignment_df_ranges", "start_read_df_NodesNodes"),
        "read_df_NodesNodes": ("start_read_df_NodesNodes", "start_assignment_df_NodesNodes"),
        "assignment_df_NodesNodes": ("start_assignment_df_NodesNodes", "start_read_df_SubStations"),
        "read_df_SubStations": ("start_read_df_SubStations", "start_assignment_df_SubStations"),
        "assignment_df_SubStations": ("start_assignment_df_SubStations", "start_read_df_VehiclesPaths"),
        "read_df_VehiclesPaths": ("start_read_df_VehiclesPaths", "start_assignment_df_VehiclesPaths"),
        "assignment_df_VehiclesPaths": ("start_assignment_df_VehiclesPaths", "start_read_df_NodesPaths"),
        "read_df_NodesPaths": ("start_read_df_NodesPaths", "start_assignment_df_NodesPaths"),
        "assignment_df_NodesPaths": ("start_assignment_df_NodesPaths", "start_read_df_SuppliersRange"),
        "read_df_SuppliersRange": ("start_read_df_SuppliersRange", "start_assignment_df_SuppliersRange"),
        "assignment_df_SuppliersRange": ("start_assignment_df_SuppliersRange", "start_read_df_NodesNodesPaths"),
        "read_df_NodesNodesPaths": ("start_read_df_NodesNodesPaths", "start_assignment_df_NodesNodesPaths"),
        "assignment_df_NodesNodesPaths": ("start_assignment_df_NodesNodesPaths", "start_calculate_sStations"),
        "calculate_sStations": ("start_calculate_sStations", "start_calculate_sStationsPaths"),
        "calculate_sStationsPaths": ("start_calculate_sStationsPaths", "start_calculate_sNodesVehiclesPaths"),
        "calculate_sNodesVehiclesPaths": ("start_calculate_sNodesVehiclesPaths", "start_calculate_sStationsVehiclesPaths"),
        "calculate_sStationsVehiclesPaths": ("start_calculate_sStationsVehiclesPaths", "start_calculate_sDestinationVehiclesPaths"),
        "calculate_sDestinationVehiclesPaths": ("start_calculate_sDestinationVehiclesPaths", "start_calculate_sOriginVehiclesPaths"),
        "calculate_sOriginVehiclesPaths": ("start_calculate_sOriginVehiclesPaths", "start_calculate_sFirstStationVehiclesPaths"),
        "calculate_sFirstStationVehiclesPaths": ("start_calculate_sFirstStationVehiclesPaths", "start_calculate_sAuxNotFirstStationVehiclesPaths"),
        "calculate_sAuxNotFirstStationVehiclesPaths": ("start_calculate_sAuxNotFirstStationVehiclesPaths", "start_calculate_sNotFirstStationVehiclesPaths"),
        "calculate_sNotFirstStationVehiclesPaths": ("start_calculate_sNotFirstStationVehiclesPaths", "start_calculate_sNodesPotentialNodesOriginalVehiclesPaths"),
        "calculate_sNodesPotentialNodesOriginalVehiclesPaths": ("start_calculate_sNodesPotentialNodesOriginalVehiclesPaths", "start_calculate_sSequenceNodesNodesVehiclesPaths"),
        "calculate_sSequenceNodesNodesVehiclesPaths": ("start_calculate_sSequenceNodesNodesVehiclesPaths", "start_calculate_sStationsSuppliers"),
        "calculate_sStationsSuppliers": ("start_calculate_sStationsSuppliers", "start_calculate_pPrice"),
        "calculate_pPrice": ("start_calculate_pPrice", "start_calculate_pConsumptionOOP"),
        "calculate_pConsumptionOOP": ("start_calculate_pConsumptionOOP", "start_calculate_pConsumptionMainRoute"),
        "calculate_pConsumptionMainRoute": ("start_calculate_pConsumptionMainRoute", "start_calculate_pQuantityVehicles"),
        "calculate_pQuantityVehicles": ("start_calculate_pQuantityVehicles", "start_calculate_pStartInventory"),
        "calculate_pStartInventory": ("start_calculate_pStartInventory", "end_process")}
    #Define the dictionary to store the time
    di_process_duration = {process: di_event[di_process_events[process][1]] - \
                       di_event[di_process_events[process][0]] \
                       for process in di_process_events}
    
    #previous_start = 0
    # for event in l_time_track:
    #     if previous_start == 0:
    #         di_time_event[event[0]] = 0
    #     else:
    #         di_time_event[event[0]] = event[1] - previous_start
    #     previous_start = event[1]
    output_dict = {"sVehicles": sVehicles,
                    "pSafetyStock": pSafetyStock,
                    "pTankCapacity": pTankCapacity,
                    "pConsumptionRate": pConsumptionRate,
                    "pMinRefuel": pMinRefuel,
                    "pVariableCost": pVariableCost,
                    "pOpportunityCost": pOpportunityCost,
                    "sSuppliers": sSuppliers,
                    "sSuppliersWithDiscount": sSuppliersWithDiscount,
                    "pMinimumPurchaseQuantity": pMinimumPurchaseQuantity,
                    "sRanges": sRanges,
                    "sOriginalStationsMirrorStations": sOriginalStationsMirrorStations,
                    "sOriginalStationsOwn": sOriginalStationsOwn,
                    "sOriginalStationsPotential": sOriginalStationsPotential,
                    "pStationCapacity": pStationCapacity,
                    "pStationUnitCapacity": pStationUnitCapacity,
                    "pCostUnitCapacity": pCostUnitCapacity,
                    "pLocationCost": pLocationCost,
                    "sVehiclesPaths": sVehiclesPaths,
                    "pTargetInventory": pTargetInventory,
                    "pDistanceOOP": pDistanceOOP,
                    "sSuppliersRanges": sSuppliersRanges,
                    "pLowerQuantityDiscount": pLowerQuantityDiscount,
                    "pUpperQuantityDiscount": pUpperQuantityDiscount,
                    "pDiscount": pDiscount,
                    "pDistance": pDistance,
                    "sStations": sStations,
                    "sStationsPaths": sStationsPaths,
                    "sNodesVehiclesPaths": sNodesVehiclesPaths,
                    "sStationsVehiclesPaths": sStationsVehiclesPaths,
                    "sDestinationVehiclesPaths": sDestinationVehiclesPaths,
                    "sOriginVehiclesPaths": sOriginVehiclesPaths,
                    "sFirstStationVehiclesPaths": sFirstStationVehiclesPaths,
                    "sNotFirstStationVehiclesPaths": sNotFirstStationVehiclesPaths,
                    "sNodesPotentialNodesOriginalVehiclesPaths": sNodesPotentialNodesOriginalVehiclesPaths,
                    "sSequenceNodesNodesVehiclesPaths": sSequenceNodesNodesVehiclesPaths,
                    "sStationsSuppliers": sStationsSuppliers,
                    "pPrice": pPrice,
                    "pConsumptionOOP": pConsumptionOOP,
                    "pConsumptionMainRoute": pConsumptionMainRoute,
                    "pQuantityVehicles": pQuantityVehicles,
                    "pStartInventory": pStartInventory,
                    "di_event": di_event,
                    "di_process_duration": di_process_duration}
    
    return(output_dict)

