from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View
from pymongo.auth import authenticate


class LogoutView(auth_views.LogoutView):
    '''
    退出
    '''
    def get(self,request,*args,**kwargs):
        auth_logout(request)
        return HttpResponseRedirect('/login/')

class LoginVies(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        #实例化
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username','')
            pass_word = request.POST.get('password','')
            print('user_name',user_name)
            print('pass_word',pass_word)

            user = authenticate(username=user_name,
                                password=pass_word)
            print(user)
            if user is not None:
                if user.is_active:
                    print('邮箱已激活,并且登录成功')
                    login(request,user)
                    return render(request,'index.html',{'name':user_name})
                else:
                    print('邮箱未激活,登录失败')
                    return render(request,'login.html',{'msg':'邮箱未激活,登录失败',
                                                        'login_form':login_form})
            else:
                print('登录失败')
                return render(request,'login.html',{'msg':'用户名或者密码错误',
                                                    'login_form':login_form})
        else:
            return render(request, 'login.html', {'login_form': login_form})