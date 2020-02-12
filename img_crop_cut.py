import os
import cv2
import numpy
import PIL

# 이미지 크롭

input_dir = "C:\\workspace_python\\Test_detector\\eyes_v5\\fake_noise\\"
input_list = os.listdir(input_dir)
# keep 폴더 내부 폴더명 가져오기 => keep 내부에 폴더가 없다면 관련 코드 지워도 됨
# print(folder_list)

output_dir = "C:\\workspace_python\\Test_detector\\eyes_v5\\fake_noise\\"
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# 옮길 데이터 하나씩 가져와서 이름 비교 후 replace
for input_name in input_list:
    img = cv2.imread(input_dir+input_name)
    print(input_dir+input_name)
    h, w, c = img.shape
    # print(h,w,c)
    crop_img = img[int(round(h / 8)):int(h - round(h / 8)), int(round(w / 8)):int(w - round(w / 8))]
    # crop_img = img[int(round(h/5)):int(round(h/2+h/9)), 0:int(w)]
    cv2.imwrite(output_dir+input_name, crop_img)