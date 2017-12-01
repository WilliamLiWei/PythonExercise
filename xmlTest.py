from xml.dom import minidom

doc = minidom.parse('book.xml')
root = doc.documentElement
# print(dir(root))
print(root.nodeName)
books = root.getElementsByTagName('book')
print(type(books))
for book in books:
    titles = book.getElementsByTagName('title')
    print(titles[0].childNodes[0].nodeValue)

import re
# 3位数字,中间一个“-”号，3-8个数字
m = re.match(r'\d{3}\-\d{3,8}', '010-12345')
# print(dir(m))
print(m.string)
print(m.pos, m.endpos)

# 分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.groups())
print("group 0:",m.group(0))
print(m.group(1))
print(m.group(2))

# 分割
p = re.compile(r'\d+')
print(type(p))
print(p.split('one1two3three3four4'))
print(m.group(2))

t = '20:15:45'
re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())
