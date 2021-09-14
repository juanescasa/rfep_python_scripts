# -*- coding: utf-8 -*-
"""
Created on Wed May 26 20:23:22 2021

@author: calle
"""
import pandas as pd
import time

l_time_track=[('start_reading', time.time()) ]
#Read tables as dataframes
#file = os.path.join("..", "data", "Data Model Generated Network-13.xlsm")
file = "C:\OneDrive - Deakin University\OD\calle test\Disun Applications\Gurobi Applications\data\Data Model Generated Network-12.xlsm"
sh = 'MaeVehicles'
df_vehicles = pd.read_excel(file, sheet_name = sh)

#Read inputs of mathematical model
##Define the elements of the mathematical model (sets and parameters)

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

sh = 'MaeSuppliers'
df_suppliers = pd.read_excel(file, sheet_name = sh)

sSuppliers=[]
sSuppliersWithDiscount = []
pMinimumPurchaseQuantity = {}

for index in range(df_suppliers.shape[0]):
    l = df_suppliers['COD_SUPPLIER'][index]
    sSuppliers.append(l)
    if df_suppliers['pSuppliersWithDiscount'][index] ==1:
        sSuppliersWithDiscount.append(l)
    pMinimumPurchaseQuantity[l]=df_suppliers['pMinimumPurchaseQuantity'][index]

sh = 'MaeRanges'
df_ranges = pd.read_excel(file, sheet_name = sh)

sRanges=[]


for index in range(df_ranges.shape[0]):
    l = df_ranges['COD_RANGE'][index]
    sRanges.append(l)


sh = 'NodesNodes'
df_nodes_nodes = pd.read_excel(file, sheet_name = sh)


sOriginalStationsMirrorStations = []

for index in range(df_nodes_nodes.shape[0]):
    i = df_nodes_nodes['COD_NODE1'][index]
    j = df_nodes_nodes['COD_NODE2'][index]
    sOriginalStationsMirrorStations.append((i,j))


sh = 'SubStations'
df_substations = pd.read_excel(file, sheet_name = sh)

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

sh = 'VehiclesPaths'
df_vehicles_paths = pd.read_excel(file, sheet_name = sh)
 
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
    

sh = 'NodesPaths'
df_nodes_paths = pd.read_excel(file, sheet_name = sh)

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

sh = 'SuppliersRanges'
df_suppliers_ranges = pd.read_excel(file, sheet_name = sh)

sSuppliersRanges = []

pLowerQuantityDiscount = {}
pUpperQuantityDiscount = {}
pDiscount = {}

for index in range(df_suppliers_ranges.shape[0]):
    l = df_suppliers_ranges['COD_SUPPLIER'][index]
    g = df_suppliers_ranges['COD_RANGE'][index]
    sSuppliersRanges.append((l,g))
    pLowerQuantityDiscount[l,g] = df_suppliers_ranges['pLowerQuantityDiscount'][index]
    pUpperQuantityDiscount[l,g] = df_suppliers_ranges['pUpperQuantityDiscount'][index]
    pDiscount[l,g] = df_suppliers_ranges['pDiscount'][index]

sh = 'NodesNodesPaths'
df_nodes_nodes_paths = pd.read_excel(file, sheet_name = sh)

sAuxNodesNodesPaths = []
pDistance = {}

for index in range(df_nodes_nodes_paths.shape[0]):
    i = df_nodes_nodes_paths['COD_NODE1'][index]
    j = df_nodes_nodes_paths['COD_NODE2'][index]
    p = df_nodes_nodes_paths['COD_PATH'][index]
    sAuxNodesNodesPaths.append((i,j,p))
    pDistance[i,j,p] = df_nodes_nodes_paths['pDistance'][index]

l_time_track.append(('start_calculate_parameters', time.time()))

#%%
#calculated sets
sStations = [i for (ii,i) in sOriginalStationsMirrorStations]
sStationsPaths = [(i,p) for (i,p) in sAuxNodesPaths if i in sStations]
sNodesVehiclesPaths = [(i,v,p) for (i,p) in sAuxNodesPaths for (v,pp) in sVehiclesPaths  if p == pp]
sStationsVehiclesPaths = [(i,v,p) for (i,p) in sAuxNodesPaths for (v,pp) in sVehiclesPaths  if p == pp if i in sStations]
sDestinationVehiclesPaths = [(i,v,p) for (i,p) in sAuxDestinationPaths for(v,pp) in sVehiclesPaths  if p == pp]
sOriginVehiclesPaths = [(i,v,p) for (i,p) in sAuxOriginPaths for(v,pp) in sVehiclesPaths  if p == pp]
sFirstStationVehiclesPaths = [(i,v,p) for (i,p) in sAuxFirstStationPaths for(v,pp) in sVehiclesPaths  if p == pp]
sAuxNotFirstStationVehiclesPaths = ((set(sNodesVehiclesPaths)-set(sFirstStationVehiclesPaths))-set(sOriginVehiclesPaths))-set(sDestinationVehiclesPaths)
sNotFirstStationVehiclesPaths =  list(sAuxNotFirstStationVehiclesPaths) 
sNodesPotentialNodesOriginalVehiclesPaths = [(j,i,v,p) for (i,j) in sOriginalStationsMirrorStations for (jj,v,p) in sNodesVehiclesPaths if j==jj if i in sOriginalStationsPotential]
sSequenceNodesNodesVehiclesPaths = [(i,j,v,p) for (i,j,p) in sAuxNodesNodesPaths for (v,pp) in sVehiclesPaths if p == pp]
sStationsSuppliers = [(j,l) for (i,j) in sOriginalStationsMirrorStations for (ii,l) in sAuxStationsSuppliers if i == ii]
#%%
#Auxiliar parameters
pFlowFactor = 1
pPercentageStartInventory = 1

#calculated parameters
#This is called dictionary comprehension: https://www.netguru.com/codestories/python-list-comprehension-dictionary
pPrice={i: pAuxPrice[ii] for (ii,i) in sOriginalStationsMirrorStations}
pConsumptionOOP = {(i,v,p): pDistanceOOP[i,p]*pConsumptionRate[v] for (i,p) in sStationsPaths for (v,pp) in sVehiclesPaths if p == pp}
pConsumptionMainRoute = {(i,j,v,p): pDistance[i,j,p] * pConsumptionRate[v] for (i,j,v,p) in sSequenceNodesNodesVehiclesPaths}
pQuantityVehicles = {(v,p): pFlowFactor*pAuxQuantityVehicles[v,p] for (v,p) in sVehiclesPaths}
pStartInventory =  {(v,p): pPercentageStartInventory*pAuxStartInventory[v,p] for (v,p) in sVehiclesPaths}


