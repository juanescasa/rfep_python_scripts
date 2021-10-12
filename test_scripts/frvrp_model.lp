\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  1.5 vRefuelQuantity[st1] + 1.1 vRefuelQuantity[st2]
   + 1.3 vRefuelQuantity[st3] + 0 vInventory[origin]
Subject To
 cMinimumInventory[st1]: vInventory[st1] >= 2
 cMinimumInventory[st2]: vInventory[st2] >= 2
 cMinimumInventory[st3]: vInventory[st3] >= 2
 cTargetInventory[destination]: vInventory[destination] >= 11
 cMinimumRefuellingQuantity[st1]: vRefuelQuantity[st1] - 10 vRefuel[st1]
   >= 0
 cMinimumRefuellingQuantity[st2]: vRefuelQuantity[st2] - 10 vRefuel[st2]
   >= 0
 cMinimumRefuellingQuantity[st3]: vRefuelQuantity[st3] - 10 vRefuel[st3]
   >= 0
 cLogicRefuelling[st1]: vRefuelQuantity[st1] - 100 vRefuel[st1] <= 0
 cLogicRefuelling[st2]: vRefuelQuantity[st2] - 100 vRefuel[st2] <= 0
 cLogicRefuelling[st3]: vRefuelQuantity[st3] - 100 vRefuel[st3] <= 0
 cTankCapacity[st1]: vRefuelQuantity[st1] + vInventory[st1] <= 100
 cTankCapacity[st2]: vRefuelQuantity[st2] + vInventory[st2] <= 100
 cTankCapacity[st3]: vRefuelQuantity[st3] + vInventory[st3] <= 100
 cInventoryBalance1[origin,st1]: vRefuel[st1] + vInventory[st1] = 5
 cInventoryBalance2[st1,st2]: - vRefuelQuantity[st1] + vRefuel[st1]
   + 0.8 vRefuel[st2] - vInventory[st1] + vInventory[st2] = -30
 cInventoryBalance2[st2,st3]: - vRefuelQuantity[st2] + 0.8 vRefuel[st2]
   + 0.2 vRefuel[st3] - vInventory[st2] + vInventory[st3] = -40
 cInventoryBalance3[st3,destination]: - vRefuelQuantity[st3]
   + 0.2 vRefuel[st3] - vInventory[st3] + vInventory[destination] = -50
Bounds
Binaries
 vRefuel[st1] vRefuel[st2] vRefuel[st3]
End
