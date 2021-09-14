# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 10:37:39 2021

@author: calle
"""
#import pandas as pd
import gurobipy as gp
from gurobipy import GRB
import rfep_model

#Activate when debugging
import openpyxl
import sys
import jecs_functions
import os
import time
import export_solution_rfep

def solve_multiple_frvrp(
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
        pDistanceOOP = 0,
        isONcNoPurchaseOwn = False):
    """
    Parameters
    ----------
    
    -----
    
    """
    #this dict stores all the tuples that output the solve of the subproblem
    d_subproblem_solution = {}
    #d_subproblem_status = {}
    #d_subproblem_ovInventory = {}
    #d_subproblem_ovRefuelQuantity = {}
    #d_subproblem_ovRefuel = {}
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
    
  
    for e in sVehiclesPaths:
        sSubVehiclesPaths = [e]
        #update lists according to subproblem -> filter per vehicle path
        sSubNodesVehiclesPaths = [(i,v,p) for (i,v,p) in sNodesVehiclesPaths if v == e[0] and p==e[1]]
        sSubStationsVehiclesPaths = [(i,v,p) for (i,v,p) in sStationsVehiclesPaths if v == e[0] and p==e[1]]
        sSubOriginVehiclesPaths = [(i,v,p) for (i,v,p) in sOriginVehiclesPaths if v == e[0] and p==e[1]]
        sSubDestinationVehiclesPaths = [(i,v,p) for (i,v,p) in sDestinationVehiclesPaths if v == e[0] and p==e[1]]
        sSubSequenceNodesNodesVehiclesPaths = [(i,j,v,p) for (i,j,v,p) in sSequenceNodesNodesVehiclesPaths if v == e[0] and p==e[1]]
        sSubFirstStationVehiclesPaths = [(i,v,p) for (i,v,p) in sFirstStationVehiclesPaths  if v == e[0] and p==e[1]]
        sSubNotFirstStationVehiclesPaths = [(i,v,p) for (i,v,p) in sNotFirstStationVehiclesPaths  if v == e[0] and p==e[1]]
        sSubNodesPotentialNodesOriginalVehiclesPaths = [(i,j,v,p) for (i,j,v,p) in sNodesPotentialNodesOriginalVehiclesPaths  if v == e[0] and p==e[1]]
        
        
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
                                #pSafetyStock = pSafetyStock,
                                pTankCapacity = pTankCapacity,
                                pMinRefuel = pMinRefuel,
                                pConsumptionMainRoute = pConsumptionMainRoute,
                                pConsumptionOOP = pConsumptionOOP,
                                pQuantityVehicles = pQuantityVehicles,
                                pPrice = pPrice,
                                pOpportunityCost = pOpportunityCost,
                                pVariableCost = pVariableCost,
                                pDistanceOOP = pDistanceOOP,
                                isONvInventory = True,
                                isONvRefuelQuantity = True,
                                isONvRefuel = True,
                                isONcInitialInventory = True,
                                #isONcTargetInventory = True,
                                #isONcMinInventory = True,
                                isONcLogicRefuel1 = True,
                                isONcLogicRefuel2 = True,
                                isONcMaxRefuel = True,
                                isONcInventoryBalance1 = True,
                                isONcInventoryBalance2 = True,
                                isONcInventoryBalance3 = True,
                                isONcNoPurchaseOwn = isONcNoPurchaseOwn,
                                isONtotalRefuellingCost= True)                      
            
    #create specific variables for each output of the function
    #d_subproblem_status[e] = d_subproblem_solution[e][0]
    #d_subproblem_ovInventory[e] = d_subproblem_solution[e][1]
    #d_subproblem_ovRefuelQuantity[e] = d_subproblem_solution[e][2]
    #d_subproblem_ovRefuel[e] = d_subproblem_solution[e][3]
    #d_subproblem_oTotalRefuellingCost[e] = d_subproblem_solution[e][9]
    #d_subproblem_oTotalCost[e] = d_subproblem_solution[e][12]
    
        # #Debug subproblem
        # output_file = os.path.join("..", "output", "outputRFEPSubproblem_v1.xlsx")
        # scenario_name = str(e[0]) + str(e[1]) + "2000km path"
        # file = "tv2-pa10-ow30-cl20-su2"
        # sStationsPaths2 = {(i,p) for (i,v,p) in sSubStationsVehiclesPaths}
        # export_solution_rfep.export_solution_rfep(
        #                     excel_input_file = file,
        #                     excel_output_file = output_file,
        #                     scenario_name = scenario_name,
        #                     output_solve = d_subproblem_solution[e],
        #                     b_print_solution_detail = True,
        #                     b_print_location = False,
        #                     b_print_statistics = True,
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
    return(d_subproblem_solution)
