from django.db import models


from base.base_models import BaseModel

class Users(BaseModel):
    user_type_enum = (
        (1,'管理员'),
        (2,'普通用户'),
    )

    username = models.CharField(max_length=20,verbose_name='用户名')
    password = models.CharField(max_length=20,verbose_name='密码')
    is_admin = models.IntegerField('is_admin', choices=user_type_enum, default=1)
    # is_admin = models.CharField(max_length=1,default=0,verbose_name='是否为管理员，1：是，0：不是')

    class Meta:
        db_table = 'user_login'
        verbose_name = '用户登录表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

