from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from .models import *

from .forms import *
from .models import *
# Create your views here.

class HomePageVIEW(View):
    def get(self, request):
        teams = Team.objects.all()
        news = News.objects.all()
        return render(request, 'home.html', {'teams': teams, 'news': news})


class TablePageVIEW(View):
    def get(self, request):
        team_table = TeamTable.objects.all().order_by('-points', '-gd')
        return render(request, 'liga/table.html', {'team_table': team_table})

class ContactUs(View):
    def get(self, request):
        contact_form = ContactUsForm()
        return render(request, 'liga/contact.html', {'contact_form': contact_form})

    def post(self, request):
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'You have successfully send'
                                      ' message!')
            return redirect("liga:contact")
        return render(request, 'liga/contact.html', {'contact_form': contact_form})


class TeamDetailVIEW(View):
    def get(self, request, id):
        team_detail = Team.objects.get(id=id)
        players = Players.objects.filter(team__name=team_detail.name)
        return render(request, 'liga/detail.html', {'team_detail': team_detail, 'players': players})
