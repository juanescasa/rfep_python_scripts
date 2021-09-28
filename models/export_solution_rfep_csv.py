# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 17:01:32 2021

@author: calle
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 17:13:19 2021

@author: calle
"""
import openpyxl
import csv
# importing datetime module for now() 
import datetime
import platform

#this function is auxiliary to the main export function. I did it to add readability to the code of the main funciton
#this fuction is defined to export the stats of solving the rfep
def print_stats_solution_complete(file_name, current_time, ls_scenario_name, ls_output_solve, ls_total_time, machine, ls_solution_algorithm):
    for index_run in range(len(ls_total_time)):
                with open(file_name, "a", newline = "") as f:
                    cw = csv.writer(f, delimiter=",")
                    cw.writerow((current_time,
                            ls_scenario_name[index_run],
                            #n_vehicles
                            ls_output_solve[index_run][25],
                            #n_paths
                            ls_output_solve[index_run][26],
                            #n_avg_stations_path                   
                            ls_output_solve[index_run][27],
                            #n_candidate_locations
                            ls_output_solve[index_run][28],
                            ls_total_time[index_run],
                            #model_runtime
                            ls_output_solve[index_run][18],
                            #n_constraints,
                            ls_output_solve[index_run][13],
                            #n_variables
                            ls_output_solve[index_run][14],
                            #n_integer_variables
                            ls_output_solve[index_run][15],
                            #n_binary_variables
                            ls_output_solve[index_run][16],
                            #mip_gap
                            ls_output_solve[index_run][19],
                            #model_nodeCount
                            ls_output_solve[index_run][20],
                            #model_initial_gap
                            ls_output_solve[index_run][21],
                            #model_time_first_incumbent
                            ls_output_solve[index_run][22],
                            #status
                            ls_output_solve[index_run][0],
                            machine,
                            ls_solution_algorithm[index_run],
                            #total_refuelling_cost
                            ls_output_solve[index_run][9],
                            #total_location_cost
                            ls_output_solve[index_run][10],
                            #total_discount
                            ls_output_solve[index_run][11],
                            #total_cost
                            ls_output_solve[index_run][12],
                            #fingerprint
                            ls_output_solve[index_run][17]
                            ))

#This function is defined when the solution to the RFEP does not come from solving an optimization problem
def print_stats_solution_summary(file_name, current_time, ls_scenario_name, ls_total_time, machine, ls_solution_algorithm):
    for index_run in range(len(ls_total_time)):
                with open(file_name, "a", newline = "") as f:
                    cw = csv.writer(f, delimiter=",")
                    cw.writerow((current_time,
                            ls_scenario_name[index_run],
                            "",
                            "",
                            "",
                            "",
                            ls_total_time[index_run],
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            machine,
                            ls_solution_algorithm[index_run],
                            "",
                            "",
                            "",
                            "",
                            ""))
#this is the main function of this script
def export_solution_rfep(ls_data_rfep = [],
                        ls_scenario_name = [],
                        ls_solution_algorithm = [],
                        ls_output_solve = [],
                        ls_total_time = [],
                        b_domain_reduction = False,
                        b_print_refuelling_detail = False,
                        b_print_refuelling_summary = False,
                        b_print_location_detail = False,
                        b_print_location_summary = False,
                        b_print_suppliers = False,
                        b_print_statistics = False,
                        b_retrieve_solve_ouput = True):                      
                        
    
    """
    export_solution_rfep prints into .csv files the solution of a run of the RFEP. 
    It can print the detailed solution of the problem or a summarized version on the 
    output depending on the configuration of all boolean variables.
    
    Assumptions: it assumes that exists a folder above this script which is called
    output in which it will print the csv files
                           
    :param ls_data_rfep: it is a list that contain all the data related to each scenario. 
    The index makes reference to a given scenario
    
    :param ls_scenario_name: the index of this list is associated to each run.
    
    :param ls_solution_algorithm
    
    :param ls_output_solve = []
    
    :param ls_total_time
    
    :param b_domain_reduction
    
    :param b_print_detail
    
    :param b_print_refuelling_summary
    
    :param b_print_location:
    
    :param b_print_location_summary:
    
    :param b_print_statistics:
    
    :param b_retrieve_solve_ouput: this param must be True if the RFEP solution comes 
                directly from solving the RFEP, otherwise (if it comes from heuristic) it should be false.
    
    :return: this function does not return anything, it just prints.
    """
    #retrieve generic parameters
    # using now() to get current time 
    current_time = datetime.datetime.now()   
    #retrieve an id for the machine that is running
    machine = platform.uname()[1]
  
    #if b_print_refuelling_detail and model_time_first_incumbent >0:               
    if b_print_refuelling_detail:
        file_name = "..\\output\\o_refuelling_details.csv"
        #I use ls)total_time as a generic list to get the number of runs that were run
        for index_run in range(len(ls_total_time)):
            
            for (i,j,v,p) in ls_data_rfep[index_run]["sSequenceNodesNodesVehiclesPaths"]:
                if (j,p) in ls_data_rfep[index_run]["sStationsPaths"]:
                    #I need to know if the domain was reduced to know which distance parameter should I export
                    #the distance(i,j,p) or distance(i,j,v,p) that comes from the domain reduction procedure
                    if b_domain_reduction:
                        with open(file_name, "a", newline = "") as f:
                            cw = csv.writer(f, delimiter=",")
                            cw.writerow((current_time, ls_scenario_name[index_run], machine,
                                         ls_solution_algorithm[index_run],
                                         #indexes, inventory
                                         i, j, v, p, ls_output_solve[index_run][1][j,v,p],
                                         #refuel quantity
                                         ls_output_solve[index_run][2][j,v,p],
                                         #bin refuel
                                         ls_output_solve[index_run][3][j,v,p],
                                         ls_data_rfep[index_run]["pStartInventory"][v,p],
                                         ls_data_rfep[index_run]["pConsumptionRate"][v],
                                         ls_data_rfep[index_run]["pSubDistance"][i,j,v,p],
                                         ls_data_rfep[index_run]["pConsumptionMainRoute"][i,j,v,p],
                                         ls_data_rfep[index_run]["pDistanceOOP"][j,p],
                                         ls_data_rfep[index_run]["pConsumptionOOP"][j,v,p],
                                         ls_data_rfep[index_run]["pPrice"][j],
                                         #this is a placeholder in case I need this to run single corridor
                                         #this is the parameter RefuelQuantity for history
                                         0,
                                         ls_data_rfep[index_run]["pQuantityVehicles"][v,p],
                                         ls_data_rfep[index_run]["pVariableCost"][v],
                                         ls_data_rfep[index_run]["pOpportunityCost"][v]))
                        
                    else:
                        with open(file_name, "a", newline = "") as f:
                            cw = csv.writer(f, delimiter=",")
                            cw.writerow((current_time, ls_scenario_name[index_run], machine,
                                         ls_solution_algorithm[index_run],
                                         #indexes, inventory
                                         i, j, v, p, ls_output_solve[index_run][1][j,v,p],
                                         #refuel quantity
                                         ls_output_solve[index_run][2][j,v,p],
                                         #bin refuel
                                         ls_output_solve[index_run][3][j,v,p],
                                         ls_data_rfep[index_run]["pStartInventory"][v,p],
                                         ls_data_rfep[index_run]["pConsumptionRate"][v],
                                         ls_data_rfep[index_run]["pDistance"][i,j,p],
                                         ls_data_rfep[index_run]["pConsumptionMainRoute"][i,j,v,p],
                                         ls_data_rfep[index_run]["pDistanceOOP"][j,p],
                                         ls_data_rfep[index_run]["pConsumptionOOP"][j,v,p],
                                         ls_data_rfep[index_run]["pPrice"][j],
                                         #this is a placeholder in case I need this to run single corridor
                                         #this is the parameter RefuelQuantity for history
                                         0,
                                         ls_data_rfep[index_run]["pQuantityVehicles"][v,p],
                                         ls_data_rfep[index_run]["pVariableCost"][v],
                                         ls_data_rfep[index_run]["pOpportunityCost"][v]))
    
              
                        
    if b_print_refuelling_summary:
        if b_retrieve_solve_ouput:
            file_name = "..\\output\\o_refuelling_summary.csv"
            for index_run in range(len(ls_total_time)):
                
         
                sStationsRefuelledVehiclePath = list(ls_output_solve[index_run][23].keys())
                for (i,v,p) in sStationsRefuelledVehiclePath:
                    with open(file_name, "a", newline = "") as f:
                                cw = csv.writer(f, delimiter=",")
                                cw.writerow((current_time, ls_scenario_name[index_run], machine,
                                             ls_solution_algorithm[index_run],
                                             i, v, p, ls_output_solve[index_run][23][i,v,p]))                 
            
        
    di_refuel_qty_station = {i: sum(ls_output_solve[index_run][3][j,v,p]*ls_data_rfep[index_run]["pQuantityVehicles"][v,p]
                                      for (j,v,p) in ls_data_rfep[index_run]["sStationsVehiclesPaths"]
                                      if (i,j) in ls_data_rfep[index_run]["sOriginalStationsMirrorStations"]) 
                              for i in ls_data_rfep[index_run]["sStations"]}
    if b_print_location_detail:
        file_name = "..\\output\\o_location_details.csv"
        for index_run in range(len(ls_total_time)):
            for i in ls_data_rfep[index_run]["sOriginalStationsOwn"]:
                with open(file_name, "a", newline = "") as f:
                             cw = csv.writer(f, delimiter=",")
                             cw.writerow((current_time, ls_scenario_name[index_run],
                                          machine, ls_solution_algorithm[index_run], i,
                                          #location
                                          ls_output_solve[index_run][5][i] if i in ls_data_rfep[index_run]["sOriginalStationsPotential"] else 0,
                                          #units of capacity
                                          ls_output_solve[index_run][4][i] if i in ls_data_rfep[index_run]["sOriginalStationsOwn"] else 0,
                                          ls_data_rfep[index_run]["pStationCapacity"][i] if i in ls_data_rfep[index_run]["sOriginalStationsOwn"] else 0,
                                          ls_data_rfep[index_run]["pStationUnitCapacity"][i] if i in ls_data_rfep[index_run]["sOriginalStationsOwn"] else 0,
                                          ls_data_rfep[index_run]["pLocationCost"][i]  if i in ls_data_rfep[index_run]["sOriginalStationsPotential"] else 0,
                                          ls_data_rfep[index_run]["pCostUnitCapacity"][i] if i in ls_data_rfep[index_run]["sOriginalStationsOwn"] else 0,
                                          di_refuel_qty_station[i]))
    #if b_print_location and model_time_first_incumbent >0:
    if b_print_location_summary:
        if b_retrieve_solve_ouput:
            file_name = "..\\output\\o_location_summary.csv"
            for index_run in range(len(ls_total_time)):
                #ovLocate = output_solve[index_run][5]
                #ovQuantityUnitsCapacity = output_solve[4]
                sOriginalStationsOwn = list(ls_output_solve[index_run][4].keys())
                sOriginalStationsPotential = list(ls_output_solve[index_run][5].keys())
                for i in sOriginalStationsOwn:                    
                        if ((ls_output_solve[index_run][5][i] if i in sOriginalStationsPotential else 0) > 0 or ls_output_solve[index_run][4][i])>0:
                            with open(file_name, "a", newline = "") as f:
                                cw = csv.writer(f, delimiter=",")
                                cw.writerow((current_time, ls_scenario_name[index_run],
                                             machine, ls_solution_algorithm[index_run], i,
                                             #location
                                             ls_output_solve[index_run][5][i] if i in sOriginalStationsPotential else 0,
                                             #units of capacity
                                             ls_output_solve[index_run][4][i]))                                
    #print supplier details
    
    if b_print_suppliers:
        
        if b_retrieve_solve_ouput:
            file_name = "..\\output\\o_suppliers_details.csv"                       
            for index_run in range(len(ls_total_time)):
                for (l,g) in ls_data_rfep[index_run]["sSuppliersRanges"]:
                    
                     with open(file_name, "a", newline = "") as f:
                                    cw = csv.writer(f, delimiter=",")
                                    cw.writerow((current_time, ls_scenario_name[index_run],
                                                 machine, ls_solution_algorithm[index_run], l, g,
                                                 #purchase quantity
                                                 ls_output_solve[index_run][6][l],
                                                 #purchase quantity in range
                                                 ls_output_solve[index_run][7][l,g],
                                                 #bin purchased in range
                                                 ls_output_solve[index_run][8][l,g],
                                                 ls_data_rfep[index_run]["pLowerQuantityDiscount"][l,g],
                                                 ls_data_rfep[index_run]["pUpperQuantityDiscount"][l,g],
                                                 ls_data_rfep[index_run]["pDiscount"][l,g]))
                                                 
                                                 
                                                 
                                                 
                
            
    
    if b_print_statistics:
        file_name = "..\\output\\o_scenario_stats.csv"
        if b_retrieve_solve_ouput:            
            print_stats_solution_complete(file_name, current_time, ls_scenario_name, 
                                          ls_output_solve, ls_total_time, machine, 
                                          ls_solution_algorithm)
        else:
            print_stats_solution_summary(file_name, current_time, ls_scenario_name, 
                                         ls_total_time, machine, ls_solution_algorithm)
            
          
        # if b_print_read_stats:
        #     aux=23
        #     for event in di_event_read:
        #         aux+=1
        #         ws.cell(row = index_row, column = aux, value = di_event_read[event])
        #     for process in di_process_duration_read:
        #         aux+=1
        #         ws.cell(row = index_row, column = aux, value = di_process_duration_read[process])
        #  #after printing read stats, next column is number 94       
          

        

