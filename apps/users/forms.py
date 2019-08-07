from django import forms

#图形验证码
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    '''
    登录验证表单
    '''
    #用户名密码不能为空
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=3)