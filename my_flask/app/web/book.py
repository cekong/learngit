''''''


'''
 把视图函数从主文件分离出来
 用蓝图注册视图函数
 https://coding.imooc.com/lesson/194.html#mid=12773
 
 线程隔离
 https://coding.imooc.com/lesson/194.html#mid=12630
 
 使用模板
 https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320129740415df73bf8f81e478982bf4d5c8aa3817a000
'''

from app.spider.my_flask_test_2_book import yushubook
from app.libs.my_flask_test_2_help import is_key_or_isbn
from flask import jsonify, request, render_template,flash
from flask_login import current_user
from . import web
from app.forms.book import searchform
from app.view_models.book import BookViewModel,BookCollection
import json
from app.models.gift import Gift
from app.models.wish import Wish
from app.view_models.trade import TradeInfo
from app.models.base import db
from app.models.book import Book
'''------------------'''
'''
q :普通关键字（书名或者isbn）  
    isbn号 isbn13(13个0到9的数字组成)  isbn10 10个0到9的数字组成含有一些‘-’
page页码
通过http://127.0.0.1:5000/book/search?q=关键字&page=页码 访问
'''
@web.route("/book/search")
def search():
    form=searchform(request.args) #验证参数
    books=BookCollection()

    if form.validate():
        q=form.q.data.strip()
        page=form.page.data
        # 用来判断q是关键字还是isbn
        key_or_isbn = is_key_or_isbn(q)

        yushu_book = yushubook()

        if key_or_isbn == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q,page)

        books.fill(yushu_book,q)

        # return json.dumps(books,default=lambda o:o.__dict__)
        # return json.dumps(books),200,{'content-type':'application/json'}
        # return jsonify(books)  # 作用和上句相同
        # return 返回的是字符串格式，而result是json即dict格式，需要序列化
    else:
        # return jsonify({'msg':'参数校验失败'})
        flash('参数校验失败')
        return jsonify(form.errors) #显示具体错误信息
    return render_template('search_result.html', books=books)
'''------------------'''

'''------------------'''
'''
通过http://127.0.0.1:5000/book/search/关键字/页码 访问
'''
# @web.route("/book/search/<q>/<page>")
# def search(q,page):#视图函数
# ...
'''------------------'''

@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    has_in_gifts = False
    has_in_wishes = False

    # 取书籍详情数据
    yushu_book = yushubook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)


    # MVC 模型-视图-控制器

    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_wishes = True

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_wishes_model = TradeInfo(trade_wishes)
    trade_gifts_model = TradeInfo(trade_gifts)




    return render_template('book_detail.html',
                           book=book, wishes=trade_wishes_model,
                           gifts=trade_gifts_model, has_in_wishes=has_in_wishes,
                           has_in_gifts=has_in_gifts)




'''使用send_static_file下载'''
# @web.route('/download')
# def download():
#     if user:
#         send_static_file
#         pass

'''request也是线程隔离的'''
@web.route('/test_xiancheng')
def test_xiancheng():
    from flask import request #使用了线程隔离
    from app.libs.none_local import n #未使用线程隔离
    print(n.v)
    n.v=4  #未实现线程隔离
    print('------------------')
    print(getattr(request,'v',None))
    setattr(request,'v',3)  #实现了线程隔离
    print('------------------')
    return ''



'''模板  Flask默认支持的模板是jinja2'''
@web.route('/my_flask_register_login')
def test():
    r={
        'name':'a',
        'action':'hello a'
    }
    r1={
        'name':'b',
        'action':'hello b'
    }
    #模板 html

    return render_template('test.html',data=r,data1=r1)

'''模板  使用基础模板layout.html+test1.html'''
@web.route('/test1')
def test1():
    r={
        'name':'a',
        'action':'hello a'
    }
    r1={
        'name':'b',
        'action':'hello b'
    }
    flash('怎么那么美',category='error')
    flash('就是那么美',category='warning')
    return render_template('test1.html',data=r,data1=r1)