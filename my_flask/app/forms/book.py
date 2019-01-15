''''''


'''
验证层
wtforms 
WTForms是一个支持多个web框架的form组件，主要用于对用户请求数据进行验证。
'''
from wtforms import Form,StringField,IntegerField
from wtforms.validators import Length,NumberRange,DataRequired,Regexp

class searchform(Form):
    q=StringField(validators=[DataRequired(),Length(min=1,max=30)])
                                #关键字长度限制,DataRequired可防止只有一个空格的字符
    page=IntegerField(validators=[NumberRange(min=1,max=99)],default=1)
                                #页码默认设为1，最大不超过99

class DriftForm(Form):
    recipient_name = \
        StringField(validators=[DataRequired(),
                                Length(
                                    min=2, max=20,
                                    message='收件人姓名长度必须在2到20个字符之间')])
    mobile = \
        StringField(validators=[DataRequired(),
                                Regexp('^1[0-9]{10}$', 0, '请输入正确的手机号')])
    message = StringField()
    address = \
        StringField(validators=[DataRequired(),
                                Length(min=10, max=70,
                                       message='地址还不到10个字吗？尽量写详细一些吧')])