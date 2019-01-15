''''''
'''
使用ViewModel处理书籍数据
https://coding.imooc.com/lesson/194.html#mid=12638
https://coding.imooc.com/lesson/194.html#mid=12639


因为用isbn和关键字搜索时返回的数据格式不同，所以需要自定义格式
'''


class BookViewModel:
    def __init__(self,book):
        self.title=book['title']
        self.publisher=book['publisher']
        self.pages = book['pages'] or ''
        self.price = book['price']
        self.summary = book['summary'] or ''
        self.image = book['image']
        self.author ='、'.join(book['author'])
        self.isbn=book['isbn']
    @property
    def intro(self):
        intros=filter(lambda x:True if x else False,
                      [self.author,self.publisher,self.price])
        return ' / '.join(intros)


class BookCollection:
    def __init__(self):
        self.total=0
        self.books=[]
        self.q=''

    def fill(self,yushu_book,q):
        self.total=yushu_book.total
        self.q=q
        self.books=[BookViewModel(book) for book in yushu_book.books]


#第二种方法
class _BookViewModel:
    @classmethod
    def package_single(cls,data,q): #搜索isbn返回的数据格式修改
        returned={
            'books':[],
            'total':0,
            'q':q
        }
        if data:
            returned['total']=1
            returned['books']=[cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls,data,q): #搜索keyword返回的数据格式修改
        returned={
            'books':[],
            'total':0,
            'q':q
        }
        if data:
            returned['total']=data['total']
            returned['books']=[cls.__cut_book_data(book) for book in data['books']]
        return returned

    @classmethod
    def __cut_book_data(cls,data):
        book={
            'title':data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',  #当此值为空时，显设置为“”，否则将设为null
            'price': data['price'],
            'summary': data['summary'] or '',  #当此值为空时，显设置为“”，否则将设为null
            'image': data['image'],
            'author':'、'.join(data['author'])#列表形式改为字符串形式
        }
        return book