from lxml import etree
import os
import cv2

# Data
folder_path = "./nose_img/"
folder_list = os.listdir(folder_path)
# print(folder_list)

for item in folder_list:  # 폴더의 파일이름 얻기
    # Create XML
    root = etree.Element("annotation")

    # Set name
    x_folder = etree.Element("folder")
    x_folder.text = "test"

    x_filename = etree.Element("filename")
    x_filename.text = item

    x_path = etree.Element("path")
    x_path.text = "C:\\tensorflow1\\models\\research\\object_detection\\images\\"+item

    # Set source
    x_source = etree.Element("source")
    x_database = etree.SubElement(x_source, "database")
    x_database.text = "Unknown"

    # Set size
    im = cv2.imread(folder_path+item)
    print(folder_path+item)
    height, width, depth = im.shape
    # print(width, height)
    x_size = etree.Element("size")
    x_width = etree.SubElement(x_size, "width")
    x_width.text = str(width)
    x_height = etree.SubElement(x_size, "height")
    x_height.text = str(height)
    x_depth = etree.SubElement(x_size, "depth")
    x_depth.text = str(depth)

    x_segmented = etree.Element("segmented")
    x_segmented.text = "0"

    x_object = etree.Element("object")
    x_name = etree.SubElement(x_object, "name")
    x_name.text = "nose_v5"
    x_pose = etree.SubElement(x_object, "pose")
    x_pose.text = "Unspecified"
    x_truncated = etree.SubElement(x_object, "truncated")
    x_truncated.text = "0"
    x_difficult = etree.SubElement(x_object, "difficult")
    x_difficult.text = "0"
    x_bndbox = etree.SubElement(x_object, "bndbox")

    x_xmin = etree.SubElement(x_bndbox, "xmin")
    x_xmin.text = "0"
    x_ymin = etree.SubElement(x_bndbox, "ymin")
    x_ymin.text = "0"
    x_xmax = etree.SubElement(x_bndbox, "xmax")
    x_xmax.text = str(width)
    x_ymax = etree.SubElement(x_bndbox, "ymax")
    x_ymax.text = str(height)

    # Append elements
    root.append(x_folder)
    root.append(x_filename)
    root.append(x_path)
    root.append(x_source)
    root.append(x_size)
    root.append(x_segmented)
    root.append(x_object)

    # Print
    # item.split('.')[0]
    x_output = etree.tostring(root, pretty_print=True, encoding='UTF-8')
    ff = open('./xml_after/'+item.split('.')[0]+".xml", 'w', encoding="utf-8")
    ff.write(x_output.decode('utf-8'))
