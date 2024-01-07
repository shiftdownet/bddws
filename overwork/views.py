from django.views.generic.base import TemplateView
from django.utils import timezone

from django.db.models import Prefetch
from accounts.models import CustomUser
from overwork.models import OverworkApplication


class TodaysOverworkApplicationsView(TemplateView ):
    template_name = "overwork/list.html"



    def get_context_data(self, **kwargs ):
        context = super().get_context_data(**kwargs)
        date = timezone.now()
        context["users"] = CustomUser.objects.prefetch_related(Prefetch("submitted_by", queryset=OverworkApplication.objects.filter(app_date=date), to_attr='app')).all()

        return context

class IndexView(TodaysOverworkApplicationsView):
    pass

