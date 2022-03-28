import sys
import os
fnames = os.listdir(sys.path[0])
fnames.remove('index.html')

import time


# hrefs
hrefs = []

for fname in fnames:
    if fname.endswith('html'):
        #print(fname)
        href = fname.replace('.html','')
        # Warning: `Watch this <http://www.youtube.com/watch?v=dQw4w9WgXcQ&ob=av3e>`_!
        href = f"""`{href} <https://godblesschina.github.io/codeshare/{fname}>`_"""
        hrefs.append(href)
findexrstbac = open('source/_index.rst')
findexrst = open('source/index.rst','w')
s = findexrstbac.read()
content = s.replace('replace','')
#print(content)
findexrst.write(content)
for line in hrefs:
    #print(line)
    findexrst.writelines(line+"\n\n\n")
    
findexrstbac.close()
findexrst.close()
open('source/index.rst','w').write(content)

print('开始编译')
os.system("make html")
#os.system('open build/html/index.html')
print("编译完成")
