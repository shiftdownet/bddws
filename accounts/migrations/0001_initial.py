# Generated by Django 5.0.1 on 2024-01-09 14:42

import accounts.models
import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeptMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pms_value', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='SectMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pms_value', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pms_value', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='WorkersPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'そのユーザ名は既に登録されています。'}, help_text='7桁の半角数字で入力してください。', max_length=7, primary_key=True, serialize=False, unique=True, validators=[accounts.models.username_validator], verbose_name='社員番号')),
                ('full_name', models.CharField(blank=True, help_text='', max_length=150, verbose_name='氏名')),
                ('email', models.EmailField(blank=True, help_text='', max_length=254, verbose_name='Eメールアドレス')),
                ('is_dept_manager', models.BooleanField(default=False, help_text='', verbose_name='部長')),
                ('is_sect_manager', models.BooleanField(default=False, help_text='', verbose_name='室長')),
                ('is_team_manager', models.BooleanField(default=False, help_text='', verbose_name='グループ長')),
                ('is_proper', models.BooleanField(default=False, help_text='', verbose_name='正社員')),
                ('is_temporary_worker', models.BooleanField(default=False, help_text='', verbose_name='派遣社員')),
                ('is_os_worker', models.BooleanField(default=False, help_text='', verbose_name='委託')),
                ('is_secondee_to', models.BooleanField(default=False, help_text='', verbose_name='他社へ出向')),
                ('is_secondee_from', models.BooleanField(default=False, help_text='', verbose_name='他社から出向')),
                ('is_absence', models.BooleanField(default=False, help_text='', verbose_name='休職')),
                ('is_out_of_monitoring_scope_total_work_time', models.BooleanField(default=False, help_text='役職や所属に関係なく、チェックを入れた場合に当該項目が集計対象外になります。', verbose_name='年間労働時間 集計対象外')),
                ('is_out_of_monitoring_scope_for_paid_leave', models.BooleanField(default=False, help_text='役職や所属に関係なく、チェックを入れた場合に当該項目が集計対象外になります。', verbose_name='有給達成目標 集計対象外')),
                ('has_auth_of_mail_check', models.BooleanField(default=False, help_text='例外的にメールの宛先確認の権限を与えるユーザにチェックを入れてください。', verbose_name='メール宛先確認権限')),
                ('has_auth_of_product_investigation', models.BooleanField(default=False, help_text='例外的に成果物の照査者権限を与えるユーザにチェックを入れてください。', verbose_name='照査者権限')),
                ('is_staff', models.BooleanField(default=True, help_text='管理ページへのアクセスを許可する場合チェックを入れます。', verbose_name='スタッフメンバー')),
                ('is_superuser', models.BooleanField(default=False, help_text='すべての権限を割り当てます。', verbose_name='管理者権限')),
                ('is_active', models.BooleanField(default=True, help_text='アカウントを無効化する際にはチェックを外してください。', verbose_name='アクティブアカウント')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, default=[1], help_text='ユーザが属する権限グループを指定してください。', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='権限')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('dept_id', models.ForeignKey(default=0, help_text='', on_delete=django.db.models.deletion.RESTRICT, to='accounts.deptmaster', verbose_name='部署名')),
                ('sect_id', models.ForeignKey(default=0, help_text='', on_delete=django.db.models.deletion.RESTRICT, to='accounts.sectmaster', verbose_name='室名')),
                ('team_id', models.ForeignKey(default=0, help_text='', on_delete=django.db.models.deletion.RESTRICT, to='accounts.teammaster', verbose_name='グループ名')),
                ('workers_position_id', models.ForeignKey(default=0, help_text='', on_delete=django.db.models.deletion.RESTRICT, to='accounts.workersposition', verbose_name='職位')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
