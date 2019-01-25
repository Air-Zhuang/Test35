import xml.dom.minidom

dom = xml.dom.minidom.parse('./file/LocList_cn.xml')
root = dom.documentElement
bb = root.getElementsByTagName('CountryRegion')
for i in bb:
    print(i.getAttribute("Name"))
    print(i.getAttribute("Code"))
