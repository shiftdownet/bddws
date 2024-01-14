from django.db import models

from django.utils.translation import gettext_lazy as _

from django.utils import timezone

from accounts.models import CustomUser


class OverworkApplication(models.Model):
    app_date = models.DateField(_("申請日"), default=timezone.now)
    submitted_by = models.ForeignKey(
        CustomUser, verbose_name="申請者", on_delete=models.DO_NOTHING, help_text=_(""), related_name='submitted_by')
    app_date = models.DateField(_("申請日"), default=timezone.now)

    is_approved = models.BooleanField(
        _("承認ステータス"), default=False, help_text=_(""))
    approved_by = models.ForeignKey(CustomUser, verbose_name="承認者", on_delete=models.DO_NOTHING, help_text=_(
        ""), null=True, blank=True, related_name='approved_by')

    planned_clock_in = models.TimeField(_("出社時刻"))
    planned_clock_out = models.TimeField(_("退社時刻"))
    planned_overwork = models.DecimalField(
        _("申請時間"), max_digits=5, decimal_places=2, default=0.00)

    reason = models.CharField(
        _("申請理由"), max_length=255, blank=True, help_text=_(""))

    def __str__(self):
        return self.reason + " by " + self.submitted_by.full_name + " at " + str(self.app_date)
