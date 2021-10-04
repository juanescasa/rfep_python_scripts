\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  2 vTransport[i1,j1] + 3 vTransport[i1,j2] + 4 vTransport[i1,j3]
   + 3 vTransport[i2,j1] + 2 vTransport[i2,j2] + vTransport[i2,j3]
   + vTransport[i3,j1] + 4 vTransport[i3,j2] + 3 vTransport[i3,j3]
   + 4 vTransport[i4,j1] + 5 vTransport[i4,j2] + 2 vTransport[i4,j3]
   + 10 vOpen[i1,j1] + 30 vOpen[i1,j2] + 20 vOpen[i1,j3] + 10 vOpen[i2,j1]
   + 30 vOpen[i2,j2] + 20 vOpen[i2,j3] + 10 vOpen[i3,j1] + 30 vOpen[i3,j2]
   + 20 vOpen[i3,j3] + 10 vOpen[i4,j1] + 30 vOpen[i4,j2] + 20 vOpen[i4,j3]
Subject To
 capacity[i1]: vTransport[i1,j1] + vTransport[i1,j2] + vTransport[i1,j3]
   <= 10
 capacity[i2]: vTransport[i2,j1] + vTransport[i2,j2] + vTransport[i2,j3]
   <= 30
 capacity[i3]: vTransport[i3,j1] + vTransport[i3,j2] + vTransport[i3,j3]
   <= 40
 capacity[i4]: vTransport[i4,j1] + vTransport[i4,j2] + vTransport[i4,j3]
   <= 20
 demandSatisfaction[j1]: vTransport[i1,j1] + vTransport[i2,j1]
   + vTransport[i3,j1] + vTransport[i4,j1] >= 20
 demandSatisfaction[j2]: vTransport[i1,j2] + vTransport[i2,j2]
   + vTransport[i3,j2] + vTransport[i4,j2] >= 50
 demandSatisfaction[j3]: vTransport[i1,j3] + vTransport[i2,j3]
   + vTransport[i3,j3] + vTransport[i4,j3] >= 30
 logicOpenArc[i1,j1]: vTransport[i1,j1] - 10 vOpen[i1,j1] <= 0
 logicOpenArc[i1,j2]: vTransport[i1,j2] - 10 vOpen[i1,j2] <= 0
 logicOpenArc[i1,j3]: vTransport[i1,j3] - 10 vOpen[i1,j3] <= 0
 logicOpenArc[i2,j1]: vTransport[i2,j1] - 20 vOpen[i2,j1] <= 0
 logicOpenArc[i2,j2]: vTransport[i2,j2] - 30 vOpen[i2,j2] <= 0
 logicOpenArc[i2,j3]: vTransport[i2,j3] - 30 vOpen[i2,j3] <= 0
 logicOpenArc[i3,j1]: vTransport[i3,j1] - 20 vOpen[i3,j1] <= 0
 logicOpenArc[i3,j2]: vTransport[i3,j2] - 40 vOpen[i3,j2] <= 0
 logicOpenArc[i3,j3]: vTransport[i3,j3] - 30 vOpen[i3,j3] <= 0
 logicOpenArc[i4,j1]: vTransport[i4,j1] - 20 vOpen[i4,j1] <= 0
 logicOpenArc[i4,j2]: vTransport[i4,j2] - 20 vOpen[i4,j2] <= 0
 logicOpenArc[i4,j3]: vTransport[i4,j3] - 20 vOpen[i4,j3] <= 0
Bounds
Binaries
 vOpen[i1,j1] vOpen[i1,j2] vOpen[i1,j3] vOpen[i2,j1] vOpen[i2,j2]
 vOpen[i2,j3] vOpen[i3,j1] vOpen[i3,j2] vOpen[i3,j3] vOpen[i4,j1]
 vOpen[i4,j2] vOpen[i4,j3]
End
