import re
s1="helloworld,helloworld"
w1="hello"
w2="world"

print(re.search(w1,s1))
print(re.search(w1,s1).group())
print(re.match(w1,s1))
print(re.match(w1,s1).group())



print(re.search(w2,s1))
print(re.search(w2,s1).group())
print(re.match(w2,s1))
print(re.match(w2,s1).group())