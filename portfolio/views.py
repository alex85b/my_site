from django.shortcuts import render
from django.views import View

from .models import Project

# Create your views here.


class IndexView(View):
    def get(self, request):
        latest_projects = Project.objects.all().order_by("-date")[:3]
        projects_skills = [proj.skills.all() for proj in latest_projects]
        display_proj = zip(latest_projects, projects_skills)
        return render(request, "portfolio/index.html", {"projects": display_proj})

    # def post(self, request):
    #     # This should be reconsidered !
    #     return render(request, "portfolio/index.html")


class ProjectDetailsVeiw(View):
    def get(self, requet, slug):
        print(f"slug: {slug}")
        return render(requet, "portfolio/project_details.html")
