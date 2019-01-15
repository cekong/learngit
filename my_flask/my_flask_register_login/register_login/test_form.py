# -*- coding: UTF-8 -*-
''''''
'''
验证层
'''

from wtforms.fields import core
from wtforms.fields import html5
from wtforms import validators
from wtforms import widgets
from wtforms import Form,StringField,IntegerField,PasswordField



class RegisterForm(Form):
    name = StringField(
        label='用户名',
        validators=[
            validators.DataRequired()
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'models-control'},
        default='用户名'                                           #设置input标签中默认值
    )

    pwd = PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空.')
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'models-control'}
    )

    pwd_confirm = PasswordField(                                #第二次输入密码
        label='重复密码',
        validators=[
            validators.DataRequired(message='重复密码不能为空.'),
            validators.EqualTo('pwd', message="两次密码输入不一致")  #验证2次输入的密码是否一致？
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'models-control'}
    )

    email = html5.EmailField(
        label='邮箱',
        validators=[
            validators.DataRequired(message='邮箱不能为空.'),
            validators.Email(message='邮箱格式错误')
        ],
        widget=widgets.TextInput(input_type='email'),    #生成email input标签
        render_kw={'class': 'models-control'}
    )

    gender = core.RadioField(
        label='性别',
        choices=(                                        #choice radio选项
            (1, '男'),
            (2, '女'),
        ),
        coerce=int                                       #讲用户提交过来的 '4' 强制转成 int 4
    )
    city = core.SelectField(
        label='城市',
        choices=(
            ('bj', '北京'),
            ('sh', '上海'),
        )
    )

    hobby = core.SelectMultipleField(                      #select 下拉框多选框
        label='爱好',
        choices=(
            (1, '篮球'),
            (2, '足球'),
        ),
        coerce=int
    )

    favor = core.SelectMultipleField(
        label='喜好',
        choices=(
            (1, '篮球'),
            (2, '足球'),
        ),
        widget=widgets.ListWidget(prefix_label=False),        #生成Checkbox 多选框
        option_widget=widgets.CheckboxInput(),
        coerce=int,
        default=[1,2]
    )

    def __init__(self, *args, **kwargs):                        #重写form验证类的__init__方法可以实时同步数据中数据
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.favor.choices = ((1, '篮球'), (2, '足球'), (3, '羽毛球'))
        self.city.choices=(('bj', '北京'), ('sh', '上海'), ('tj','天津'))


    def validate_pwd_confirm(self, field):                       #wtforms验证 钩子函数
        """
        自定义pwd_confirm字段规则，例：与pwd字段是否一致
        :param field:
        :return:
        """
        # 最开始初始化时，self.data中已经有所有的值

        if field.data != self.data['pwd']:
            # raise validators.ValidationError("密码不一致") # 继续后续验证
            raise validators.StopValidation("密码不一致")  # 不再继续后续验证


#登录验证实例
class LoginForm(Form):

    #不同的字段 内部包含正则表达式 html5.EmailField | html5.DateTimeField...
    name=StringField(
        label='用户名',
        validators=[                                #验证规则和错误提示信息
            validators.DataRequired(message='用户名不能为空.'),
            validators.Length(min=6, max=18, message='用户名长度必须大于%(min)d且小于%(max)d')
        ],
        widget=widgets.TextInput(),                 #前端页面显示的插件.TextArea
        render_kw={'class': 'models-control'}      #设置form标签的class信息

        )

    # 不同的字段 内部包含正则表达式  html5.EmailField | html5.DateTimeField...
    pwd = PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空.'),
            validators.Length(min=8, message='用户名长度必须大于%(min)d'),
            #自定义验证规则
            validators.Regexp(regex="^(?=.*[a-z])(?=.*\d)[a-z\d]{8,}",
                              message='密码至少8个字符，1个小写字母，1个数字')

        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'models-control'}
    )