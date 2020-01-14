import xml.etree.ElementTree as ET
import os

# 폴더 내 이미지 불러오기
folder_path = "before/"
folder_list = os.listdir(folder_path)

for item in folder_list:  # 폴더의 파일이름 얻기

    tree = ET.parse(folder_path+item)
    root = tree.getroot()
    element = root[1] #get first child of root element
    element.text = "f_"+element.text
    print(element.text)
    tree.write("after/"+element.text+".xml")