import pandas as pd
#Read generator tables
folder_path = "data\\"

#Each scenario generator change this
folder_name = "Path 2000"
folder_parent = folder_path + folder_name + '\\'

file_name = "Scenario Map.xlsx"
file = folder_parent + file_name
sh = 'Generate Tables'
df_scenario_map = pd.read_excel(file, sheet_name = sh)
print(df_scenario_map.shape)
