<map version="freeplane 1.6.0">
<!--To view this file, download free mind mapping software Freeplane from http://freeplane.sourceforge.net -->
<node TEXT="Scripts RFEP" FOLDED="false" ID="ID_313299805" CREATED="1631597182520" MODIFIED="1631597188695" STYLE="oval">
<font SIZE="18"/>
<hook NAME="MapStyle">
    <properties edgeColorConfiguration="#808080ff,#ff0000ff,#0000ffff,#00ff00ff,#ff00ffff,#00ffffff,#7c0000ff,#00007cff,#007c00ff,#7c007cff,#007c7cff,#7c7c00ff" fit_to_viewport="false" show_note_icons="true"/>

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node" STYLE="oval" UNIFORM_SHAPE="true" VGAP_QUANTITY="24.0 pt">
<font SIZE="24"/>
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="default" ICON_SIZE="12.0 pt" COLOR="#000000" STYLE="fork">
<font NAME="SansSerif" SIZE="10" BOLD="false" ITALIC="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.attributes">
<font SIZE="9"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.note" COLOR="#000000" BACKGROUND_COLOR="#ffffff" TEXT_ALIGN="LEFT"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="styles.topic" COLOR="#18898b" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subtopic" COLOR="#cc3300" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subsubtopic" COLOR="#669900">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.important">
<icon BUILTIN="yes"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#000000" STYLE="oval" SHAPE_HORIZONTAL_MARGIN="10.0 pt" SHAPE_VERTICAL_MARGIN="10.0 pt">
<font SIZE="18"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,1" COLOR="#0033ff">
<font SIZE="16"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,2" COLOR="#00b439">
<font SIZE="14"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,3" COLOR="#990000">
<font SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,4" COLOR="#111111">
<font SIZE="10"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,5"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,6"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,7"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,8"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,9"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,10"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,11"/>
</stylenode>
</stylenode>
</map_styles>
</hook>
<hook NAME="AutomaticEdgeColor" COUNTER="1" RULE="ON_BRANCH_CREATION"/>
<node TEXT="Scripts Documentation" POSITION="right" ID="ID_1392047158" CREATED="1626688060845" MODIFIED="1631597197716">
<edge COLOR="#ff0000"/>
<node TEXT="generate_scenario_map.py" FOLDED="true" ID="ID_1360068251" CREATED="1628065805682" MODIFIED="1631597598249">
<icon BUILTIN="button_ok"/>
<node TEXT="description" ID="ID_1965323838" CREATED="1628065841298" MODIFIED="1628065846700">
<node TEXT="generate automatically scenario map" ID="ID_113318847" CREATED="1628065846953" MODIFIED="1628065853362"/>
<node TEXT="export it to excel" ID="ID_105224601" CREATED="1628065857338" MODIFIED="1628065862299"/>
<node TEXT="the rules to generate the combination of factors are based on the toy scenario all factors" ID="ID_1207741135" CREATED="1628065862459" MODIFIED="1628065905309"/>
</node>
<node TEXT="input" ID="ID_1713901262" CREATED="1628482196330" MODIFIED="1628482197754"/>
<node TEXT="output" ID="ID_737622149" CREATED="1628482203174" MODIFIED="1628482204482"/>
</node>
<node TEXT="create_scenarios_from_generator" ID="ID_182593659" CREATED="1626688067093" MODIFIED="1627262235240">
<node TEXT="v1" FOLDED="true" ID="ID_1037982813" CREATED="1626739980460" MODIFIED="1627262235240">
<node TEXT="Path" ID="ID_846055190" CREATED="1626688086597" MODIFIED="1626688089332">
<node TEXT="C:\OneDrive - Deakin University\OD\calle test\Disun Applications\Gurobi Applications\models" ID="ID_832681424" CREATED="1626740006497" MODIFIED="1626740006497"/>
</node>
<node TEXT="Description" FOLDED="true" ID="ID_1777707866" CREATED="1626688089468" MODIFIED="1626745715972">
<node TEXT="It read csv generator tables and creates csv tables ready to feed the RFEP model" ID="ID_503664975" CREATED="1626740015117" MODIFIED="1626762272211"/>
<node TEXT="It only uses 2 factors to create scenarios" ID="ID_1730549514" CREATED="1626740054596" MODIFIED="1626762288018">
<node TEXT="paths" ID="ID_1536725625" CREATED="1626762277554" MODIFIED="1626762279561"/>
<node TEXT="types of vehicles" ID="ID_997632025" CREATED="1626762279708" MODIFIED="1626762282756"/>
</node>
<node TEXT="The variation of paths modifies all the rest of the tables for the RFEP" ID="ID_226501737" CREATED="1626740075765" MODIFIED="1626740095128">
<node TEXT="Directly" ID="ID_703419935" CREATED="1626740158701" MODIFIED="1626762299083">
<node TEXT="NodesPaths" ID="ID_1360392167" CREATED="1626740135541" MODIFIED="1626740142104"/>
<node TEXT="VehiclePaths" ID="ID_1695398415" CREATED="1626740146621" MODIFIED="1626740158120"/>
<node TEXT="NodesNodesPaths" ID="ID_784173505" CREATED="1626740563332" MODIFIED="1626740567135"/>
</node>
<node TEXT="Undirectly" ID="ID_399668406" CREATED="1626740254182" MODIFIED="1626762302831">
<node TEXT="MaeNodes" ID="ID_623952624" CREATED="1626740095796" MODIFIED="1626740127856">
<node TEXT="Less paths, likely less nodes" ID="ID_527046732" CREATED="1626740121621" MODIFIED="1626740411094"/>
</node>
<node TEXT="NodesNodes" ID="ID_970189550" CREATED="1626740305004" MODIFIED="1626740306744">
<node TEXT="Less paths, likely less nodes" ID="ID_1108322540" CREATED="1626740307094" MODIFIED="1626740414573"/>
</node>
<node TEXT="SubStations" ID="ID_262453969" CREATED="1626740284820" MODIFIED="1626740294008">
<node TEXT="Less paths, likely less stations" ID="ID_1290847956" CREATED="1626740294325" MODIFIED="1626740418030"/>
</node>
<node TEXT="MaeSuppliers" ID="ID_1545980658" CREATED="1626740270653" MODIFIED="1626740283713">
<node TEXT="Less stations, might reduce the suppliers in the network" ID="ID_940408784" CREATED="1626740286805" MODIFIED="1626740380131"/>
</node>
<node TEXT="SupplierRanges" ID="ID_1396921430" CREATED="1626740380741" MODIFIED="1626740445544">
<node TEXT="Less suppliers, then less suppliers ranges" ID="ID_849115504" CREATED="1626740445798" MODIFIED="1626740483361"/>
</node>
<node TEXT="MaeRanges" ID="ID_674823902" CREATED="1626740461509" MODIFIED="1626740488608">
<node TEXT="Less SuppliersRanges could reduce the number of ranges" ID="ID_897806318" CREATED="1626740488814" MODIFIED="1626740526072"/>
</node>
</node>
</node>
<node TEXT="The variation of vehicles, modify mae vehicles" ID="ID_1138102559" CREATED="1626740596621" MODIFIED="1626740608321"/>
</node>
<node TEXT="Input files" FOLDED="true" ID="ID_1583820777" CREATED="1626745728883" MODIFIED="1626745952709">
<node TEXT="data/toy instance" ID="ID_1824777257" CREATED="1626745910716" MODIFIED="1626746030996">
<node TEXT="Scenario Map Toy 1.xlsx" ID="ID_863571082" CREATED="1626745882785" MODIFIED="1626745882785" LINK="Disun%20Applications/Gurobi%20Applications/data/Scenario%20Map%20Toy%201.xlsx"/>
<node TEXT="Generator tables .csv" ID="ID_1973761006" CREATED="1626745737990" MODIFIED="1626745758107">
<node TEXT="VehiclesPaths.csv" ID="ID_141921224" CREATED="1626745776350" MODIFIED="1626745776350" LINK="Disun%20Applications/Gurobi%20Applications/data/Toy%20instance/VehiclesPaths.csv"/>
<node TEXT="MaeNodes.csv" ID="ID_1917585228" CREATED="1626745776372" MODIFIED="1626745776372" LINK="Disun%20Applications/Gurobi%20Applications/data/Toy%20instance/MaeNodes.csv"/>
<node TEXT="MaePaths.csv" ID="ID_838355208" CREATED="1626745776372" MODIFIED="1626745776372" LINK="Disun%20Applications/Gurobi%20Applications/data/Toy%20instance/MaePaths.csv"/>
<node TEXT="MaeRanges.csv" ID="ID_1305091445" CREATED="1626745776387" MODIFIED="1626745776387" LINK="Disun%20Applications/Gurobi%20Applications/data/Toy%20instance/MaeRanges.csv"/>
<node TEXT="MaeSuppliers.csv" ID="ID_601055671" CREATED="1626745776387" MODIFIED="1626745776387" LINK="Disun%20Applications/Gurobi%20Applications/data/Toy%20instance/MaeSuppliers.csv"/>
<node TEXT="MaeVehicles.csv" ID="ID_1520206688" CREATED="1626745776387" MODIFIED="1626745776387" LINK="Disun%20Applications/Gurobi%20Applications/data/Toy%20instance/MaeVehicles.csv"/>
<node TEXT="NodesNodes.csv" ID="ID_1797697709" CREATED="1626745776387" MODIFIED="1626745776387" LINK="Disun%20Applications/Gurobi%20Applications/data/Toy%20instance/NodesNodes.csv"/>
<node TEXT="NodesNodesPaths.csv" ID="ID_962838005" CREATED="1626745776387" MODIFIED="1626745776387" LINK="Disun%20Applications/Gurobi%20Applications/data/Toy%20instance/NodesNodesPaths.csv"/>
<node TEXT="NodesPaths.csv" ID="ID_785441518" CREATED="1626745776387" MODIFIED="1626745776387" LINK="Disun%20Applications/Gurobi%20Applications/data/Toy%20instance/NodesPaths.csv"/>
<node TEXT="SubStations.csv" ID="ID_388538232" CREATED="1626745776387" MODIFIED="1626745776387" LINK="Disun%20Applications/Gurobi%20Applications/data/Toy%20instance/SubStations.csv"/>
<node TEXT="SuppliersRanges.csv" ID="ID_1399649715" CREATED="1626745776387" MODIFIED="1626745776387" LINK="Disun%20Applications/Gurobi%20Applications/data/Toy%20instance/SuppliersRanges.csv"/>
</node>
</node>
</node>
<node TEXT="Pseudocode" FOLDED="true" ID="ID_609608522" CREATED="1626744738622" MODIFIED="1626744743273">
<node TEXT="Read generator tables" ID="ID_592026054" CREATED="1626744744080" MODIFIED="1626744754937"/>
<node TEXT="Read scenario map" ID="ID_987514685" CREATED="1626744756550" MODIFIED="1626744760705">
<node TEXT="It is an excel file that presents the tables defintion of each scenario" ID="ID_952550497" CREATED="1626744762198" MODIFIED="1626744780416"/>
<node TEXT="There are multiple scenarios that share same tables, therefore I use this common factor to only generate &quot;unique&quot; tables" ID="ID_1846424286" CREATED="1626744780686" MODIFIED="1626744949161"/>
<node TEXT="There could be repeated tables depending on the data" ID="ID_1327828674" CREATED="1626744950934" MODIFIED="1626744982559"/>
</node>
<node TEXT="Read levels of factors" ID="ID_868838812" CREATED="1626744996510" MODIFIED="1626745001033">
<node TEXT="I read the different levels I want to give to the factors" ID="ID_202214925" CREATED="1626745001287" MODIFIED="1627262281166">
<node TEXT="The size of the set of types of vehicles and paths, in this case" ID="ID_1057667333" CREATED="1626745021092" MODIFIED="1626745036114"/>
</node>
</node>
<node TEXT="Create generated tables" ID="ID_1050245438" CREATED="1626745241462" MODIFIED="1626831497759">
<node TEXT="Tables that depends on the level of vehicles" ID="ID_90908173" CREATED="1626745252441" MODIFIED="1626745269288">
<node TEXT="MaeVehicles" ID="ID_514090819" CREATED="1626763791934" MODIFIED="1626763799418"/>
</node>
<node TEXT="Tables that depends on the level of paths" ID="ID_26057535" CREATED="1626745269423" MODIFIED="1626745289593">
<node TEXT="NodesPaths" ID="ID_448846977" CREATED="1626740135541" MODIFIED="1626740142104"/>
<node TEXT="NodesNodesPaths" ID="ID_87176883" CREATED="1626740563332" MODIFIED="1626740567135"/>
<node TEXT="MaeNodes" ID="ID_1934711317" CREATED="1626740095796" MODIFIED="1626740127856">
<node TEXT="Less paths, likely less nodes" ID="ID_1460858280" CREATED="1626740121621" MODIFIED="1626740411094"/>
</node>
<node TEXT="NodesNodes" ID="ID_185161507" CREATED="1626740305004" MODIFIED="1626740306744">
<node TEXT="Less paths, likely less nodes" ID="ID_1452171813" CREATED="1626740307094" MODIFIED="1626740414573"/>
</node>
<node TEXT="SubStations" ID="ID_921757158" CREATED="1626740284820" MODIFIED="1626740294008">
<node TEXT="Less paths, likely less stations" ID="ID_893329969" CREATED="1626740294325" MODIFIED="1626740418030"/>
</node>
<node TEXT="MaeSuppliers" ID="ID_438026812" CREATED="1626740270653" MODIFIED="1626740283713">
<node TEXT="Less stations, might reduce the suppliers in the network" ID="ID_1497310607" CREATED="1626740286805" MODIFIED="1626740380131"/>
</node>
<node TEXT="SupplierRanges" ID="ID_1038549680" CREATED="1626740380741" MODIFIED="1626740445544">
<node TEXT="Less suppliers, then less suppliers ranges" ID="ID_795745131" CREATED="1626740445798" MODIFIED="1626740483361"/>
</node>
<node TEXT="MaeRanges" ID="ID_764698352" CREATED="1626740461509" MODIFIED="1626740488608">
<node TEXT="Less SuppliersRanges could reduce the number of ranges" ID="ID_273077943" CREATED="1626740488814" MODIFIED="1626740526072"/>
</node>
</node>
<node TEXT="Tables that depends on the variation of both: vehicles and paths" ID="ID_313052305" CREATED="1626745289790" MODIFIED="1626745307370">
<node TEXT="VehiclesPaths" ID="ID_1962527682" CREATED="1626763801043" MODIFIED="1626763943214"/>
</node>
</node>
</node>
<node TEXT="outputfiles" ID="ID_1461590653" CREATED="1626745900469" MODIFIED="1626745903593">
<node TEXT="data/toy instance/Generated tables" ID="ID_1542652675" CREATED="1626746055641" MODIFIED="1626746066561">
<node TEXT="All tables required to build each scenario" ID="ID_531730371" CREATED="1626746070776" MODIFIED="1626746081189"/>
</node>
</node>
<node TEXT="Tricks" FOLDED="true" ID="ID_71346180" CREATED="1626745454508" MODIFIED="1626745455918">
<node TEXT="I read all tables in a for and I used a dictionary to store all dataframes of the generator tables, in which the key is the name of the table" ID="ID_275464919" CREATED="1626745522075" MODIFIED="1626763746533"/>
<node TEXT="I use pd.merge to filter tables" ID="ID_1240559062" CREATED="1626745456168" MODIFIED="1626745469766">
<node TEXT="df_nodes_nodes = pd.merge(df_table[&quot;NodesNodes&quot;], df_mae_nodes, left_on= &quot;COD_NODE2&quot;, right_on = &quot;COD_NODE&quot;, how=&quot;inner&quot;)" ID="ID_1492075841" CREATED="1626745471070" MODIFIED="1626745507685"/>
</node>
<node TEXT="export tables" ID="ID_515389292" CREATED="1626745560135" MODIFIED="1626745564539">
<node TEXT="DataFrameName.to_csv(export_string, index=False)" ID="ID_208477477" CREATED="1626745564809" MODIFIED="1626745589373"/>
<node TEXT="The export_string is the string that defines the path and the name of the file" ID="ID_1837364453" CREATED="1626745589595" MODIFIED="1626745617307"/>
</node>
</node>
</node>
<node TEXT="v2" FOLDED="true" ID="ID_1325798441" CREATED="1627533216452" MODIFIED="1631597486066"><richcontent TYPE="NOTE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      This is the currently implemented version
    </p>
  </body>
</html>

</richcontent>
<node TEXT="Description" ID="ID_461428804" CREATED="1627533218251" MODIFIED="1627533222270">
<node TEXT="Incorporates all factors to generate scenarios" ID="ID_1150793846" CREATED="1627533222517" MODIFIED="1627533230567"/>
</node>
<node TEXT="Pseudocode" FOLDED="true" ID="ID_729152486" CREATED="1628482233467" MODIFIED="1628482235527">
<node TEXT="Table generation" ID="ID_282420319" CREATED="1628482908838" MODIFIED="1628482912150">
<node TEXT="Create function to export tables" FOLDED="true" ID="ID_1853520939" CREATED="1628482253646" MODIFIED="1628482266658">
<node TEXT="MaeSuppliers" ID="ID_885790166" CREATED="1628482266893" MODIFIED="1628482293052"/>
<node TEXT="SuppliersRanges" ID="ID_1129544215" CREATED="1628482273177" MODIFIED="1628482282215"/>
<node TEXT="SubStations" ID="ID_501423413" CREATED="1628482283292" MODIFIED="1628482285748"/>
</node>
<node TEXT="Read generator tables" ID="ID_138654248" CREATED="1626744744080" MODIFIED="1626744754937"/>
<node TEXT="Read generation parameters" FOLDED="true" ID="ID_1169087584" CREATED="1628482348662" MODIFIED="1628482352653">
<node TEXT="There are some parameters that the alforithm use to generate scenarios" ID="ID_384136483" CREATED="1628482352891" MODIFIED="1628482368019"/>
<node TEXT="Example" ID="ID_221468554" CREATED="1628482424104" MODIFIED="1628482425799">
<node TEXT="capacity_cost" ID="ID_1034103230" CREATED="1628482426285" MODIFIED="1628482430628">
<node TEXT="This parameter is used to create the costs associated to the capacity of the stations" ID="ID_1274396415" CREATED="1628482430876" MODIFIED="1628482448255"/>
</node>
</node>
</node>
<node TEXT="Read scenario map" ID="ID_391727214" CREATED="1626744756550" MODIFIED="1626744760705">
<node TEXT="It is an excel file that presents the tables defintion of each scenario" ID="ID_1413579698" CREATED="1626744762198" MODIFIED="1626744780416"/>
<node TEXT="There are multiple scenarios that share same tables, therefore I use this common factor to only generate &quot;unique&quot; tables" ID="ID_578260520" CREATED="1626744780686" MODIFIED="1626744949161"/>
<node TEXT="There could be repeated tables depending on the data" ID="ID_1873657573" CREATED="1626744950934" MODIFIED="1626744982559"/>
</node>
<node TEXT="Read levels of factors" ID="ID_1176402216" CREATED="1626744996510" MODIFIED="1626745001033">
<node TEXT="I read the different levels I want to give to the factors" ID="ID_611511135" CREATED="1626745001287" MODIFIED="1627262281166"/>
</node>
<node TEXT="Read valid combinations own stations * candidate locations" FOLDED="true" ID="ID_1550791942" CREATED="1628482520673" MODIFIED="1628482532215">
<node TEXT="There are some combinations of these two factor which are not valid. But this is defined in scenario map. So I make use of it" ID="ID_609825367" CREATED="1628482532469" MODIFIED="1628482558004"/>
</node>
<node TEXT="Define survivor supplier" ID="ID_461429048" CREATED="1628482566927" MODIFIED="1628482572824"/>
<node TEXT="Create generated tables" FOLDED="true" ID="ID_1674124772" CREATED="1626745241462" MODIFIED="1626831497759">
<node TEXT="Tables that depends on the level of vehicles" ID="ID_967959925" CREATED="1626745252441" MODIFIED="1626745269288">
<node TEXT="MaeVehicles" ID="ID_1214161828" CREATED="1626763791934" MODIFIED="1626763799418"/>
</node>
<node TEXT="Tables that depends on the level of paths" ID="ID_961284889" CREATED="1626745269423" MODIFIED="1626745289593">
<node TEXT="NodesPaths" ID="ID_1002231025" CREATED="1626740135541" MODIFIED="1626740142104"/>
<node TEXT="NodesNodesPaths" ID="ID_1090743849" CREATED="1626740563332" MODIFIED="1626740567135"/>
<node TEXT="MaeNodes" ID="ID_122927250" CREATED="1626740095796" MODIFIED="1626740127856">
<node TEXT="Less paths, likely less nodes" ID="ID_1856157906" CREATED="1626740121621" MODIFIED="1626740411094"/>
</node>
<node TEXT="NodesNodes" ID="ID_1829191544" CREATED="1626740305004" MODIFIED="1626740306744">
<node TEXT="Less paths, likely less nodes" ID="ID_634258965" CREATED="1626740307094" MODIFIED="1626740414573"/>
</node>
<node TEXT="Tables that depend on" ID="ID_922996083" CREATED="1628482631247" MODIFIED="1628482641906">
<node TEXT="factors" FOLDED="true" ID="ID_1221117881" CREATED="1628482682195" MODIFIED="1628482683497">
<node TEXT="suppliers" ID="ID_1121155888" CREATED="1628482642447" MODIFIED="1628482724103">
<icon BUILTIN="flag-yellow"/>
</node>
<node TEXT="Quantity own stations" ID="ID_1320098048" CREATED="1628482646867" MODIFIED="1628482733643">
<icon BUILTIN="flag-green"/>
</node>
<node TEXT="candidate locations" ID="ID_1430390524" CREATED="1628482665712" MODIFIED="1628482736097">
<icon BUILTIN="flag-pink"/>
</node>
</node>
<node TEXT="tables" FOLDED="true" ID="ID_266418180" CREATED="1628482691310" MODIFIED="1628482692250">
<node TEXT="SubStations" FOLDED="true" ID="ID_168706580" CREATED="1626740284820" MODIFIED="1628482742378">
<icon BUILTIN="flag-yellow"/>
<icon BUILTIN="flag-green"/>
<icon BUILTIN="flag-pink"/>
<node TEXT="Less paths, likely less stations" ID="ID_1300471756" CREATED="1626740294325" MODIFIED="1626740418030"/>
</node>
<node TEXT="SupplierRanges" FOLDED="true" ID="ID_25884035" CREATED="1626740380741" MODIFIED="1628482729730">
<icon BUILTIN="flag-yellow"/>
<node TEXT="Less suppliers, then less suppliers ranges" ID="ID_1879608955" CREATED="1626740445798" MODIFIED="1626740483361"/>
</node>
<node TEXT="MaeSuppliers" ID="ID_1841238536" CREATED="1626740270653" MODIFIED="1628482729730">
<icon BUILTIN="flag-yellow"/>
<node TEXT="Less stations, might reduce the suppliers in the network" ID="ID_780856500" CREATED="1626740286805" MODIFIED="1626740380131"/>
</node>
</node>
</node>
<node TEXT="MaeRanges" ID="ID_1846695716" CREATED="1626740461509" MODIFIED="1626740488608">
<node TEXT="Less SuppliersRanges could reduce the number of ranges" ID="ID_152360300" CREATED="1626740488814" MODIFIED="1626740526072"/>
</node>
</node>
<node TEXT="Check feasibility of vehicles_paths" ID="ID_1951884130" CREATED="1628482779652" MODIFIED="1628482795775"/>
<node TEXT="Tables that depends on the variation of both: vehicles and paths" ID="ID_291417362" CREATED="1626745289790" MODIFIED="1626745307370">
<node TEXT="VehiclesPaths" ID="ID_917577602" CREATED="1626763801043" MODIFIED="1626763943214"/>
</node>
</node>
</node>
<node TEXT="Parameter calculation" ID="ID_501953257" CREATED="1628482920701" MODIFIED="1628482924455">
<node TEXT="Iterate for each scenario" FOLDED="true" ID="ID_364051379" CREATED="1628483060883" MODIFIED="1628483066639">
<node TEXT="Read tables for each scenario" ID="ID_1543620514" CREATED="1628483022549" MODIFIED="1628743774821"/>
<node TEXT="Create data model for the RFEP" ID="ID_1921777549" CREATED="1628483067570" MODIFIED="1628483073983"/>
<node TEXT="Increase price in own stations" ID="ID_10684533" CREATED="1628483086712" MODIFIED="1628483092791"/>
<node TEXT="Solve each FRVRP associated to the RFEP" ID="ID_120459870" CREATED="1628483094294" MODIFIED="1628483116446"/>
<node TEXT="Define Min Refuelling Qty" ID="ID_282422713" CREATED="1628483142249" MODIFIED="1628483151310"/>
<node TEXT="Update MaeSuppliers" ID="ID_1327601160" CREATED="1628483294374" MODIFIED="1628483300017"/>
<node TEXT="Define lower quantity discount" ID="ID_1550518076" CREATED="1628483151470" MODIFIED="1628483165574"/>
<node TEXT="Define upper quantity discount" ID="ID_256138433" CREATED="1628483165775" MODIFIED="1628483173138"/>
<node TEXT="Update SuppliersRanges" ID="ID_1000329857" CREATED="1628483301166" MODIFIED="1628483307781"/>
<node TEXT="Define station capacity" ID="ID_292008077" CREATED="1628483415876" MODIFIED="1628483421761"/>
<node TEXT="Define location cost" ID="ID_271405814" CREATED="1628483421915" MODIFIED="1628483425860"/>
<node TEXT="Define station unit capacity" ID="ID_1909046038" CREATED="1628483426030" MODIFIED="1628483432409"/>
<node TEXT="Define cost unit capacity" ID="ID_1051733479" CREATED="1628483432559" MODIFIED="1628483439105"/>
<node TEXT="Update SubStation" ID="ID_1416078093" CREATED="1628483439974" MODIFIED="1628743786916"/>
</node>
</node>
</node>
<node TEXT="input files" ID="ID_71499833" CREATED="1628482417461" MODIFIED="1628482420315">
<node TEXT="Generation parameters.xlsx" ID="ID_1263001567" CREATED="1628482420558" MODIFIED="1628482421529"/>
<node TEXT="Scenario Map.xlsx" ID="ID_1815819690" CREATED="1628482462892" MODIFIED="1628482463809"/>
</node>
<node TEXT="input modules" FOLDED="true" ID="ID_427622098" CREATED="1628483000710" MODIFIED="1628483004330">
<node TEXT="read_data_rfep" ID="ID_233862635" CREATED="1628483006327" MODIFIED="1628483011110"/>
</node>
</node>
</node>
<node TEXT="read_data_rfep_function" FOLDED="true" ID="ID_1355920329" CREATED="1626861821941" MODIFIED="1626862009282">
<node TEXT="Path" ID="ID_1464798408" CREATED="1626861834068" MODIFIED="1626861836414">
<node TEXT="C:\OneDrive - Deakin University\OD\calle test\Disun Applications\Gurobi Applications\models" ID="ID_677978778" CREATED="1626862014942" MODIFIED="1626862015367"/>
</node>
<node TEXT="Arguments" ID="ID_1369311086" CREATED="1626861843324" MODIFIED="1626861845270">
<node TEXT="Tables of an instance of the rfep" ID="ID_669904557" CREATED="1626861846605" MODIFIED="1626861858118"/>
</node>
<node TEXT="Outputs" ID="ID_787583187" CREATED="1626861845437" MODIFIED="1626861860686">
<node TEXT="data elements of the rfep" ID="ID_888550727" CREATED="1626861861940" MODIFIED="1626861875446">
<node TEXT="sets" ID="ID_1852828282" CREATED="1626861875669" MODIFIED="1626861877472"/>
<node TEXT="parameters" ID="ID_1355946165" CREATED="1626861877637" MODIFIED="1626861879544"/>
</node>
</node>
<node TEXT="Tricks" ID="ID_435967802" CREATED="1626861881053" MODIFIED="1626861882622">
<node TEXT="I read most of the input as a dictionary" ID="ID_87404870" CREATED="1626861883021" MODIFIED="1626861989294"/>
<node TEXT="I output a tuple with a dictionary wit all the values so that I can use it without having to map the numbers as was my previous approach" ID="ID_52698342" CREATED="1626861892285" MODIFIED="1626861934175"/>
</node>
</node>
<node TEXT="export_solution_rfep.py" ID="ID_190065034" CREATED="1631597574924" MODIFIED="1631597589643">
<icon BUILTIN="bookmark"/>
</node>
<node TEXT="run_multiple_scenarios_independent_subproblems" ID="ID_1290267351" CREATED="1631598971966" MODIFIED="1631599925386">
<icon BUILTIN="bookmark"/>
</node>
<node TEXT="run_multiple_scenarios.py" FOLDED="true" ID="ID_1946383594" CREATED="1627864545939" MODIFIED="1627864554935">
<node TEXT="Path" ID="ID_1202149780" CREATED="1627864555188" MODIFIED="1627864573142">
<node TEXT="C:\OneDrive - Deakin University\OD\calle test\Disun Applications\Gurobi Applications\models" ID="ID_1429783922" CREATED="1626740006497" MODIFIED="1626740006497"/>
</node>
<node TEXT="Description" ID="ID_69895097" CREATED="1627864573291" MODIFIED="1627864575326">
<node TEXT="it receives the scenario map and a folder to read the tables" ID="ID_267224432" CREATED="1627864610068" MODIFIED="1627864637845"/>
<node TEXT="It automatically knows how to create each scenario based on the scenario map information" ID="ID_418027461" CREATED="1627864638528" MODIFIED="1627864656730"/>
<node TEXT="Solve all scenarios and export the results to Excel" ID="ID_740613906" CREATED="1627864671762" MODIFIED="1627864681054"/>
</node>
<node TEXT="input files" ID="ID_1135860688" CREATED="1627864593996" MODIFIED="1627865173904">
<node TEXT="Scenario Map Toy 1.xlsx" ID="ID_483083209" CREATED="1627864694628" MODIFIED="1627864694628"/>
<node TEXT="All Generated tables" ID="ID_737326731" CREATED="1627864682249" MODIFIED="1627865173904"/>
</node>
<node TEXT="Modules" ID="ID_1241626313" CREATED="1627864575467" MODIFIED="1627864582831">
<node TEXT="read_data_rfep_function" ID="ID_803543340" CREATED="1627864719788" MODIFIED="1627864731358"/>
<node TEXT="rfep_model" ID="ID_745058291" CREATED="1627864732075" MODIFIED="1627864737543"/>
<node TEXT="export_solution_rfep" ID="ID_1363007781" CREATED="1627864737907" MODIFIED="1627864744822"/>
<node TEXT="time" ID="ID_1253301412" CREATED="1627864746880" MODIFIED="1627864747623"/>
</node>
<node TEXT="Pseudocode" ID="ID_1276558096" CREATED="1627864584883" MODIFIED="1627864587439">
<node TEXT="Save tables names in string list" ID="ID_1141020235" CREATED="1627864749555" MODIFIED="1627864766471"/>
<node TEXT="Read scenario" ID="ID_1914399649" CREATED="1627864768869" MODIFIED="1631597107038"/>
<node TEXT="For each scenario" ID="ID_1534747312" CREATED="1627864785302" MODIFIED="1627864791106">
<node TEXT="track the solution time" ID="ID_1561979698" CREATED="1627864792990" MODIFIED="1627864800931"/>
<node TEXT="Read tables name associated to each scenario" ID="ID_987362788" CREATED="1627864882768" MODIFIED="1627864897725">
<node TEXT="I do a concatenation of tables names and scenario codes of tables present in scenario map" ID="ID_513243257" CREATED="1627864898460" MODIFIED="1627864927921"/>
</node>
<node TEXT="Read tables of the scenario and build the model elements" ID="ID_150015853" CREATED="1627864801088" MODIFIED="1627864849288">
<node TEXT="use function read_data_rfep_function" ID="ID_1961423125" CREATED="1627864850239" MODIFIED="1627864861114"/>
</node>
<node TEXT="Solve rfep and save the solution" ID="ID_73509241" CREATED="1627864862886" MODIFIED="1627864972270">
<node TEXT="use rfep_model" ID="ID_483683942" CREATED="1627864972915" MODIFIED="1627864976870"/>
<node TEXT="the data comes straight from the function read_data_rfep" ID="ID_814920970" CREATED="1627864979787" MODIFIED="1627865005698"/>
</node>
<node TEXT="export the output" ID="ID_571582642" CREATED="1627865006868" MODIFIED="1631597155623">
<node TEXT="use the function export_solution_rfep" ID="ID_1571197929" CREATED="1627865018621" MODIFIED="1627865031100"/>
</node>
</node>
</node>
<node TEXT="output files" ID="ID_891535853" CREATED="1627864587611" MODIFIED="1627864592739"/>
<node TEXT="tricks" ID="ID_14504480" CREATED="1627864598507" MODIFIED="1627864599807"/>
</node>
<node TEXT="reduce_stations_path" ID="ID_1372359086" CREATED="1631597822398" MODIFIED="1631598035297">
<icon BUILTIN="bookmark"/>
<node TEXT="Description" ID="ID_1749658694" CREATED="1631597937269" MODIFIED="1631597939862">
<node TEXT="Source script" ID="ID_1788215703" CREATED="1631597940117" MODIFIED="1631598014241" LINK="#ID_9084057"/>
</node>
</node>
<node TEXT="rfep_as_x_frvrp" ID="ID_476276516" CREATED="1631599250582" MODIFIED="1631599925386">
<icon BUILTIN="revision-red"/>
<icon BUILTIN="bookmark"/>
<node TEXT="Description" ID="ID_1629985021" CREATED="1631599266087" MODIFIED="1631599268487"/>
</node>
<node TEXT="solve_multiple_frvrp.py" FOLDED="true" ID="ID_1738562142" CREATED="1631599269423" MODIFIED="1631599925385">
<icon BUILTIN="revision-red"/>
<icon BUILTIN="bookmark"/>
<node TEXT="Descirption" ID="ID_1852646360" CREATED="1627263119937" MODIFIED="1627263122371">
<node TEXT="function that solves the frvrp multiple times (one for each vehicle path combination)" ID="ID_449093086" CREATED="1627263126529" MODIFIED="1627263151403"/>
</node>
<node TEXT="Input" ID="ID_1044142189" CREATED="1627262946747" MODIFIED="1627262947945">
<node TEXT="Sets and parameters of the FRVRP" ID="ID_1107227771" CREATED="1627262951145" MODIFIED="1627262960922"/>
</node>
<node TEXT="Output" ID="ID_1494560057" CREATED="1627262948168" MODIFIED="1627262949891">
<node TEXT="a dictionary of one component" ID="ID_361420239" CREATED="1627262961805" MODIFIED="1627263038978"/>
<node TEXT="The dictionary stores the solution of each subproblem" ID="ID_1471242820" CREATED="1627263039601" MODIFIED="1627263046852"/>
</node>
</node>
<node TEXT="run_multiple_scenarios_domain_reduction.py" ID="ID_596442517" CREATED="1631865961322" MODIFIED="1631865978264">
<icon BUILTIN="bookmark"/>
</node>
<node TEXT="test" FOLDED="true" ID="ID_10627433" CREATED="1631599969517" MODIFIED="1631599970605">
<node TEXT="RFEP Subproblems domain reduction.py" ID="ID_9084057" CREATED="1624841164127" MODIFIED="1631597984370" LINK="#ID_1788215703">
<node TEXT="Description" ID="ID_1629859640" CREATED="1625119718230" MODIFIED="1625119722663">
<node TEXT="Implements the domain reduction algortihm that eliminates not promising stations from path" ID="ID_681138163" CREATED="1625119722967" MODIFIED="1625119754776"/>
<node TEXT="It solves the complete model with the domain reduction and without the domain reduction and exports the results to Excel for analysis" ID="ID_1046615443" CREATED="1625119754950" MODIFIED="1625119782849"/>
<node TEXT="This script was the base to build the function reduce_stations_path" ID="ID_1116419467" CREATED="1631597916646" MODIFIED="1631597931439"/>
</node>
<node TEXT="auxiliaries file" ID="ID_797798512" CREATED="1625119581005" MODIFIED="1625119596982">
<node TEXT="input file" ID="ID_967761004" CREATED="1625119630885" MODIFIED="1625119649782">
<node TEXT="Data Model Generated Network-12.xlsx" ID="ID_1457435519" CREATED="1625119597597" MODIFIED="1625119630119"/>
</node>
<node TEXT="output file" ID="ID_1308095792" CREATED="1625119637285" MODIFIED="1625119646991">
<node TEXT="outputRFEPSubproblem_v1.xlsx" ID="ID_1626709539" CREATED="1625119609900" MODIFIED="1625119626679"/>
</node>
</node>
<node TEXT="modules required" ID="ID_1620922438" CREATED="1625119263071" MODIFIED="1625119270626">
<node TEXT="export_solution_rfep" ID="ID_1517864008" CREATED="1624841149104" MODIFIED="1624841155643"/>
<node TEXT="read_data_rfep" ID="ID_569838335" CREATED="1624841157176" MODIFIED="1624841163961"/>
<node TEXT="rfep_model.py" ID="ID_45446311" CREATED="1624841191175" MODIFIED="1624844828858"/>
</node>
<node TEXT="Pseudocode" FOLDED="true" ID="ID_137439895" CREATED="1625119310792" MODIFIED="1625119327882">
<node TEXT="Read data" ID="ID_1120711278" CREATED="1624844861057" MODIFIED="1624844865691"/>
<node TEXT="Enters a loop to solve subproblems" ID="ID_117939745" CREATED="1624844865873" MODIFIED="1624845081762">
<node TEXT="Reduce the domain of each subproblem" ID="ID_387867406" CREATED="1624844984713" MODIFIED="1624845081762"/>
<node TEXT="Updates the sets and required parameters (distance and fuel consumption in segments)" ID="ID_282290175" CREATED="1625119338377" MODIFIED="1625119362947"/>
</node>
<node TEXT="Solve the complete RFEP after domain reduction" ID="ID_1216384230" CREATED="1624844999570" MODIFIED="1624845011035"/>
<node TEXT="Exports the solution of the RFEP after domain reduction" ID="ID_1637851324" CREATED="1624845023188" MODIFIED="1624845066930"/>
<node TEXT="Solve the RFEP without domain reduction" ID="ID_180007352" CREATED="1624845011193" MODIFIED="1624845020251"/>
<node TEXT="Export the solution of the RFEP" ID="ID_1296445085" CREATED="1624845051476" MODIFIED="1624845078143"/>
</node>
</node>
<node TEXT="rfep_test_domain_reduction" FOLDED="true" ID="ID_640897636" CREATED="1625716494714" MODIFIED="1625724363397">
<node TEXT="Description" ID="ID_1330038573" CREATED="1625716502890" MODIFIED="1625716506462">
<node TEXT="Test the domain reduction function" ID="ID_1871238270" CREATED="1625716507018" MODIFIED="1625716519873"/>
</node>
<node TEXT="auxiliaries file" ID="ID_801957444" CREATED="1625119581005" MODIFIED="1625119596982">
<node TEXT="input file" ID="ID_299398965" CREATED="1625119630885" MODIFIED="1625119649782">
<node TEXT="Data Model Generated Network-12.xlsx" ID="ID_1500743585" CREATED="1625119597597" MODIFIED="1625119630119"/>
</node>
<node TEXT="output file" ID="ID_656198117" CREATED="1625119637285" MODIFIED="1625119646991">
<node TEXT="outputRFEPSubproblem_v1.xlsx" ID="ID_1624392734" CREATED="1625119609900" MODIFIED="1625119626679"/>
</node>
</node>
<node TEXT="modules required" ID="ID_1232622578" CREATED="1625119263071" MODIFIED="1625119270626">
<node TEXT="export_solution_rfep.py" ID="ID_1777014031" CREATED="1624841149104" MODIFIED="1625716703251"/>
<node TEXT="read_data_rfep.py" ID="ID_1829341850" CREATED="1624841157176" MODIFIED="1625716701060"/>
<node TEXT="rfep_model.py" ID="ID_182858388" CREATED="1624841191175" MODIFIED="1624844828858"/>
<node TEXT="reduce_stations_path.py" ID="ID_145925961" CREATED="1625716623814" MODIFIED="1625716695188">
<node TEXT="Implement the domain reduction procedure" ID="ID_1161113343" CREATED="1625716722479" MODIFIED="1625716733198"/>
</node>
</node>
<node TEXT="Pseudocode" ID="ID_1423829741" CREATED="1625717892107" MODIFIED="1631865128490">
<node TEXT="import data" ID="ID_350311615" CREATED="1625717895468" MODIFIED="1625717898331"/>
<node TEXT="call domain reduction" ID="ID_1404858839" CREATED="1625717898491" MODIFIED="1625717907342"/>
<node TEXT="call problem solve" ID="ID_379582433" CREATED="1625717907490" MODIFIED="1625717914843"/>
<node TEXT="print results" ID="ID_661335411" CREATED="1625717915002" MODIFIED="1625717917901"/>
</node>
</node>
</node>
</node>
</node>
</map>
