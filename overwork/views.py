from django.views.generic.base import View
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils import timezone

from django.db.models import Prefetch
from accounts.models import CustomUser
from overwork.models import OverworkApplication


class OverworkApplicationsView( View ):
    template_name = "overwork/list.html"

    def get(self, request, *args, **kwargs):
        if "date" in request.GET:
            date = request.GET["date"]
        else:
            date = timezone.now()
        return render(request, self.template_name, {"users": CustomUser.objects.prefetch_related(Prefetch("submitted_by", queryset=OverworkApplication.objects.filter(app_date=date), to_attr='app')).all()})
    
class IndexView(OverworkApplicationsView):
    pass

