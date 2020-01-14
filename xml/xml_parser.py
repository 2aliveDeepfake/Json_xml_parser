from xml.etree.ElementTree import parse

tree = parse("alcymltoqb 09_0.xml")
root = tree.getroot()

folder = root.findtext("folder")
filename = root.findtext("filename")
path = root.findtext("path")
database = root.findtext("source").find("database")

width = root.findtext("size").find("width")
height = root.findtext("size").find("height")
depth = root.findtext("size").find("depth")
segmented = root.findtext("segmented")

print(folder, filename, path, database)
print(width, height, depth, segmented)
