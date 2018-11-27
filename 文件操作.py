''''''
'''写文件'''
f=open('test.txt','wt')
f.write('hello world')
f.close()

'''使用with，追加内容'''
with open('test.txt','at') as f:
    f.write('\nhello mooc')


'''读取文件'''
with open('test.txt','rt') as f:
    print(f.read())