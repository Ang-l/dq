from django.http import HttpResponse
from app01.model.models import User_login
import json

#登录视图
def login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_login_obj = User_login.objects.filter(username=username).first()
        #获取数据判断是否为管理员，0不是，1是。
        is_admin = user_login_obj.is_admin

        #如果账号存在
        if user_login_obj:
            #判断密码是否正确
            if user_login_obj.password == password:
                data_str={
                    'code':200,
                    'message':'登录成功',
                    'username':username,
                    'is_admin':is_admin,
                    'is_login':1,
                }
                data_str = json.dumps(data_str)
                return HttpResponse(data_str,content_type='applocation/json')
            else:
                data_str = {
                    'code': 200,
                    'message': '登录失败',
                    'is_login': 0,
                }
                data_str = json.dumps(data_str)
                return HttpResponse(data_str, content_type='applocation/json')
        else:
            data_str = {
                'code': 200,
                'message': '登录失败',
                'is_login': 0,
            }
            data_str = json.dumps(data_str)
            return HttpResponse(data_str, content_type='applocation/json')

