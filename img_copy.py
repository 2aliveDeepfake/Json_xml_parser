import os
import shutil

# 크롭 완료한 폴더
folder_path = "G:\\main_original_crop_glasses\\"
folder_list = os.listdir(folder_path)
# keep 폴더 내부 폴더명 가져오기 => keep 내부에 폴더가 없다면 관련 코드 지워도 됨
# print(folder_list)

# 크롭 안된 폴더
input_dir = "G:\\main_original_01\\"
input_list = os.listdir(input_dir)
# print(input_list)

# 옮길 데이터 하나씩 가져와서 이름 비교 후 replace
for input_name in input_list:
    inputname, inputExtension = os.path.splitext(input_name)
    inputname = inputname[0:15]
    print("크롭 안된 : "+ inputname)

    for item in folder_list:  # 각 폴더 이름(hood_T)의 파일이름 얻기
        filename, fileExtension = os.path.splitext(item)
        filename= filename[0:15]
        print("크롭된 : " + filename)
        if (filename == inputname):
            print(filename+","+inputname)
            # print(input_dir+input_name)
            # print("G:\\DFDC_img\\dfdc_train_part_04\\dfdc_train_04_fake_done\\"+input_name)
            shutil.copy(input_dir+input_name, "G:\\margin_glasses\\"+input_name)
            # if not os.path.isfile(input_dir+input_name):
            #     print("already moved")