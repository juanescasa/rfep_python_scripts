NAME 
ROWS
 N  OBJ
 L  capacity[i1]
 L  capacity[i2]
 L  capacity[i3]
 L  capacity[i4]
 G  demandSatisfaction[j1]
 G  demandSatisfaction[j2]
 G  demandSatisfaction[j3]
 L  logicOpenArc[i1,j1]
 L  logicOpenArc[i1,j2]
 L  logicOpenArc[i1,j3]
 L  logicOpenArc[i2,j1]
 L  logicOpenArc[i2,j2]
 L  logicOpenArc[i2,j3]
 L  logicOpenArc[i3,j1]
 L  logicOpenArc[i3,j2]
 L  logicOpenArc[i3,j3]
 L  logicOpenArc[i4,j1]
 L  logicOpenArc[i4,j2]
 L  logicOpenArc[i4,j3]
COLUMNS
    vTransport[i1,j1]  OBJ       2
    vTransport[i1,j1]  capacity[i1]  1
    vTransport[i1,j1]  demandSatisfaction[j1]  1
    vTransport[i1,j1]  logicOpenArc[i1,j1]  1
    vTransport[i1,j2]  OBJ       3
    vTransport[i1,j2]  capacity[i1]  1
    vTransport[i1,j2]  demandSatisfaction[j2]  1
    vTransport[i1,j2]  logicOpenArc[i1,j2]  1
    vTransport[i1,j3]  OBJ       4
    vTransport[i1,j3]  capacity[i1]  1
    vTransport[i1,j3]  demandSatisfaction[j3]  1
    vTransport[i1,j3]  logicOpenArc[i1,j3]  1
    vTransport[i2,j1]  OBJ       3
    vTransport[i2,j1]  capacity[i2]  1
    vTransport[i2,j1]  demandSatisfaction[j1]  1
    vTransport[i2,j1]  logicOpenArc[i2,j1]  1
    vTransport[i2,j2]  OBJ       2
    vTransport[i2,j2]  capacity[i2]  1
    vTransport[i2,j2]  demandSatisfaction[j2]  1
    vTransport[i2,j2]  logicOpenArc[i2,j2]  1
    vTransport[i2,j3]  OBJ       1
    vTransport[i2,j3]  capacity[i2]  1
    vTransport[i2,j3]  demandSatisfaction[j3]  1
    vTransport[i2,j3]  logicOpenArc[i2,j3]  1
    vTransport[i3,j1]  OBJ       1
    vTransport[i3,j1]  capacity[i3]  1
    vTransport[i3,j1]  demandSatisfaction[j1]  1
    vTransport[i3,j1]  logicOpenArc[i3,j1]  1
    vTransport[i3,j2]  OBJ       4
    vTransport[i3,j2]  capacity[i3]  1
    vTransport[i3,j2]  demandSatisfaction[j2]  1
    vTransport[i3,j2]  logicOpenArc[i3,j2]  1
    vTransport[i3,j3]  OBJ       3
    vTransport[i3,j3]  capacity[i3]  1
    vTransport[i3,j3]  demandSatisfaction[j3]  1
    vTransport[i3,j3]  logicOpenArc[i3,j3]  1
    vTransport[i4,j1]  OBJ       4
    vTransport[i4,j1]  capacity[i4]  1
    vTransport[i4,j1]  demandSatisfaction[j1]  1
    vTransport[i4,j1]  logicOpenArc[i4,j1]  1
    vTransport[i4,j2]  OBJ       5
    vTransport[i4,j2]  capacity[i4]  1
    vTransport[i4,j2]  demandSatisfaction[j2]  1
    vTransport[i4,j2]  logicOpenArc[i4,j2]  1
    vTransport[i4,j3]  OBJ       2
    vTransport[i4,j3]  capacity[i4]  1
    vTransport[i4,j3]  demandSatisfaction[j3]  1
    vTransport[i4,j3]  logicOpenArc[i4,j3]  1
    MARKER    'MARKER'                 'INTORG'
    vOpen[i1,j1]  OBJ       10
    vOpen[i1,j1]  logicOpenArc[i1,j1]  -10
    vOpen[i1,j2]  OBJ       30
    vOpen[i1,j2]  logicOpenArc[i1,j2]  -10
    vOpen[i1,j3]  OBJ       20
    vOpen[i1,j3]  logicOpenArc[i1,j3]  -10
    vOpen[i2,j1]  OBJ       10
    vOpen[i2,j1]  logicOpenArc[i2,j1]  -20
    vOpen[i2,j2]  OBJ       30
    vOpen[i2,j2]  logicOpenArc[i2,j2]  -30
    vOpen[i2,j3]  OBJ       20
    vOpen[i2,j3]  logicOpenArc[i2,j3]  -30
    vOpen[i3,j1]  OBJ       10
    vOpen[i3,j1]  logicOpenArc[i3,j1]  -20
    vOpen[i3,j2]  OBJ       30
    vOpen[i3,j2]  logicOpenArc[i3,j2]  -40
    vOpen[i3,j3]  OBJ       20
    vOpen[i3,j3]  logicOpenArc[i3,j3]  -30
    vOpen[i4,j1]  OBJ       10
    vOpen[i4,j1]  logicOpenArc[i4,j1]  -20
    vOpen[i4,j2]  OBJ       30
    vOpen[i4,j2]  logicOpenArc[i4,j2]  -20
    vOpen[i4,j3]  OBJ       20
    vOpen[i4,j3]  logicOpenArc[i4,j3]  -20
    MARKER    'MARKER'                 'INTEND'
RHS
    RHS1      capacity[i1]  10
    RHS1      capacity[i2]  30
    RHS1      capacity[i3]  40
    RHS1      capacity[i4]  20
    RHS1      demandSatisfaction[j1]  20
    RHS1      demandSatisfaction[j2]  50
    RHS1      demandSatisfaction[j3]  30
BOUNDS
 BV BND1      vOpen[i1,j1]
 BV BND1      vOpen[i1,j2]
 BV BND1      vOpen[i1,j3]
 BV BND1      vOpen[i2,j1]
 BV BND1      vOpen[i2,j2]
 BV BND1      vOpen[i2,j3]
 BV BND1      vOpen[i3,j1]
 BV BND1      vOpen[i3,j2]
 BV BND1      vOpen[i3,j3]
 BV BND1      vOpen[i4,j1]
 BV BND1      vOpen[i4,j2]
 BV BND1      vOpen[i4,j3]
ENDATA
