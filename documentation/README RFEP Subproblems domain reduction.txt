RFEP Subproblems domain reduction.py
    auxiliaries files
        input file
            Data Model Generated Network-12.xlsx
        output file
            outputRFEPSubproblem_v1.xlsx
    modules required
        export_solution_rfep
        read_data_rfep
        rfep_model.py
    Pseudocode
        Read data
        Enters a loop to solve subproblems
            Reduce the domain of each subproblem
            Updates the sets and required parameters (distance and fuel consumption in segments)
        Solve the complete RFEP after domain reduction
        Exports the solution of the RFEP after domain reduction
        Solve the RFEP without domain reduction
        Export the solution of the RFEP

