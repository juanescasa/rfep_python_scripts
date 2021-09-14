# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 17:42:53 2021

@author: calle
"""
#import pandas as pd
import gurobipy as gp
from gurobipy import GRB
import rfep_model

#Activate when debugging
#import openpyxl
#import sys
#import jecs_functions
#import os
#import time

def reduce_stations_path(
        factor_options = 1,
        factor_price = 2,
        slack_reduction = 2,
        sVehiclesPaths = [],
        sNodesVehiclesPaths = [],
        sStationsVehiclesPaths = [],
        sOriginalStationsOwn = [],
        sOriginalStationsPotential = [],
        sSuppliers = [],
        sSuppliersRanges = [],
        sOriginVehiclesPaths = [],
        sDestinationVehiclesPaths = [],
        sSequenceNodesNodesVehiclesPaths = [],
        sFirstStationVehiclesPaths = [],
        sNotFirstStationVehiclesPaths = [],
        sNodesPotentialNodesOriginalVehiclesPaths = [],
        sOriginalStationsMirrorStations = [],
        sStationsSuppliers = [],
        sSuppliersWithDiscount = [],
        sRanges = [],
        pStartInventory = 0,
        pTargetInventory = 0,
        pSafetyStock = 0,
        pTankCapacity = 0,
        pMinRefuel = 0,
        pConsumptionRate = 0,
        pDistance = 0,
        pConsumptionMainRoute = 0,
        pConsumptionOOP = 0,
        pQuantityVehicles = 0,
        pPrice = 0,
        pOpportunityCost = 0,
        pVariableCost = 0,
        pDistanceOOP = 0):
    """
    Parameters
    ----------
    factor_options : number that multiplies the refuelling times to define how many stations will be left after reduction
    factor_price : number that multiplies the price to avoid choosing a station in a following run of the FRVRP
    slack_reduction : has to be >= 2. number that defines if it is worthy to solve 
                the subproblem many times to reduce the quantity of stations left 
                in the path. if n_stations_sub <= n_refuelling_times*factor_options+slack_reduction 
                do not reduce the stations of the associated path
    Yield
    -----
    
    """
    #this dict stores all the tuples that output the solve of the subproblem
    d_subproblem_solution = {}
    #d_subproblem_status = {}
    #d_subproblem_ovInventory = {}
    #d_subproblem_ovRefuelQuantity = {}
    d_subproblem_ovRefuel = {}
    #d_subproblem_oTotalRefuellingCost = {}
    #d_subproblem_oTotalCost = {}
    
    #solution statistics
    # d_subproblem_n_constraints = {}
    # d_subproblem_n_variables = {}
    # d_subproblem_n_integer_variables = {}
    # d_subproblem_n_binary_variables = {}
    # d_subproblem_model_fingerprint = {}
    # d_subproblem_model_runtime = {}
    # d_subproblem_model_MIPGap = {}
    
    
    #Domain reduction parameters
    #Define an auxiliary dictionary for price (domain reduction procedure)
       #if the algorithm would only reduce the slack_reduction the quantity of station,
    #it is not worthy to reduce the number of stations, otherwise it is worthy
    sSubStationsVehiclesPaths2 = []
    sAuxSubStationsVehiclesPaths2 = []
    
    #It is the parameter where the new distance will be stored, the sequence of nodes changes
    #because of the domain reduction.
    pSubDistance = {}
    sSequenceNodesNodesVehiclesPaths2 = []
    sFirstStationVehiclesPaths2 = []
    sNotFirstStationVehiclesPaths2 = []
        
    
    for e in sVehiclesPaths:
        sSubVehiclesPaths = e
        #update lists according to subproblem -> filter per vehicle path
        sSubNodesVehiclesPaths = [(i,v,p) for (i,v,p) in sNodesVehiclesPaths if v == e[0] and p==e[1]]
        sSubStationsVehiclesPaths = [(i,v,p) for (i,v,p) in sStationsVehiclesPaths if v == e[0] and p==e[1]]
        sSubOriginVehiclesPaths = [(i,v,p) for (i,v,p) in sOriginVehiclesPaths if v == e[0] and p==e[1]]
        sSubDestinationVehiclesPaths = [(i,v,p) for (i,v,p) in sDestinationVehiclesPaths if v == e[0] and p==e[1]]
        sSubSequenceNodesNodesVehiclesPaths = [(i,j,v,p) for (i,j,v,p) in sSequenceNodesNodesVehiclesPaths if v == e[0] and p==e[1]]
        sSubFirstStationVehiclesPaths = [(i,v,p) for (i,v,p) in sFirstStationVehiclesPaths  if v == e[0] and p==e[1]]
        sSubNotFirstStationVehiclesPaths = [(i,v,p) for (i,v,p) in sNotFirstStationVehiclesPaths  if v == e[0] and p==e[1]]
        sSubNodesPotentialNodesOriginalVehiclesPaths = [(i,j,v,p) for (i,j,v,p) in sNodesPotentialNodesOriginalVehiclesPaths  if v == e[0] and p==e[1]]
        #In each change of subproblem I need to come back to the full dictionary of prices.
        pPrice2 = pPrice
        #for each subproblem (v,p) choose a number of stations that will be optional to refuel
        #counts the stations that are promising options to refuel
        n_stations_chosen = 0
        #define the options for the specific (v,p) according to the refuelling times of the first run. 10 is just a dummy value
        n_refuelling_options = 10
        n_iterations_sub = 0
        #s_sSubStationsVehiclesPaths2 = set()
        
          
        while n_stations_chosen < n_refuelling_options:
        #while n_iterations_sub < 1:
            n_iterations_sub+=1
            #solve subproblem
            d_subproblem_solution[e] = rfep_model.solve_rfep(
                                    sNodesVehiclesPaths = sSubNodesVehiclesPaths,
                                    sStationsVehiclesPaths = sSubStationsVehiclesPaths,
                                    sOriginalStationsOwn = sOriginalStationsOwn,
                                    sOriginalStationsPotential = sOriginalStationsPotential,
                                    sSuppliers = sSuppliers,
                                    sSuppliersRanges = sSuppliersRanges,
                                    sOriginVehiclesPaths = sSubOriginVehiclesPaths,
                                    sDestinationVehiclesPaths = sSubDestinationVehiclesPaths,
                                    sSequenceNodesNodesVehiclesPaths = sSubSequenceNodesNodesVehiclesPaths,
                                    sFirstStationVehiclesPaths = sSubFirstStationVehiclesPaths,
                                    sNotFirstStationVehiclesPaths = sSubNotFirstStationVehiclesPaths,
                                    sNodesPotentialNodesOriginalVehiclesPaths = sSubNodesPotentialNodesOriginalVehiclesPaths,
                                    sOriginalStationsMirrorStations = sOriginalStationsMirrorStations,
                                    sStationsSuppliers = sStationsSuppliers,
                                    sSuppliersWithDiscount = sSuppliersWithDiscount,
                                    sRanges = sRanges,
                                    pStartInventory = pStartInventory,
                                    pTargetInventory = pTargetInventory,
                                    pSafetyStock = pSafetyStock,
                                    pTankCapacity = pTankCapacity,
                                    pMinRefuel = pMinRefuel,
                                    pConsumptionMainRoute = pConsumptionMainRoute,
                                    pConsumptionOOP = pConsumptionOOP,
                                    pQuantityVehicles = pQuantityVehicles,
                                    pPrice = pPrice2,
                                    pOpportunityCost = pOpportunityCost,
                                    pVariableCost = pVariableCost,
                                    pDistanceOOP = pDistanceOOP,
                                    isONvInventory = True,
                                    isONvRefuelQuantity = True,
                                    isONvRefuel = True,
                                    isONcInitialInventory = True,
                                    isONcTargetInventory = True,
                                    isONcMinInventory = True,
                                    isONcLogicRefuel1 = True,
                                    isONcLogicRefuel2 = True,
                                    isONcMaxRefuel = True,
                                    isONcInventoryBalance1 = True,
                                    isONcInventoryBalance2 = True,
                                    isONcInventoryBalance3 = True,
                                    isONtotalRefuellingCost= True)                      
            
            #create specific variables for each output of the function
            #d_subproblem_status[e] = d_subproblem_solution[e][0]
            #d_subproblem_ovInventory[e] = d_subproblem_solution[e][1]
            #d_subproblem_ovRefuelQuantity[e] = d_subproblem_solution[e][2]
            d_subproblem_ovRefuel[e] = d_subproblem_solution[e][3]
            #d_subproblem_oTotalRefuellingCost[e] = d_subproblem_solution[e][9]
            #d_subproblem_oTotalCost[e] = d_subproblem_solution[e][12]
            
            #Debug subproblem
            # output_file = os.path.join("..", "output", "outputRFEPSubproblem_v1.xlsx")
            # scenario_name = "Revision 2LKM-40L,295"
            # sStationsPaths2 = {(i,p) for (i,v,p) in sSubStationsVehiclesPaths}
            # export_solution_rfep.export_solution_rfep(
            #                     excel_input_file = file,
            #                     excel_output_file = output_file,
            #                     scenario_name = scenario_name,
            #                     output_solve = d_subproblem_solution[e],
            #                     b_print_solution_detail = True,
            #                     sVehiclesPaths = sSubVehiclesPaths,
            #                     sOriginalStationsPotential = sOriginalStationsPotential,
            #                     sSequenceNodesNodesVehiclesPaths = sSubSequenceNodesNodesVehiclesPaths,
            #                     sStationsPaths = sStationsPaths2,
            #                     sOriginalStationsOwn = sOriginalStationsOwn,
            #                     sStationsVehiclesPaths = sSubStationsVehiclesPaths,
            #                     pStartInventory = pStartInventory,
            #                     pDistance = pDistance,
            #                     pConsumptionRate = pConsumptionRate,
            #                     pConsumptionMainRoute = pConsumptionMainRoute,
            #                     pDistanceOOP = pDistanceOOP,
            #                     pConsumptionOOP = pConsumptionOOP,
            #                     pQuantityVehicles = pQuantityVehicles,
            #                     pVariableCost = pVariableCost,
            #                     pOpportunityCost = pOpportunityCost,
            #                     pPrice = pPrice)
          
        
            
            
            
            #In the first iteration of each subproblem define the iteration limits.
            if n_iterations_sub == 1:
                n_refuelling_times = sum(d_subproblem_ovRefuel[e][i,v,p] for (i,v,p) in sSubStationsVehiclesPaths)
                n_stations_sub = len(sSubStationsVehiclesPaths)
                
                if n_stations_sub <= n_refuelling_times*factor_options+slack_reduction:
                    #stop iterating over the subproblem, it is small enough in terms of stations per path.
                    #add an slack because if the path has stations in origin and destination and the 
                    #tank is full at origin and safety stock = target inventory. The vehicle
                    #wont be able to refuel in origin and in destination and we could fall
                    #in an infinite loop (slack must me >=2).
                    #use the same set to store the optional refuelling stations of this subproblem
                    #as the set that store the refuelling stations when the iteration continues
                    s_sSubStationsVehiclesPaths2 = set(sSubStationsVehiclesPaths)
                    break
                n_refuelling_options = n_refuelling_times*factor_options
                
            #increase the price for the stations in which the (vehicle,path) combination refuelled
            pPrice2 = {i: factor_price*pPrice2[i] if d_subproblem_ovRefuel[e][i, e[0], e[1]]>=0.99 else pPrice2[i] for (i,v,p) in sSubStationsVehiclesPaths}
            
            #store in a set the tuple set of stations in which the (veh,path) refuelled.
            #sets are used as data type because sets only allow unique values within 
            #and I need to be adding stations each iteration and they migh have already been chosen 
            #in a previous iteration.
            s_sAuxSubStationsVehiclesPaths2 = {(i,v,p) for (i,v,p) in sSubStationsVehiclesPaths if d_subproblem_ovRefuel[e][i, e[0], e[1]]>=0.99}
            
            #Add the current refuelling stations to the stations of the previous iteration
            if n_iterations_sub ==1:
                # since the set at the beginning is empty, it is a direct assignation,
                #after the first iteration, start using the union (union with empty is empty)
                s_sSubStationsVehiclesPaths2 = s_sAuxSubStationsVehiclesPaths2
            else:
                s_sSubStationsVehiclesPaths2 = s_sSubStationsVehiclesPaths2.union(s_sAuxSubStationsVehiclesPaths2)
            
            n_stations_chosen = len(s_sSubStationsVehiclesPaths2)
        
        s_sSubproblemStations = {i for (i,v,p) in s_sSubStationsVehiclesPaths2}
        
        #Build the new subsets associated to the current subproblem
        s_sSubNodesVehiclesPaths = s_sSubStationsVehiclesPaths2.union(sSubOriginVehiclesPaths).union(sSubDestinationVehiclesPaths) 
        
        s_sSubNodesPotentialNodesOriginalVehiclesPaths2 =\
        {(i,j,v,p) for (i,j,v,p) in sSubNodesPotentialNodesOriginalVehiclesPaths\
         for ii in s_sSubproblemStations if i==ii}
            
        #Build the sets for the integrated problem
        
        if e == sVehiclesPaths[0]:
            s_sStationsVehiclesPaths2 = s_sSubStationsVehiclesPaths2
            s_sNodesVehiclesPaths2 = s_sSubNodesVehiclesPaths
            s_sNodesPotentialNodesOriginalVehiclesPaths2 =\
                s_sSubNodesPotentialNodesOriginalVehiclesPaths2
        else:
            s_sStationsVehiclesPaths2 = s_sStationsVehiclesPaths2.union(s_sSubStationsVehiclesPaths2)
            s_sNodesVehiclesPaths2 = s_sNodesVehiclesPaths2.union(s_sSubNodesVehiclesPaths)
            s_sNodesPotentialNodesOriginalVehiclesPaths2 =\
                s_sNodesPotentialNodesOriginalVehiclesPaths2.union\
                (s_sSubNodesPotentialNodesOriginalVehiclesPaths2)        
            
        
        #Rebuild the sets and parameters that depends on the sequence of nodes in
        #path (sequence procedure)
        #intialize parameters of the rebuild sequence procedure
        aux_distance = 0
        #assign the origin associated to the current vehicle path
        aux = sSubOriginVehiclesPaths[0][0]
        v = e[0]
        p = e[1]
        index_segment = 0
        
        for ee in sSubSequenceNodesNodesVehiclesPaths:
            #if it is the origin then goes in the new list
            aux_distance = aux_distance + pDistance[ee[0], ee[1], ee[3]]
            if ee[1] in s_sSubproblemStations:
                i = aux
                j = ee[1]            
                aux = ee[1]
                sSequenceNodesNodesVehiclesPaths2.append((i,j,v,p))
                pSubDistance[i,j,v,p] = aux_distance
                aux_distance = 0
                #create the new first station
                index_segment +=1
                if index_segment ==1:
                    sFirstStationVehiclesPaths2.append((j,v,p))
                else:
                    sNotFirstStationVehiclesPaths2.append((j,v,p))
          
        #for the last segment of the path add the destination.
        i = aux
        j = sSubDestinationVehiclesPaths[0][0]
        sSequenceNodesNodesVehiclesPaths2.append((i,j,v,p))
        pSubDistance[i,j,v,p] = aux_distance
        
        s_sSubNodesPotentialNodesOriginalVehiclesPaths2 =\
        {(i,j,v,p) for (i,j,v,p) in sSubNodesPotentialNodesOriginalVehiclesPaths\
         for ii in s_sSubproblemStations if i==ii}
    
    #Update parameter because the path segments changed after the domain reduction
    pConsumptionMainRoute2 = {(i,j,v,p): pSubDistance[i,j,v,p]*pConsumptionRate[v]\
                              for (i,j,v,p) in sSequenceNodesNodesVehiclesPaths2}
    
    #convert the sets into lists to keep the modelling standards
    sStationsVehiclesPaths2 = list(s_sStationsVehiclesPaths2)
    sNodesVehiclesPaths2 = list(s_sNodesVehiclesPaths2)
    sNodesPotentialNodesOriginalVehiclesPaths2 =\
        list(s_sNodesPotentialNodesOriginalVehiclesPaths2)
    sStationsPaths2 = {(i,p) for (i,v,p) in sStationsVehiclesPaths2}
    
    return(sNodesVehiclesPaths2,
         sStationsVehiclesPaths2,
         sSequenceNodesNodesVehiclesPaths2,
         sFirstStationVehiclesPaths2,
         sNotFirstStationVehiclesPaths2,
         sNodesPotentialNodesOriginalVehiclesPaths2,
         sStationsPaths2,
         pSubDistance,
         pConsumptionMainRoute2)
