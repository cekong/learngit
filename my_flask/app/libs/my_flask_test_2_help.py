''''''
'''
用来判断q是关键字还是isbn
'''
def is_key_or_isbn(word):
    ''''''
    '''
        key :普通关键字  /isbn:isbn号 isbn13(13个0到9的数字组成)  isbn10 10个0到9的数字组成含有一些‘-’
        page
    '''
    key_or_isbn='key'
    if len(word) ==13 and word.isdigit():
        key_or_isbn= 'isbn'
    short_word=word.replace('-','')
    if '-' in word and len(short_word)==10 and short_word.isdigit() :
        key_or_isbn='isbn'

    return key_or_isbn