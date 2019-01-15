
''''''
'''
闪现 flash
'''
from flask import Flask,request,flash,get_flashed_messages

app = Flask(__name__)
app.secret_key = 'some_secret'
'''一定要注意要加secret_key 参数'''

@app.route('/set/')
def index2():
    flash('Disposable')    #在message中设置1个个值
    return 'ok'

#---------------------------------------------------------------------------------

@app.route('/')
def index1():
    messages = get_flashed_messages() #获取message中设置的值，只能获取1次。（1次性）
    print(messages)
    return "Index1"






if __name__ == "__main__":
    app.run()
