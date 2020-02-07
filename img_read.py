import os
import cv2
import numpy
import PIL

input_dir = "img\\"
input_list = os.listdir(input_dir)
# keep 폴더 내부 폴더명 가져오기 => keep 내부에 폴더가 없다면 관련 코드 지워도 됨
# print(folder_list)

# 옮길 데이터 하나씩 가져와서 이름 비교 후 replace
for input_name in input_list:
    name = input_name[0:10]
    print(name)