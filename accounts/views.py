from django.shortcuts import render,redirect
from django.views import generic
from .models import CustomUser
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView as BaseLoginView,  LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin

class LoginView(BaseLoginView):
    form_class = LoginFrom
    template_name = "accounts/login.html"

class LogoutView(BaseLogoutView):
    pass

class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    form_class = SetPasswordForm
    success_url = reverse_lazy('accounts:password_change_done')
    template_name = 'accounts/password_change.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # 継承元のメソッドCALL
        context["form_name"] = "password_change"
        return context

class PasswordChangeDone(LoginRequiredMixin,PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'


class ProfileView(TemplateView):
    template_name = "accounts/profile.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        try:
            user = CustomUser.objects.filter(username=self.request.user)[0]
            ctx["view"] = {
                "社員番号": user.username,
                "氏名": user.full_name,
                "E-Mail": user.email,
                "部署名": user.dept_id,
                "室名": user.sect_id,
                "グループ名": user.team_id,
                "職位": user.workers_position_id,
                "部長": user.is_dept_manager,
                "室長": user.is_sect_manager,
                "グループ長": user.is_team_manager,
                "正社員": user.is_proper,
                "派遣社員": user.is_temporary_worker,
                "委託": user.is_os_worker,
                "他社へ出向": user.is_secondee_to,
                "他社から出向": user.is_secondee_from,
                "休職": user.is_absence,
                "年間労働時間 集計対象外": user.is_out_of_monitoring_scope_total_work_time,
                "有給達成目標 集計対象外": user.is_out_of_monitoring_scope_for_paid_leave,
                "メール宛先確認権限": user.has_auth_of_mail_check,
                "照査者権限": user.has_auth_of_product_investigation,
                "スタッフメンバー": user.is_staff,
                "管理者権限": user.is_superuser,
                "アクティブアカウント": user.is_active,
            }
            
        except:
            pass

        return ctx

