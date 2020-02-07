import os
import shutil

# 기존에 분류를 진행해놓은 해놓은 대분류 폴더
folder_path = "../dataset/a_image/"
# stage 1~10 폴더명 가져오기
folder_list = os.listdir(folder_path)
# keep 폴더 내부 폴더명 가져오기 => keep 내부에 폴더가 없다면 관련 코드 지워도 됨

# 옮길 데이터가 있는 폴더
input_dir = "C:\\Users\\Ju\\Desktop\\a_image\\"
input_list = os.listdir(input_dir)

# 옮길 데이터 하나씩 가져와서 이름 비교 후 replace
for input_name in input_list:

    inputname, inputExtension = os.path.splitext(input_name)
    #print(inputname)

    for item in folder_list:  # 각 폴더 이름(hood_T)의 파일이름 얻기
        filename, fileExtension = os.path.splitext(item)
        #print('파일명 : ' + filename)
        if (filename == inputname):
            print(filename+","+inputname)
            #os.remove(input_dir+"\\"+item)
            os.remove(folder_path+item)
        # else:
        #     os.remove(folder_path+"\\"+item)
            #os.rename(input_dir+"\\"+item, folder_path+"\\"+item)
            #os.replace(input_dir+"\\"+item, folder_path+"\\"+item)