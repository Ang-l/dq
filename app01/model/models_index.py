from django.db import models

# 定义关系图谱—安全管.理工作模型类tupu_safety_management
class Tupu_Safety_Management(models.Model):
    responsible_department = models.CharField(max_length=255,verbose_name='责任部门')
    list_type = models.CharField(max_length=255,verbose_name='清单类型')
    annual_objectives = models.CharField(max_length=255,verbose_name='年度目标')
    supporting_departments_units = models.TextField(verbose_name='支撑部门及单位')
    common_goal = models.TextField(verbose_name='共性目标')
    personality_goal = models.TextField(verbose_name='个性目标')
    concrete_measure = models.TextField(verbose_name='具体措施')
    concrete_measure_sum = models.IntegerField(verbose_name='具体措施数量')

    class Meta:
        db_table = 'tupu_safety_management'
        verbose_name = '图谱安全管理工作表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.responsible_department


# 定义关系图谱—党建综合考评模型类tupu_pary_building
class Tupu_Party_Building(models.Model):
    responsible_department = models.CharField(max_length=255, verbose_name='责任部门')
    inspection_items = models.CharField(max_length=255,verbose_name='考核事项')
    list_type = models.CharField(max_length=255,verbose_name='清单类型')
    annual_objectives = models.CharField(max_length=255,verbose_name='年度目标')
    supporting_departments_units = models.TextField(verbose_name='支撑部门及单位')
    common_goal = models.TextField(verbose_name='共性目标')
    personality_goal = models.TextField(verbose_name='个性目标')
    concrete_measure = models.TextField(verbose_name='具体措施')
    concrete_measure_sum = models.IntegerField(verbose_name='具体措施数量')

    class Meta:
        db_table = 'tupu_pary_building'
        verbose_name = '图谱党建综合考评表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.responsible_department


# 定义关系图谱—关键业绩指标模型类tupu_key_performance_indicator
class Tupu_Key_Performance_Indicator(models.Model):
    responsible_department = models.CharField(max_length=255, verbose_name='责任部门')
    index_name = models.CharField(max_length=255,verbose_name='指标名称')
    inspection_items = models.CharField(max_length=255,verbose_name='考核事项')
    performance_appraisal_cycle = models.CharField(max_length=255,verbose_name='考核周期')
    index_weight = models.IntegerField(verbose_name='指标权重')
    list_type = models.CharField(max_length=255,verbose_name='指标类型')
    complete_value = models.CharField(max_length=255,verbose_name='目标完成值')
    annual_objectives = models.CharField(max_length=255,verbose_name='年度目标')
    supporting_departments_units = models.TextField(verbose_name='支撑部门及单位')
    common_goals = models.TextField(verbose_name='共性目标')
    personality_goal = models.TextField(verbose_name='个性目标')
    concrete_measure = models.TextField(verbose_name='具体措施')
    concrete_measure_sum = models.IntegerField(verbose_name='具体措施数量')

    class Meta:
        db_table = 'tupu_key_performance_indicator'
        verbose_name = '图谱关键业绩指标表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.responsible_department


# 定义关系图谱—红线指标模型类tupu_red_indicator
class Tupu_Red_Indicator(models.Model):
    responsible_department = models.CharField(max_length=255, verbose_name='责任部门')
    index_name = models.CharField(max_length=255, verbose_name='指标名称')
    supporting_departments_units = models.TextField(verbose_name='支撑部门及单位')
    common_goals = models.TextField(verbose_name='共性目标')
    personality_goal = models.TextField(verbose_name='个性目标')
    concrete_measure = models.TextField(verbose_name='具体措施')
    concrete_measure_sum = models.IntegerField(verbose_name='具体措施数量')

    class Meta:
        db_table = 'tupu_red_indicator'
        verbose_name = '图谱红线指标表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.responsible_department


# 定义关系图谱—专业评价指标模型类tupu_professional_evaluation_index
class Tupu_Professional_Evaluation_Index(models.Model):
    responsible_department = models.CharField(max_length=255, verbose_name='责任部门')
    pofessional_name = models.CharField(max_length=255,verbose_name='专业名称')
    list_type = models.CharField(max_length=255, verbose_name='指标类型')
    annual_objectives = models.CharField(max_length=255, verbose_name='年度目标')
    supporting_departments_units = models.TextField(verbose_name='支撑部门及单位')
    common_goals = models.TextField(verbose_name='共性目标')
    personality_goal = models.TextField(verbose_name='个性目标')
    concrete_measure = models.TextField(verbose_name='具体措施')
    concrete_measure_sum = models.IntegerField(verbose_name='具体措施数量')

    class Meta:
        db_table = 'tupu_professional_evaluation_index'
        verbose_name = '图谱专业评价指标表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.responsible_department


'''
class User(base_models.BaseModel):
    
        #0:什么平台都不可登录
        #1:可以登录小程序平台 以客户的身份登录进去
        #2:admin和小程序都可以登录、小程序是以销售的身份登录
    
    status_enum = (
        (0, '不可使用'),
        (1, 'customer'),
        (2, "admin")
    )

    customer_type_enum = (
        (0, '个人用户'),
        (1, '机构用户')
    )

    customer_level_enum = (
        (0, '未评测'),
        (1, '保守型'),
        (2, '稳健型'),
        (3, '平衡型'),
        (4, '成长型'),
        (5, '进取型'),
    )

    mobile = models.CharField('手机号码', max_length=12, null=False, blank=False, serialize=True,
                              validators=[mobile_validator])
    realname = models.CharField('真实姓名', max_length=60, null=False, blank=False, serialize=True)
    idcard = models.CharField('身份证', max_length=18, null=False, blank=False, serialize=True)
    customer_level = models.IntegerField('客户类型', choices=customer_level_enum, default=0)
    need_idauth = models.BooleanField('是否需要实名认证', default=True)
    address = models.TextField('地址', null=True, blank=True, default='')
    inviter = models.ForeignKey('User', verbose_name='邀请人', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.IntegerField('status', choices=status_enum, default=0)
    email = models.EmailField('email', null=True, blank=True, default='')

    # 表示当前用户是个人用户还是机构用户 改字段不可为空
    customer_type = models.IntegerField('客户类型', choices=customer_type_enum, default=0)

    department = models.ForeignKey('Department', verbose_name='部门', on_delete=models.SET_NULL, null=True, blank=True)
    entry_date = models.DateField('入职时间', null=True, blank=True)
    employee_number = models.DecimalField('编号', max_digits=20, decimal_places=0, null=True, blank=True)
    title = models.CharField('岗位名称', max_length=60, null=True, blank=True)

    occupation = models.CharField('职业', max_length=60, null=True, blank=True)
    education = models.CharField('学历', max_length=20, null=True, blank=True)
    role = models.ForeignKey('Role', verbose_name='拥有的所有角色', on_delete=models.SET_NULL, null=True, blank=True)
    permission = models.ManyToManyField(verbose_name='所拥有的权限', to='Permission', blank=True)

    # is_active
    is_active = models.BooleanField('是否在职', default=True)

    # 测评日期 测评文件
    evaluation_date = models.DateField('测评日期', null=True, blank=True)
    evaluation_file = models.FileField(max_length=200, upload_to='upload/evaluation', null=True, blank=True,
                                       verbose_name="测评文件")

    def __str__(self):
        return self.realname

    def mobile_masked(self):
        if self.mobile:
            return self.mobile[0:3] + '****' + self.mobile[7:11]

    # 交易总金额
    def principal_amount_tatol(self):
        total = Portfolio.objects.filter(customer=self, is_deleted=0, portfolio_status=1).all()
        principal_amount = Decimal(0.00)
        for i in total:
            if i.principal_amount:
                principal_amount += i.principal_amount

        return principal_amount

    # 获取权限
    def initial_permissions(self):
        permissions = self.permission.all().values("url", "method").distinct()
        # permissions_role = user.role.permissions.all().values("url","method").distinct()
        permissions_list = []

        for i in permissions:
            if i not in permissions_list:
                permissions_list.append(i)

        return permissions_list

    # 返回self的全部权限
    def permission_dist(self):
        permissions = self.permission.all().values("url", "method").distinct()
        permission_list = {}
        for item in permissions:
            if item["url"] in permission_list.keys():
                for i in permission_list.keys():
                    if item["url"] == i:
                        permission_list[item["url"]].append(item['method'])
            else:
                permission_list[item["url"]] = [item['method']]

        return permission_list

    # 判断当前用户是否是部门管理员
    @property
    def is_dept_admin(self):
        # 只有status 才会有role
        if self.status == 2:
            # 如果role is 销售主管 return true
            if self.role != None and self.role.name == '销售主管':
                return True
            else:
                return False
        else:
            return False

    # 返回 customer_level_str
    @property
    def customer_level_str(self):
        if self.evaluation_date == None:
            return self.get_customer_level_display
        else:
            # 如果测评日期大于365天的情况下 return 测评已过期
            if (arrow.now() - arrow.get(self.evaluation_date)).days > 90:
                return '测评已过期'
            else:
                return self.get_customer_level_display

    # 查看当前用户是否需要重新评测
    @property
    def is_re_evaluation(self):
        # 没有测评需要测评
        if self.evaluation_date == None:
            return True
        else:
            # 距离上次测评日期大于一年 重新测评
            if (arrow.now() - arrow.get(self.evaluation_date)).days <= 90:
                return False
            else:
                return True

    @property
    def evaluation_date_end(self):
        if self.evaluation_date == None:
            return None
        
        else:
            return arrow.get(self.evaluation_date).shift(days=90).to('Asia/Shanghai').format('YYYY-MM-DD')

    # 返回年龄
    @property
    def age(self):
        try:
            if not self.idcard:
                return 0
            else:
                # 身份证出生年月日
                birth = self.idcard[6:14]
                d1 = arrow.get(birth)
                d2 = arrow.now()
                age = int((d2 - d1).days / 365)
                return age

        except Exception as e:
            return 0

    # 返回性别
    @property
    def sex(self):
        try:
            if not self.idcard:
                return ''
            else:
                birth = int(self.idcard[16])
                if birth % 2 == 1:
                    return '男'

                else:
                    return '女'
        except Exception as e:
            return ''

    # 根据身份证号查询 e签宝 accountId
    def esign_accountid(self):
        e = esign.Esign()
        res = e.getByThirdId(self.idcard)
        # 如果不存在的话创建返回 accountId
        if res['code'] != 0:
            res = self.esign_register(self.realname, self.idcard, self.mobile)
            accountId = res['data']['accountId']
        else:
            accountId = res['data']['accountId']

        return accountId
'''