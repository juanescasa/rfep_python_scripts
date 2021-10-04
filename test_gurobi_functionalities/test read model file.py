# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 18:21:44 2021

@author: calle
"""
#reaad a model file using Gurobi
import gurobipy as gp
from gurobipy import GRB

model = gp.read("fctp.mps")

#number of improved parameter sets returned. see https://www.gurobi.com/documentation/9.1/refman/tuneresults.html
model.Params.tuneResults = 1

# Tune the model
model.tune()

if model.tuneResultCount > 0:

    # Load the best tuned parameters into the model
    model.getTuneResult(0)

    # Write tuned parameters to a file
    model.write('tune0.prm')

    # Solve the model using the tuned parameters
    model.optimize()
    

model2  = gp.read("fctp.mps")

model2.readParams('tune0.prm')

model.write('DidIreadParam.prm')
