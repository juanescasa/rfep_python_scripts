# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 13:49:14 2021

@author: calle
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 11:57:12 2021

@author: calle
"""
#Practising callbacks
import gurobipy as gp
from gurobipy import GRB
import time

#Create the callback function

# Base data
sOrigins, pSupply = gp.multidict({
    ('i1'):   10,
    ('i2'):  30,
    ('i3'):  40,
    ('i4'):  20,
    })

sDestinations, pDemand = gp.multidict({
    ('j1'):   20,
    ('j2'):  50,
    ('j3'):  30,
    })

pCost = {
    ('i1', 'j1'): 2,
    ('i1', 'j2'): 3,
    ('i1', 'j3'): 4,
    ('i2', 'j1'): 3,
    ('i2', 'j2'): 2,
    ('i2', 'j3'): 1,
    ('i3', 'j1'): 1,
    ('i3', 'j2'): 4,
    ('i3', 'j3'): 3,
    ('i4', 'j1'): 4,
    ('i4', 'j2'): 5,
    ('i4', 'j3'): 2  
}

pOpenCost = {
    ('i1', 'j1'): 10,
    ('i1', 'j2'): 30,
    ('i1', 'j3'): 20,
    ('i2', 'j1'): 10,
    ('i2', 'j2'): 30,
    ('i2', 'j3'): 20,
    ('i3', 'j1'): 10,
    ('i3', 'j2'): 30,
    ('i3', 'j3'): 20,
    ('i4', 'j1'): 10,
    ('i4', 'j2'): 30,
    ('i4', 'j3'): 20  
}

M = {(i,j): min(pSupply[i], pDemand[j]) for i in sOrigins for j in sDestinations}

#create model
m=gp.Model()

#create variables
vTransport = m.addVars(sOrigins, sDestinations, name="vTransport")
vOpen = m.addVars(sOrigins, sDestinations, vtype = GRB.BINARY, name="vOpen")

#create constraints
#supply constraint
m.addConstrs((vTransport.sum(i,'*') <= pSupply[i] for i in sOrigins), name='capacity')
#demand constraint
m.addConstrs((vTransport.sum('*', j) >= pDemand[j] for j in sDestinations), name='demandSatisfaction')
#Logic constraint
#m.addConstrs((vTransport[i,j] <= M[i,j]*vOpen[i,j] for (i,j) in sOriginsDestinations), name='logicOpenArc')
m.addConstrs((vTransport[i,j] <= M[i,j]*vOpen[i,j] for i in sOrigins for j in sDestinations), name='logicOpenArc')

#create objective function
m.setObjective(vTransport.prod(pCost) + vOpen.prod(pOpenCost) , GRB.MINIMIZE)

m.tune()
for i in range(m.tuneResultCount):
    m.write('tune'+str(i)+'.prm')
    
m.optimize()
print()

solution = m.getAttr('x', vTransport)
print('Objective function: ' + str(m.ObjVal))
for i in sOrigins:
    for j in sDestinations:
        if solution[i,j]>0:
            print('%s -> %s: %g' % (i, j,  solution[i,j]))