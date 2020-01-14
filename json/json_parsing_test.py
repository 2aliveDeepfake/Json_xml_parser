import json # import json module
import os
import shutil


folder_path = "metadata_14"
#folder_list = os.listdir(folder_path)
# for i in folder_list :
#     i, inputExtension = os.path.splitext(i)
#     #print(i+".json")
#     print("\n"+i+"\n")
with open(folder_path+".json") as json_file:
    json_data = str(json.load(json_file))
    #json_string = json_data["json_string"]
    #print(json_data)
    comma= json_data.replace("},","},\n")
    print(comma)


