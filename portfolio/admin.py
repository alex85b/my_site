from django.contrib import admin

from .models import Project, Team, Skill

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_filter = ("team_lead", "skills", "date",)
    list_display = ("name", "youtube_link", "date",)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Project, ProjectAdmin)
admin.site.register(Team)
admin.site.register(Skill)
