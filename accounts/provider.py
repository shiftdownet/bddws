from .models import CustomUser
from .forms import *


class UserData():
    def get(self, user_id, restricted):
        user = CustomUser.objects.filter(username=user_id)[0]
        everyone = True
        return {
            "社員番号": {"value": user.username, "isEnabled": everyone},
            "氏名": {"value": user.full_name, "isEnabled": everyone},
            "E-Mail": {"value": user.email, "isEnabled": everyone},
            "部署名": {"value": user.dept_id, "isEnabled": everyone},
            "室名": {"value": user.sect_id, "isEnabled": everyone},
            "グループ名": {"value": user.team_id, "isEnabled": everyone},
            "職位": {"value": user.workers_position_id, "isEnabled": everyone},
            "部長": {"value": user.is_dept_manager, "isEnabled": everyone},
            "室長": {"value": user.is_sect_manager, "isEnabled": everyone},
            "グループ長": {"value": user.is_team_manager, "isEnabled": everyone},
            "正社員": {"value": user.is_proper, "isEnabled": restricted},
            "派遣社員": {"value": user.is_temporary_worker, "isEnabled": restricted},
            "委託": {"value": user.is_os_worker, "isEnabled": restricted},
            "他社へ出向": {"value": user.is_secondee_to, "isEnabled": restricted},
            "他社から出向": {"value": user.is_secondee_from, "isEnabled": restricted},
            "休職": {"value": user.is_absence, "isEnabled": restricted},
            "年間労働時間 集計対象外": {"value": user.is_out_of_monitoring_scope_total_work_time, "isEnabled": everyone},
            "有給達成目標 集計対象外": {"value": user.is_out_of_monitoring_scope_for_paid_leave, "isEnabled": everyone},
            "メール宛先確認権限": {"value": user.has_auth_of_mail_check, "isEnabled": everyone},
            "照査者権限": {"value": user.has_auth_of_product_investigation, "isEnabled": everyone},
            "スタッフメンバー": {"value": user.is_staff, "isEnabled": restricted},
            "管理者権限": {"value": user.is_superuser, "isEnabled": restricted},
            "アクティブアカウント": {"value": user.is_active, "isEnabled": everyone},
        }
