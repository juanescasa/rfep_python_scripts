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
                            ls_output_solve[index_run][12]                       
                            ))
    
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
                            ""))

def export_solution_rfep(ls_data_rfep = [],
                        ls_scenario_name = [],
                        ls_solution_algorithm = [],
                        ls_output_solve = [],
                        b_domain_reduction = False,
                        b_print_refuelling_detail = False,
                        b_print_refuelling_summary = False,
                        b_print_location = False,
                        b_print_location_summary = False,
                        b_print_statistics = False,
                        b_print_read_stats = False,
                        b_retrieve_solve_ouput = True,                        
                        ls_total_time=[],
                        di_event_read = {},
                        di_process_duration_read = {},
                        sVehiclesPaths = [],
                        sOriginalStationsPotential=[],
                        sSequenceNodesNodesVehiclesPaths=[],
                        sDestinationVehiclePath=[],
                        sStationsPaths=set(),
                        sOriginalStationsOwn=[],
                        sStationsVehiclesPaths=[],
                        sSuppliersRanges=[],
                        pStartInventory=0,
                        pConsumptionRate=0,
                        pDistance=0,
                        pSubDistance=0,
                        pConsumptionMainRoute=0,
                        pDistanceOOP=0,
                        pConsumptionOOP=0,
                        pQuantityVehicles=0,
                        pVariableCost=0,
                        pOpportunityCost=0,
                        pLocationCost=0,
                        pStationCapacity=0,
                        pStationUnitCapacity=0,
                        pCostUnitCapacity=0,
                        pPrice=0,
                        pDiscount=0):
    
    """
    export_solution_rfep prints into an excel file the solution of a run of the RFEP
    
    :param excel_input_file: input data used to run the scenario. In multiple scenario
                        runs this file is replaced by the folder of the generated tables                            
                        
    :param b_retrieve_solve_ouput: this param must be True if the RFEP solution comes 
                directly from solving the RFEP, otherwise (if it comes from heuristic) it should be false.
    :param di_event_read: dictionary that holds the time in which each event in the data reading process happened
    :param di_process_events_read: dictionary that holds the duration of each process in the data reading
    :return: this function does not return anything, it just prints.
    """
    #retrieve generic parameters
    # using now() to get current time 
    current_time = datetime.datetime.now()   
    machine = platform.uname()[1]
  
    #if b_print_refuelling_detail and model_time_first_incumbent >0:               
    if b_print_refuelling_detail:
        file_name = "..\\output\\o_refuelling_details.csv"
        for index_run in range(len(ls_total_time)):
            
            
            for (i,j,v,p) in ls_data_rfep[index_run]["sSequenceNodesNodesVehiclesPaths"]:
                if (j,p) in ls_data_rfep[index_run]["sStationsPaths"]:
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
                        print(ls_output_solve[index_run][1][j,v,p])
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
                        
    #       sheet_name = 'oNodesNodesVehiclesPaths'
    #       ws = workbook[sheet_name]
    #       index_row = ws.max_row    
    #       for (i,j,v,p) in sSequenceNodesNodesVehiclesPaths:
    #          if (j,p) in sStationsPaths:
    #                 index_row=index_row +1
    #                 ws.cell(row=index_row, column = 1, value=scenario)
    #                 ws.cell(row=index_row, column = 2, value=i)
    #                 ws.cell(row=index_row, column = 3, value=j)
    #                 ws.cell(row=index_row, column = 4, value=v)
    #                 ws.cell(row=index_row, column = 5, value=p)
    #                 ws.cell(row=index_row, column = 6, value=ovInventory[j,v,p])
    #                 ws.cell(row=index_row, column = 7, value=ovRefuelQuantity[j,v,p])
    #                 ws.cell(row=index_row, column = 8, value=ovRefuel[j,v,p])
    #                 ws.cell(row=index_row, column = 9, value=pStartInventory[v,p])
    #                 ws.cell(row=index_row, column = 10, value=pConsumptionRate[v])
    #                 #if a domain reduction procedure was applied, the distance 
    #                 #changed of domain
    #                 if b_domain_reduction:
    #                     ws.cell(row=index_row, column = 11, value=pSubDistance[i,j,v,p])
    #                 else:
    #                     ws.cell(row=index_row, column = 11, value=pDistance[i,j,p])   
                    
    #                 #trhe distance changed of index after the domain reduction. So the original distance wont fit
    #                 #
                    
    #                 ws.cell(row=index_row, column = 12, value=pConsumptionMainRoute[i,j,v,p])
    #                 ws.cell(row=index_row, column = 13, value=pDistanceOOP[j,p])
    #                 ws.cell(row=index_row, column = 14, value=pConsumptionOOP[j,v,p])
    #                 ws.cell(row=index_row, column = 15, value=pPrice[j])
    #                 ws.cell(row=index_row, column = 16, value=0) #this is a placeholder in case I need this to run single corridor
    #                 ws.cell(row=index_row, column = 17, value=pQuantityVehicles[v,p])
    #                 ws.cell(row=index_row, column = 18, value=pVariableCost[v])
    #                 ws.cell(row=index_row, column = 19, value=pOpportunityCost[v])
    #                 ws.cell(row=index_row, column = 20, value=excel_input_file)
                        
      ##  Print location variables
    # if b_print_location and model_time_first_incumbent >0:
          
    #       sheet_name = 'oOriginalStationsOwn'
    #       ws = workbook[sheet_name]
    #       index_row = ws.max_row    
            
          # for i in sOriginalStationsOwn:
          #    index_row = index_row+1
          #    ws.cell(row=index_row, column = 1, value = scenario)
          #    ws.cell(row=index_row, column = 2, value = i)
          #    if i in sOriginalStationsPotential:
          #           ws.cell(row=index_row, column = 3, value = ovLocate[i])
          #           ws.cell(row=index_row, column = 7, value = pLocationCost[i])
          #    else:
          #           ws.cell(row=index_row, column = 3, value = 0)
          #           ws.cell(row=index_row, column = 7, value = 0)
          #    ws.cell(row=index_row, column = 4, value = ovQuantityUnitsCapacity[i])
          #    ws.cell(row=index_row, column = 5, value = pStationCapacity[i])
          #    ws.cell(row=index_row, column = 6, value = pStationUnitCapacity[i])
          #    ws.cell(row=index_row, column = 8, value = pCostUnitCapacity[i])
          #    ws.cell(row=index_row, column = 9, value = excel_input_file)

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
                    
            
        

    #if b_print_location and model_time_first_incumbent >0:
    if b_print_location_summary:
        if b_retrieve_solve_ouput:
            file_name = "..\\output\\o_location_summary.csv"
            for index_run in range(len(ls_total_time)):
                #ovLocate = output_solve[index_run][5]
                #ovQuantityUnitsCapacity = output_solve[4]
                sOriginalStationsOwn = list(ls_output_solve[index_run][4].keys())
                sOwnStationsPotential = list(ls_output_solve[index_run][5].keys())
                for i in sOriginalStationsOwn:
                    if i in sOwnStationsPotential:
                        if (ls_output_solve[index_run][5][i]>0 or ls_output_solve[index_run][4][i])>0:
                            with open(file_name, "a", newline = "") as f:
                                cw = csv.writer(f, delimiter=",")
                                cw.writerow((current_time, ls_scenario_name[index_run],
                                             machine, ls_solution_algorithm[index_run], i,
                                             #location
                                             ls_output_solve[index_run][5][i],
                                             #units of capacity
                                             ls_output_solve[index_run][4][i]))
                    else:
                       if (ls_output_solve[index_run][4][i])>0:
                            with open(file_name, "a", newline = "") as f:
                                cw = csv.writer(f, delimiter=",")
                                cw.writerow((current_time, ls_scenario_name[index_run],
                                             machine, ls_solution_algorithm[index_run], i,
                                             #location
                                             0,
                                             #units of capacity
                                             ls_output_solve[index_run][4][i]))     
                                         
                                         
                        
        
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
          
    #workbook.save(output_file)
    
        

