from lxml import etree
import os
import cv2

# Data
folder_path = "./xml_before/"
folder_list = os.listdir(folder_path)
# print(folder_list)

for item in folder_list:  # 폴더의 파일이름 얻기
    # Create XML
    root = etree.Element("annotation")

    x_object = etree.Element("object")
    x_name = etree.SubElement(x_object, "name")
    x_name.text = "nose_v5"

    root.append(x_object)

    # Print
    # item.split('.')[0]
    x_output = etree.tostring(root, pretty_print=True, encoding='UTF-8')
    print(str('./xml_after/'+item.split('.')[0]+".xml"))
    ff = open('./xml_after/'+item.split('.')[0]+".xml", 'w', encoding="utf-8")
    ff.write(x_output.decode('utf-8'))
