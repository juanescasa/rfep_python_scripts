# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 14:10:04 2021

@author: calle

Implementation of the FRVRP. Based on the formulation in Suzuki 2008.
A Generic Model of Motor-Carrier Fuel Optimization
"""
import gurobipy as gp
from gurobipy import GRB

#Define input data
#Sets
#Nodes
sNodes = ['origin', 'st1', 'st2', 'st3', 'destination']

#Stations
sStations = ['st1', 'st2', 'st3']

#Origin
sOrigin = ['origin']

#Destination
sDestination = ['destination']

#This set is required in the initial inventory constraint
sOriginFirstStation = [('origin', 'st1')]

sSequenceNodesNodes = [('st1', 'st2'), ('st2', 'st3')]

sLastStationDestination = [('st3','destination')]

#Parameters
#Price [$/lt]
pPrice = {'st1': 1.5,
          'st2': 1.1,
          'st3': 1.3}

#Minimum Refuelling [lt]
pMinimumRefuelling = 10
#Tank Capacity [lt]
pTankCapacity = 100

#Distance main route [Km]
pDistanceMainRoute = {('origin', 'st1'): 10,
                      ('st1', 'st2'): 30,
                      ('st2', 'st3'): 40,
                      ('st3', 'destination'): 50}

#Distance out of the path [Km]
pDistanceOOP = {'st1': 1,
                'st2': 0.8,
                'st3': 0.2}

#Fuel consumption [liters/km]
pFuelConsumptionRate = 1
pStartInventory = 15
pTargetInventory = 11
pSafetyStock = 2

#Define model
m = gp.Model()
#Define variables

#Refuelling quantity
vRefuelQuantity = m.addVars(sStations, name = 'vRefuelQuantity')
#Refuelling binary
vRefuel = m.addVars(sStations, vtype =GRB.BINARY, name = 'vRefuel')
#Inventory before arriving to node
vInventory = m.addVars(sNodes, name = 'vInventory')

#Define objective function
#Minimize refuelling cost
m.setObjective(gp.quicksum(pPrice[i]*vRefuelQuantity[i] for i in sStations))

#Define constraints
#Minimum Inventory at each point
cMinimumInventory = m.addConstrs((vInventory[i] >= pSafetyStock for i in sStations), name = 'cMinimumInventory')
#Target inventory at destination
cTargetInventory = m.addConstrs((vInventory[i] >= pTargetInventory for i in sDestination), name = 'cTargetInventory')
#Minimum Refuelling Quantity
cMinimumRefuellingQuantity = m.addConstrs((vRefuelQuantity[i] >= pMinimumRefuelling*vRefuel[i] for i in sStations), name = 'cMinimumRefuellingQuantity')
#Logic Refuelling
cLogicRefuelling = m.addConstrs((vRefuelQuantity[i] <= pTankCapacity*vRefuel[i] for i in sStations), name = 'cLogicRefuelling')
#Tank capacity
cTankCapacity = m.addConstrs((vRefuelQuantity[i] + vInventory[i] <= pTankCapacity for i in sStations), name = 'cTankCapacity')
#Inventory balance initial station
cInventoryBalance1 = m.addConstrs((vInventory[j] == pStartInventory - 
                                   (pDistanceMainRoute[i,j] + pDistanceOOP[j]*vRefuel[j])*pFuelConsumptionRate for (i,j) in sOriginFirstStation), name = 'cInventoryBalance1' )
#Inventory balance 
cInventoryBalance2 = m.addConstrs((vInventory[j]== vInventory[i] + vRefuelQuantity[i] - 
                                  (pDistanceMainRoute[i,j] + pDistanceOOP[i]*vRefuel[i]+ pDistanceOOP[j]*vRefuel[j])*pFuelConsumptionRate for (i,j) in sSequenceNodesNodes), name = 'cInventoryBalance2')
#Inventory Balance destination
cInventoryBalance3 = m.addConstrs((vInventory[j]== vInventory[i] + vRefuelQuantity[i] - 
                                  (pDistanceMainRoute[i,j] + pDistanceOOP[i]*vRefuel[i])*pFuelConsumptionRate for (i,j) in sLastStationDestination), name = 'cInventoryBalance3')
#Optimize
m.optimize()

#Recover the variables
ovRefuelQuantity = m.getAttr('x', vRefuelQuantity)
ovInventory  = m.getAttr('x', vInventory)
print("Refuel qty")
print(ovRefuelQuantity)
print("Inventory")
print(ovInventory)

m.write('frvrp_model.lp')