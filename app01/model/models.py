from django.db import models

#定义用户模型类User_login
class User_login(models.Model):
    username = models.CharField(max_length=20,verbose_name='用户名')
    password = models.CharField(max_length=20,verbose_name='密码')
    is_admin = models.CharField(max_length=1,default=0,verbose_name='是否为管理员，1：是，0：不是')

    class Meta:
        db_table = 'user_login'
        verbose_name = '用户登录表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

#定义关键业绩指标定义模型类key_performance_indicator _dingyi
class Key_Performance_indicator_dingyi(models.Model):
    assessment_latitude =  models.CharField(max_length=255,verbose_name='考核维度')
    index_name = models.CharField(max_length=255,verbose_name='指标名称')
    key_test = models.CharField(max_length=2000,verbose_name='考核要素')
    basic_score = models.IntegerField(verbose_name='基础分值')
    submit_the_cycle = models.CharField(max_length=255,verbose_name='报送周期')
    evaluation_department = models.CharField(max_length=255,verbose_name='评价部门')
    define_design_formulas = models.CharField(max_length=2000,verbose_name='定义和计算公式')
    evaluation_criterion = models.CharField(max_length=2000,verbose_name='定义和评价标准')

    #元类
    class Meta:
        db_table = 'key_performance_indicator_dingyi'   #定义数据库中的表名
        verbose_name = '关键业绩指标定义表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.index_name

#定义专业评价指标定义模型类professional_evaluation_index_dingyi
class Professional_Evaluation_index_dingyi(models.Model):
    inspection_department = models.CharField(max_length=255,verbose_name='考核部门')
    pofessional_name = models.CharField(max_length=255,verbose_name='专业名称')
    points_based_on = models.CharField(max_length=2000,verbose_name='减分依据')

    class Meta:
        db_table = 'professional_evaluation_index_dingyi'
        verbose_name = '专业评价指标定义表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.pofessional_name

#定义红线指标定义模型类red_indicator_dingyi
class Red_Indicator_dingyi(models.Model):
    inspection_department = models.CharField(max_length=255,verbose_name='考核部门')
    index_name = models.CharField(max_length=255,verbose_name='指标名称')
    grading = models.CharField(max_length=2000,verbose_name='评分依据')

    class Meta:
        db_table = 'red_indicator_dingyi'
        verbose_name = '红线指标定义表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.index_name

#定义安全管理工作定义模型类safety_management_dingyi
class Safety_Management_dingyi(models.Model):
    inspection_department = models.CharField(max_length=255,verbose_name='考核部门')
    points_based_on = models.CharField(max_length=2000,verbose_name='减分依据')

    class Meta:
        db_table = 'safety_management_dingyi'
        verbose_name = '安全管理工作定义表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.inspection_department

#定义党建综合考评定义模型类party_building_dingyi
class Party_Building_dingyi(models.Model):
    inspection_department = models.CharField(max_length=255,verbose_name='考核部门')
    inspection_items = models.CharField(max_length=2000,verbose_name='考核事项')

    class Meta:
        db_table = 'party_building_dingyi'
        verbose_name = '党建综合考评定义表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.inspection_department

