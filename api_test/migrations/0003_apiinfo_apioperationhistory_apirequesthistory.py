# Generated by Django 2.0.1 on 2018-01-19 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_test', '0002_auto_20180119_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='接口名称')),
                ('http_type', models.CharField(choices=[('http', 'HTTP'), ('https', 'HTTPS')], default='HTTP', max_length=50, verbose_name='http/https')),
                ('requestType', models.CharField(choices=[('POST', 'POST'), ('GET', 'GET'), ('PUT', 'PUT'), ('DELETE', 'DELETE')], max_length=50, verbose_name='请求方式')),
                ('apiAddress', models.CharField(max_length=1024, verbose_name='接口地址')),
                ('request_head', models.CharField(blank=True, max_length=1024, null=None, verbose_name='请求头')),
                ('requestParameterType', models.CharField(choices=[('form-data', '表单(form-data)'), ('raw', '源数据(raw)'), ('Restful', 'Restful')], max_length=50, verbose_name='请求参数格式')),
                ('requestParameter', models.CharField(blank=True, max_length=10240, null=True, verbose_name='请求参数')),
                ('status', models.BooleanField(default=True, verbose_name='状态')),
                ('response', models.CharField(blank=True, max_length=10240, null=True, verbose_name='返回数据')),
                ('mock_code', models.CharField(choices=[('200', '200'), ('404', '404'), ('400', '400'), ('502', '502'), ('500', '500'), ('302', '302')], max_length=50, verbose_name='HTTP状态')),
                ('data', models.TextField(blank=True, max_length=4096, null=True, verbose_name='内容')),
                ('lastUpdateTime', models.DateTimeField(auto_now=True, verbose_name='最近更新')),
                ('userUpdate', models.CharField(max_length=50, verbose_name='更新人')),
                ('description', models.CharField(blank=True, max_length=1024, null=True, verbose_name='描述')),
                ('ApiGroupLevelFirst_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ApiGroupLevelFirst_id', to='api_test.ApiGroupLevelFirst', verbose_name='所属一级分组')),
                ('ApiGroupLevelSecond_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ApiGroupLevelSecond_id', to='api_test.ApiGroupLevelSecond', verbose_name='所属二级分组')),
                ('project_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Project_id', to='api_test.Project', verbose_name='所属项目')),
            ],
            options={
                'verbose_name': '接口',
                'verbose_name_plural': '接口管理',
            },
        ),
        migrations.CreateModel(
            name='ApiOperationHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=50, verbose_name='用户姓名')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='操作时间')),
                ('description', models.CharField(blank=True, max_length=1024, null=True, verbose_name='操作内容')),
                ('apiInfo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_test.ApiInfo', verbose_name='接口ID')),
            ],
            options={
                'verbose_name': '接口操作历史',
                'verbose_name_plural': '接口操作历史',
            },
        ),
        migrations.CreateModel(
            name='APIRequestHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('requestTime', models.DateTimeField(auto_now_add=True, verbose_name='请求时间')),
                ('requestType', models.CharField(max_length=50, verbose_name='请求方法')),
                ('requestAddress', models.CharField(max_length=1024, verbose_name='请求地址')),
                ('httpCode', models.CharField(max_length=50, verbose_name='HTTP状态')),
                ('apiInfo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_test.ApiInfo', verbose_name='接口ID')),
            ],
            options={
                'verbose_name': '接口请求历史',
                'verbose_name_plural': '接口请求历史',
            },
        ),
    ]