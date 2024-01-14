from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from accounts.models import *


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (_("Basic info"), {"fields": ("is_active", "password",)}),
        (_("Personal info"), {"fields": ("full_name", "email")}),
        (_("Belongs"), {"fields": ("dept_id", "sect_id", "team_id")}),
        (_("Position"), {"fields": ("workers_position_id",)}),
        (_("Post"), {"fields": ("is_dept_manager",
         "is_sect_manager", "is_team_manager")}),
        (_("Category"), {"fields": ("is_proper", "is_temporary_worker",
         "is_os_worker", "is_secondee_to", "is_secondee_from", "is_absence")}),
        (_("Attribute"), {"fields": (
            "is_out_of_monitoring_scope_total_work_time", "is_out_of_monitoring_scope_for_paid_leave")}),
        (_("Business Permissions"), {
         "fields": ("has_auth_of_mail_check", "has_auth_of_product_investigation")}),
        (
            _("System Permissions"),
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "groups",
                    # "user_permissions",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )
    list_display = ("username", "full_name", "dept_id", "sect_id", "team_id",
                    "workers_position_id", "is_staff", "is_superuser", "last_login")
    list_filter = ("dept_id", "sect_id", "team_id", "workers_position_id")
    search_fields = ("username", "full_name")
    # ordering = ("username",)
    filter_horizontal = (
        "groups",
        # "user_permissions",
    )


CustomUser = get_user_model()
admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(DeptMaster)
admin.site.register(SectMaster)
admin.site.register(TeamMaster)
admin.site.register(WorkersPosition)
