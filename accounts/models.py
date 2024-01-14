from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin, UserManager, Group, Permission
import re


class DeptMaster(models.Model):
    pms_value = models.IntegerField(default=0)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class SectMaster(models.Model):
    pms_value = models.IntegerField(default=0)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class TeamMaster(models.Model):
    pms_value = models.IntegerField(default=0)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class WorkersPosition(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


def username_validator(value):
    if not re.match(r"[0-9]{7}", value):
        raise ValidationError("7桁の半角数字で入力してください。")


class CustomUser(AbstractBaseUser, PermissionsMixin):
    # PK
    username = models.CharField(
        _("社員番号"),
        max_length=7,
        primary_key=True,
        unique=True,
        help_text=_(
            "7桁の半角数字で入力してください。"
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("そのユーザ名は既に登録されています。"),
        },
    )

    # Personal Info
    full_name = models.CharField(
        _("氏名"), max_length=150, blank=True, help_text=_(""))
    email = models.EmailField(_("Eメールアドレス"), blank=True, help_text=_(""))

    # Belongs
    dept_id = models.ForeignKey(
        DeptMaster, verbose_name="部署名", on_delete=models.RESTRICT, default=0, help_text=_(""))
    sect_id = models.ForeignKey(
        SectMaster, verbose_name="室名", on_delete=models.RESTRICT, default=0, help_text=_(""))
    team_id = models.ForeignKey(TeamMaster, verbose_name="グループ名",
                                on_delete=models.RESTRICT, default=0, help_text=_(""))

    # Position
    workers_position_id = models.ForeignKey(
        WorkersPosition, verbose_name="職位", on_delete=models.RESTRICT, default=0, help_text=_(""))

    # Post
    is_dept_manager = models.BooleanField(
        _("部長"), default=False, help_text=_(""))
    is_sect_manager = models.BooleanField(
        _("室長"), default=False, help_text=_(""))
    is_team_manager = models.BooleanField(
        _("グループ長"), default=False, help_text=_(""))

    # Category
    is_proper = models.BooleanField(_("正社員"), default=False, help_text=_(""))
    is_temporary_worker = models.BooleanField(
        _("派遣社員"), default=False, help_text=_(""))
    is_os_worker = models.BooleanField(_("委託"), default=False, help_text=_(""))
    is_secondee_to = models.BooleanField(
        _("他社へ出向"), default=False, help_text=_(""))
    is_secondee_from = models.BooleanField(
        _("他社から出向"), default=False, help_text=_(""))
    is_absence = models.BooleanField(_("休職"), default=False, help_text=_(""))

    # Attribute
    is_out_of_monitoring_scope_total_work_time = models.BooleanField(
        _("年間労働時間 集計対象外"), default=False, help_text=_("役職や所属に関係なく、チェックを入れた場合に当該項目が集計対象外になります。"))
    is_out_of_monitoring_scope_for_paid_leave = models.BooleanField(
        _("有給達成目標 集計対象外"), default=False, help_text=_("役職や所属に関係なく、チェックを入れた場合に当該項目が集計対象外になります。"))

    # Business Permission
    has_auth_of_mail_check = models.BooleanField(
        _("メール宛先確認権限"), default=False, help_text=_("例外的にメールの宛先確認の権限を与えるユーザにチェックを入れてください。"))
    has_auth_of_product_investigation = models.BooleanField(
        _("照査者権限"), default=False, help_text=_("例外的に成果物の照査者権限を与えるユーザにチェックを入れてください。"))

    # System Permission
    is_staff = models.BooleanField(
        _("スタッフメンバー"), default=True, help_text=_("管理ページへのアクセスを許可する場合チェックを入れます。"))
    is_superuser = models.BooleanField(
        _("管理者権限"), default=False, help_text=_("すべての権限を割り当てます。"), )
    is_active = models.BooleanField(
        _("アクティブアカウント"), default=True, help_text=_("アカウントを無効化する際にはチェックを外してください。"))

    groups = models.ManyToManyField(
        Group,
        verbose_name=_("権限"),
        default=[1],
        blank=True,
        help_text=_("ユーザが属する権限グループを指定してください。"),
        related_name="user_set",
        related_query_name="user",
    )

    # Important date
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    # Other settings
    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        # abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        return self.full_name

    def get_short_name(self):
        """Return the short name for the user."""
        return self.full_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
