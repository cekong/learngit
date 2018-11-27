''''''
'''
正则表达式
http://www.runoob.com/regexp/regexp-syntax.html
https://coding.imooc.com/learn/list/92.html
'''
import re

line="bobbbbb123"
reg_str=".*?(b{3,5}).*"
a=re.match(reg_str,line)
print(a.group(1))


line="xxx出生于2001年1月1日"
line="xxx出生于2001年01月01日"
line="xxx出生于2001-01-01"
# line="xxx出生于2001/1/1"
# line="xxx出生于2001-1-1"
# line="xxx出生于2001年1月"
reg_str1=".*于(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}.?|[月]$|$))"
a1=re.match(reg_str1,line)
print(a1.group(1))
print(a1.group(1))