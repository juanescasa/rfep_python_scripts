#How to retrieve the non-zero values of dictionaries.

li_StationsVehicles = [('st1', 'v2'),
                      ('st1', 'v3'),
                      ('st2', 'v4'),
                      ('st3', 'v5')]

di_ovRefuel = {('st1', 'v2'): 100,
                ('st1', 'v3'): 0,
                ('st2', 'v4'): 0,
                ('st3', 'v5'): 70 }

di_ovsRefuel = {(i,v): di_ovRefuel[i,v]  for (i,v) in li_StationsVehicles if di_ovRefuel[i,v]>0}
