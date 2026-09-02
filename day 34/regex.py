#match using(it checks only strating position is currect or not)
import re
pattern = r'[0-9]'
text = 'codegnan'
res = re.match(pattern,text)
print(res.group()if res else "pattern not found")

#search(check  whole entire string)
import re
pattern = r'[0-9]'
text = 'codegnan2026'
res = re.search(pattern,text)
print(res.group()if res else "pattern not found")
#findall(list of pattern it gives)
import re
pattern = r'[0-9]'
text = 'codegnan 2026 python version 3.14'
res = re.findall(pattern,text)
print(res)
#finditer(it is also give index)
import re
pattern = r'[0-9]'
text = 'codegnan 2026 python version 3.14'
res = re.finditer(pattern,text)
for i in res:
    print(i.group(),i.start())
    
#print(res)

#fullmatch(what only needded thing)
import re
pattern = r'[0-9]{10}'
text = '6302760173'
res = re.fullmatch(pattern,text)


#split()
import re
pattern = r'[,(#)]'
text = 'java,python(html#css'
res = re.split(pattern,text)
print(res)

#sub(replacing)
import re
pattern = r'[a-z]'
text = 'python version 3.14,batch-63'
res = re.sub(pattern,'*',text)
print(res)

#symbuls
import re
pattern = r'e.t'
text = 'e@t eaat eat ett ect egfhjet hgjeokj'
res = re.findall(pattern,text)
print(res)


#cap ^(to check starting function)
import re
pattern = r'^(91)'
text = '6302760173'
res = re.findall(pattern,text)
print(res)
#$
import re
pattern = r'0$'
text = '6302760173'
res = re.findall(pattern,text)
print(res)


import re
pattern = r'to+'
text = ' to tdffhjk too tooo toooooo'
res = re.findall(pattern,text)
print(res)

import re
pattern = r'to#'
text = ' to tdffhjk too tooo toooooo'
res = re.findall(pattern,text)
print(res)


import re
pattern = r'ab+'
text = ' ab abbb a abbbbb abbbbb'
res = re.findall(pattern,text)
print(res)



#
import re
pattern = r'colo?rs'
text = ' colous'
res = re.findall(pattern,text)
print(res)

#import re(\or)
pattern = r'91|0'
text = ' 05678'
res = re.findall(pattern,text)
print(res)

#
import re
pattern = r'[aeiouAEIOU]'
text = ' coegnan progrming'
res = re.findall(pattern,text)
print(res)





