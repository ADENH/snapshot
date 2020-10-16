from django.shortcuts import render
from teams.models import Team
from .models import Company
# Create your views here.
def index(request):
    teams = Team.objects.all()

    company = Company.objects.get(id=1)
    context={
        'teams' : teams,
        'company' : company
    }

    return render(request,'index.html',context)