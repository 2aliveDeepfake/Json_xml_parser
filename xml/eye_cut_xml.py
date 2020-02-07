from xml.etree import ElementTree as ET
import os
import cv2

# 폴더 내 이미지 불러오기
xml_path = "before/"
xml_list = os.listdir(xml_path)

img_path = "eye_cut_after/"
img_list = os.listdir(img_path)

for xml_item, img_item in zip(xml_list, img_list):  # 폴더의 파일이름 얻기


    # 넓이, 높이, 찾기
    # width = root.findtext("size/width")
    # height = root.findtext("size/height")
    # print(width, height)

    img = cv2.imread(img_path + img_item)
    print(img_path + img_item)
    h, w, c = img.shape
    print(w, h, c)

    tree = ET.parse(xml_path + xml_item)
    # root = tree.getroot()

    x_size = ET.Element("size")
    x_width = ET.SubElement(x_size, "width")
    x_width.text = str(w)
    x_height = ET.SubElement(x_size, "height")
    x_height.text = str(h)

    tree.write("after/"+xml_item)