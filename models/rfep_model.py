# -*- coding: utf-8 -*-
"""
Created on Wed May 26 12:08:30 2021

@author: calle
"""
import gurobipy as gp
from gurobipy import GRB
import sys
import time

def callback_initial_gap(model, where):
        if where == GRB.Callback.MIPSOL:
            model._n_incumbents = model._n_incumbents+1
            if model._n_incumbents == 1:
                model._time_first_incumbent = time.time() - model._time_start
                best_bound = model.cbGet(GRB.Callback.MIPSOL_OBJBND)
                current_obj_value = model.cbGet(GRB.Callback.MIPSOL_OBJ)
                model._initial_gap = abs(best_bound - current_obj_value) / abs(current_obj_value)
                #debug callback
                #model._best_bound = best_bound
                #model._current_objective_value = current_obj_value

def solve_rfep(sNodesVehiclesPaths,
                sStationsVehiclesPaths,
                sOriginalStationsOwn,
                sOriginalStationsPotential,
                sSuppliers,
                sSuppliersRanges,
                sOriginVehiclesPaths,
                sDestinationVehiclesPaths,
                sSequenceNodesNodesVehiclesPaths,
                sFirstStationVehiclesPaths,
                sNotFirstStationVehiclesPaths,
                sNodesPotentialNodesOriginalVehiclesPaths,
                sOriginalStationsMirrorStations,
                sStationsSuppliers,
                sSuppliersWithDiscount,
                sRanges,
                pStartInventory = 0,
                pTargetInventory = 0,
                pSafetyStock = 0,
                pTankCapacity = 0,
                pMinRefuel = 0,
                pConsumptionMainRoute = 0,
                pConsumptionOOP = 0,
                pQuantityVehicles = 0,
                pStationCapacity = 0,
                pStationUnitCapacity = 0,
                pMinimumPurchaseQuantity = 0,
                pLowerQuantityDiscount = 0,
                pUpperQuantityDiscount = 0,
                pPrice = 0,
                pOpportunityCost = 0,
                pVariableCost = 0,
                pDistanceOOP = 0,
                pCostUnitCapacity = 0,
                pDiscount = 0,
                pLocationCost = 0,
                isONvInventory = False,
                isONvRefuelQuantity = False,
                isONvRefuel = False,
                isONvQuantityUnitsCapacity = False,
                isONvLocate = False,
                isONvQuantityPurchased = False,
                isONvQuantityPurchasedRange = False,
                isONvPurchasedRange = False,
                isONcInitialInventory = False,
                isONcTargetInventory = False,
                isONcMinInventory = False,
                isONcLogicRefuel1 = False,
                isONcLogicRefuel2 = False,
                isONcMaxRefuel = False,
                isONcInventoryBalance1 = False,
                isONcInventoryBalance2 = False,
                isONcInventoryBalance3 = False,
                isONcLogicLocation = False,
                isONcLogicLocation2 = False,
                isONcStationCapacity = False,
                isONcQuantityPurchased = False,
                isONcMinimumQuantitySupplier = False,
                isONcMinQuantityRange = False,
                isONcMaxQuantityRange = False,
                isONcUniqueQuantityRange = False,
                isONcUniqueRange = False,
                isONcNoPurchaseOwn = False,
                isONtotalRefuellingCost= False,
                isONtotalLocationCost= False,
                isONtotalDiscount= False,
                timeLimit = 86400,
                retrieveSolutionDetail = True,
                mip_start = {},
                ):
    """
    Parameters
    ----------
    retrieveSolutionDetail : when it is False it reduces the output from the funciton.
    
    timeLimit : limit gurobi run in seconds

    
    -----
    
    """

    m = gp.Model()
    m.Params.timeLimit = timeLimit
    #Define variables
    if isONvInventory:
        vInventory = m.addVars(sNodesVehiclesPaths, name = 'vInventory')
    if isONvRefuelQuantity:
        vRefuelQuantity = m.addVars(sStationsVehiclesPaths, name = 'vRefuelQuantity')
    if isONvRefuel:
        vRefuel = m.addVars(sStationsVehiclesPaths, vtype = GRB.BINARY, name = 'vRefuel')
    if isONvQuantityUnitsCapacity:
        vQuantityUnitsCapacity = m.addVars(sOriginalStationsOwn, vtype = GRB.INTEGER, name = 'vQuantityUnitsCapacity')
    if isONvLocate:
        vLocate = m.addVars(sOriginalStationsPotential, vtype = GRB.BINARY, name = 'vLocate')
    if isONvQuantityPurchased:
        vQuantityPurchased = m.addVars(sSuppliers, name = 'vQuantityPurchased')
    if isONvQuantityPurchasedRange:
        vQuantityPurchasedRange = m.addVars(sSuppliersRanges, name = 'vQuantityPurchasedRange')
    if isONvPurchasedRange:
        vPurchasedRange = m.addVars(sSuppliersRanges, vtype = GRB.BINARY, name='vPurchasedRange')
    
    #Define Constraints
    #Refuelling Logic Constraints
    if isONcInitialInventory:
        cInitialInventory = m.addConstrs((vInventory[i,v,p]==pStartInventory[v,p] 
                                      for (i,v,p) in sOriginVehiclesPaths), name = 'initialInventory')
    if isONcTargetInventory:
        cTargetInventory = m.addConstrs((vInventory[i,v,p]==pTargetInventory[v,p] 
                                      for (i,v,p) in sDestinationVehiclesPaths), name = 'targetInventory')
    if isONcMinInventory:
        cMinInventory = m.addConstrs((vInventory[i,v,p]>=pSafetyStock[v] 
                                   for (i,v,p) in sStationsVehiclesPaths), name ='minInventory')
    if isONcLogicRefuel1:
        cLogicRefuel1 = m.addConstrs((vRefuelQuantity[i,v,p]<=(pTankCapacity[v])*vRefuel[i,v,p] 
                                   for (i,v,p) in sStationsVehiclesPaths), name = 'logicRefuel1')
    if isONcLogicRefuel2:
        cLogicRefuel2 = m.addConstrs((vRefuelQuantity[i,v,p]>=pMinRefuel[v]*vRefuel[i,v,p]
                                   for (i,v,p) in sStationsVehiclesPaths), name = 'logicRefuel2')
    if isONcMaxRefuel:
        cMaxRefuel = m.addConstrs((vInventory[i,v,p] + vRefuelQuantity[i,v,p] <= pTankCapacity[v] 
                                for (i,v,p) in sStationsVehiclesPaths), name = 'maxRefuel')
    if isONcInventoryBalance1:
        cInventoryBalance1 = m.addConstrs((vInventory[j,v,p] == pStartInventory[v,p] - (pConsumptionMainRoute[i,j,v,p] + pConsumptionOOP[j,v,p]*vRefuel[j,v,p]) 
                                        for (i,j,v,p) in sSequenceNodesNodesVehiclesPaths if (j,v,p) in sFirstStationVehiclesPaths), name = 'inventoryBalance1')
    if isONcInventoryBalance2:
        cInventoryBalance2 = m.addConstrs((vInventory[j,v,p] == vInventory[i,v,p] + vRefuelQuantity[i,v,p] - 
                   (pConsumptionOOP[i,v,p]*vRefuel[i,v,p] + pConsumptionMainRoute[i,j,v,p] + pConsumptionOOP[j,v,p]*vRefuel[j,v,p]) 
                   for (i,j,v,p) in sSequenceNodesNodesVehiclesPaths if (j,v,p) in sNotFirstStationVehiclesPaths), name = 'inventoryBalance2')
    if isONcInventoryBalance3:
        cInventoryBalance3 = m.addConstrs((vInventory[j,v,p]==vInventory[i,v,p]+vRefuelQuantity[i,v,p] - (pConsumptionMainRoute[i,j,v,p] + pConsumptionOOP[i,v,p]*vRefuel[i,v,p]) 
                                       for (i,j,v,p) in sSequenceNodesNodesVehiclesPaths if (j,v,p) in sDestinationVehiclesPaths), name = 'inventoryBalance3')
    # #Location Logic Constraints
    if isONcLogicLocation:
        cLogicLocation = m.addConstrs((vRefuel[j,v,p] <= vLocate[i] for (j,i,v,p) in sNodesPotentialNodesOriginalVehiclesPaths), name = 'logicLocation')
    # #Valid Inequality
    if isONcLogicLocation2:
        cLogicLocation2 = m.addConstrs((vRefuelQuantity[j,v,p] <= (pTankCapacity[v]-pSafetyStock[v])*vLocate[i] for (j,i,v,p) in sNodesPotentialNodesOriginalVehiclesPaths), name = 'logicLocation2')
    if isONcStationCapacity:
        cStationCapacity = m.addConstrs(((gp.quicksum(pQuantityVehicles[v,p] * vRefuelQuantity[j,v,p] for (j,v,p) in sStationsVehiclesPaths if (i,j) in sOriginalStationsMirrorStations))
                                      <=pStationCapacity[i] + pStationUnitCapacity[i]*vQuantityUnitsCapacity[i]  for i in sOriginalStationsOwn), name = 'stationCapacity')
    #Supplier Logic constraints
    if isONcQuantityPurchased:
        cQuantityPurchased = m.addConstrs((vQuantityPurchased[l] == gp.quicksum(pQuantityVehicles[v,p]*vRefuelQuantity[i,v,p] for (i,v,p) in sStationsVehiclesPaths if (i,l) in sStationsSuppliers) for l in sSuppliers), name = 'quantityPurchased')
    if isONcMinimumQuantitySupplier:
        cMinimumQuantitySupplier = m.addConstrs((vQuantityPurchased[l]>=pMinimumPurchaseQuantity[l] for l in sSuppliers), name = 'minimumQuantitySupplier')
    if isONcMinQuantityRange:
        cMinQuantityRange = m.addConstrs((vQuantityPurchasedRange[l,g]>= vPurchasedRange[l,g]*pLowerQuantityDiscount[l,g] for (l,g) in sSuppliersRanges), name = 'minQuantityRange')
    if isONcMaxQuantityRange:
        cMaxQuantityRange = m.addConstrs((vQuantityPurchasedRange[l,g]<= vPurchasedRange[l,g]*pUpperQuantityDiscount[l,g] for (l,g) in sSuppliersRanges), name = 'maxQuantityRange')
    if isONcUniqueQuantityRange:
        cUniqueQuantityRange = m.addConstrs((gp.quicksum(vQuantityPurchasedRange[l,g] for g in sRanges if (l,g) in sSuppliersRanges) == vQuantityPurchased[l] for l in sSuppliersWithDiscount), name = 'uniqueQuantityRange')
    if isONcUniqueRange:
        cUniqueRange = m.addConstrs((gp.quicksum(vPurchasedRange[l,g] for g in sRanges if (l, g) in sSuppliersRanges) == 1 for l in sSuppliersWithDiscount), name = 'uniqueRange')
    #Building scenarios constraints
    if isONcNoPurchaseOwn:
        sSuppliersOwn = ['OWN']
        cNoPurchaseOwn = m.addConstrs((0 == gp.quicksum(pQuantityVehicles[v,p]*vRefuelQuantity[i,v,p] for (i,v,p) in sStationsVehiclesPaths if (i,l) in sStationsSuppliers) for l in sSuppliersOwn), name = 'cNoPurchaseOwn')
    
    
    #Objective Function
    if isONtotalRefuellingCost:
        totalRefuellingCost = gp.quicksum(pQuantityVehicles[v,p]*(vRefuelQuantity[i,v,p]*pPrice[i] + (pOpportunityCost[v] + 2*pVariableCost[v]*pDistanceOOP[i,p])*vRefuel[i,v,p])  
                                       for (i,v,p) in sStationsVehiclesPaths)
    else:
        totalRefuellingCost = 0
    
    if isONtotalLocationCost:
        totalLocationCost = gp.quicksum(pLocationCost[i]*vLocate[i] for i in sOriginalStationsPotential) + gp.quicksum(pCostUnitCapacity[i]*vQuantityUnitsCapacity[i] for i in sOriginalStationsOwn)
    else:
        totalLocationCost = 0
    
    if isONtotalDiscount:
        totalDiscount = gp.quicksum(pDiscount[l,g]*vQuantityPurchasedRange[l,g] for (l,g) in sSuppliersRanges)
    else:
        totalDiscount=0
    m.setObjective(totalRefuellingCost + totalLocationCost - totalDiscount, GRB.MINIMIZE )
    #m.setObjective(0, GRB.MINIMIZE )
    #This allows to get a definitive conclusion between unbounded or infeasible model.
    m.Params.DualReductions = 0
    #l_time_track.append(('start_optimization', time.time()))
    m._n_incumbents = 0
    m._initial_gap = 10
    m._time_first_incumbent = 0
    m._time_start = time.time()
    
    #provide mip start value
    if len(mip_start)>0:
        #this procedure iterates over the dynamic list defined by the tuples of the dictionaries of the variables
        #This is required because the mip start may not include all the decision variables of the original problem.
        #For intance, the mip start could come from a domain reduction procedure. 
        for (i,v,p) in mip_start["vRefuel"].keys():
            vRefuel[i,v,p].Start=mip_start["vRefuel"][i,v,p]
            vRefuelQuantity[i,v,p].Start=mip_start["vRefuelQuantity"][i,v,p]
        for (i,v,p) in mip_start["vInventory"].keys():
            vInventory[i,v,p].Start = mip_start["vInventory"][i,v,p]
        for i in mip_start["vQuantityUnitsCapacity"].keys():
            vQuantityUnitsCapacity[i].Start = mip_start["vQuantityUnitsCapacity"][i]
            if i in mip_start["vLocate"].keys():
                vLocate[i].Start = mip_start["vLocate"][i]
        for l in sSuppliers:
            vQuantityPurchased[l].Start = mip_start["vQuantityPurchased"][l]
        for (l,g) in sSuppliersRanges:
            vPurchasedRange[l,g].Start = mip_start["vPurchasedRange"][l,g]       
    
    #this is executed when I want to tune the model. It is still not working.
    # m.tune()
    # for i in range(m.tuneResultCount):
    #     m.write('tune'+str(i)+'.prm')
    
    m.optimize(callback_initial_gap)
    #l_time_track.append(('start_export_output', time.time()))
    #Dealing with infeasability
    status = m.status
    if status == GRB.INFEASIBLE:
        print("The model is infeasible")
        m.computeIIS()
        for c in m.getConstrs():
            if c.IISConstr:
                print('%s' % c.constrName)
        #this stop the execution of this file.
        sys.exit()
    
    if m._n_incumbents > 0:
        
        if isONvInventory:
            ovInventory = m.getAttr('x', vInventory)            
        else:
            ovInventory = {}            
            
        if isONvRefuelQuantity:
            ovRefuelQuantity = m.getAttr('x', vRefuelQuantity)
            osvRefuelQuantity = {(i,v,p): ovRefuelQuantity[i,v,p] for (i,v,p) in sStationsVehiclesPaths if ovRefuelQuantity[i,v,p]>0.01}
        else:
            ovRefuelQuantity = {}    
        #it is greater of 0.1 to avoid precision errors.    
        if isONvRefuel:
            ovRefuel = m.getAttr('x', vRefuel)
            osvRefuel = {(i,v,p): ovRefuel[i,v,p] for (i,v,p) in sStationsVehiclesPaths if ovRefuel[i,v,p]>0.01}
        else:
            ovRefuel = {}
            osvRefuel = {}
            
        if isONvQuantityUnitsCapacity:
            ovQuantityUnitsCapacity = m.getAttr('x', vQuantityUnitsCapacity)
        else:
            ovQuantityUnitsCapacity = {}           
        
        if isONvLocate:
            ovLocate = m.getAttr('x', vLocate)            
        else:
            ovLocate = {}
        
        if isONvQuantityPurchasedRange:
            ovQuantityPurchased = m.getAttr('x', vQuantityPurchased)
            #I do not need to summarize this. This dictionary should be always >0            
        else:
            ovQuantityPurchased = {}
        
        if isONvQuantityPurchasedRange:
            ovQuantityPurchasedRange = m.getAttr('x', vQuantityPurchasedRange)            
        else:
            ovQuantityPurchasedRange = {}          
            
        if isONvPurchasedRange:
            ovPurchasedRange = m.getAttr('x', vPurchasedRange)
        else:
            ovPurchasedRange = 0
        
        if isONtotalRefuellingCost:
            oTotalRefuellingCost = sum(pQuantityVehicles[v,p]*(ovRefuelQuantity[i,v,p]*pPrice[i] + (pOpportunityCost[v] + 2*pVariableCost[v]*pDistanceOOP[i,p])*ovRefuel[i,v,p])  
                                           for (i,v,p) in sStationsVehiclesPaths)
        else:
            oTotalRefuellingCost = 0
        
        if isONtotalLocationCost:
            oTotalLocationCost = sum(pLocationCost[i]*ovLocate[i] for i in sOriginalStationsPotential) + sum(pCostUnitCapacity[i]*ovQuantityUnitsCapacity[i] for i in sOriginalStationsOwn)
        else:
            oTotalLocationCost = 0
        
        if isONtotalDiscount:
            oTotalDiscount = sum(pDiscount[l,g]*ovQuantityPurchasedRange[l,g] for (l,g) in sSuppliersRanges)
        else:
            oTotalDiscount = 0
            
        oTotalCost = oTotalRefuellingCost + oTotalLocationCost - oTotalDiscount
        
        #Calculate scenario size features
        n_vehicles = len({v for (i,v,p) in sOriginVehiclesPaths})
        n_paths = len({p for (i,v,p) in sOriginVehiclesPaths})
        n_vehicles_paths = len(sOriginVehiclesPaths)
        n_stations_vehicles_paths = len(sStationsVehiclesPaths)
        n_avg_stations_path = n_stations_vehicles_paths/n_vehicles_paths
        n_candidate_locations = len(sOriginalStationsPotential)
        #Calculate scenario stats
        n_constraints = m.NumConstrs
        n_variables = m.Numvars
        n_integer_variables = m.NumIntVars
        n_binary_variables = m.NumBinVars
        model_fingerprint = hex(m.Fingerprint & 0xFFFFFFFF)
        model_runtime = m.Runtime
        model_MIPGap = m.Mipgap
        model_nodeCount = m.nodeCount
        model_initial_gap = m._initial_gap
        model_time_first_incumbent = m._time_first_incumbent  
        
        #This block reduce the size of the output to only decision variables
        if not retrieveSolutionDetail:
            ovInventory = {}
            ovRefuelQuantity = {}
            ovRefuel = {}           
            
            
        return(status,
                ovInventory,
                ovRefuelQuantity,
                ovRefuel,
                ovQuantityUnitsCapacity,
                ovLocate,
                ovQuantityPurchased,
                ovQuantityPurchasedRange,
                ovPurchasedRange,
                oTotalRefuellingCost,
                oTotalLocationCost,
                oTotalDiscount,
                oTotalCost,
                n_constraints,
                n_variables,
                n_integer_variables,
                n_binary_variables,
                model_fingerprint,
                model_runtime,
                model_MIPGap,
                model_nodeCount,
                model_initial_gap,
                model_time_first_incumbent,
                osvRefuelQuantity,
                osvRefuel,
                n_vehicles,
                n_paths,
                n_avg_stations_path,
                n_candidate_locations)   
    else:
        return(0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0)