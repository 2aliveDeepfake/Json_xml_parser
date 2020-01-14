import json # import json module
import os
import shutil



# 크롭 완료한 폴더
# folder_path = "G:\\Facebook_Dataset\\"
folder_path = "D:\Facebook_Dataset_videos\\"
folder_list = os.listdir(folder_path)
for i in folder_list :
    i, inputExtension = os.path.splitext(i)
    # print(i)
    file_list = os.listdir(folder_path+i+"\\")
    #print(file_list)
    print(folder_path+i+"\\metadata.json")

    # 이동 하고 싶은 폴더에 json 파일 생성
    if file_list[0] == "metadata.json" :
        #print(file_list[1][16:18])
        shutil.copy(folder_path+i+"\\metadata.json", "G:\\Json_file\\metadata_"+str(file_list[1][16:18]+".json"))

    if file_list[1] == "metadata.json":
        #print(file_list[0][16:18])
        shutil.copy(folder_path+i+"\\metadata.json", "G:\\Json_file\\metadata_" + str(file_list[0][16:18]+".json"))


