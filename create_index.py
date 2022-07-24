## 根据GitHub上已有的md文件，在index页面上添加一个目录
import os

MdFileList = [i for i in os.listdir() if i[-3:]=='.md']
print("you have %d MD file" % len(MdFileList))

def URLTemplate(text,url):
    return "[%s](https://sti1l-0.github.io/%s)" % (text, url)

index_md = """
# Welcome to sti1l-0's blog

all the link below is the markdown-based blog I write

try CTRL+F to find what you need
"""

for md in MdFileList:
    i = os.path.splitext(md)[0]
    index_md += "\n+ " + URLTemplate(i, i) + "\n"

with open('index.md', 'w', encoding='utf-8') as f:
    f.write(index_md)
    print("index.md was written")