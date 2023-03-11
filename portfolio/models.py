from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Skill(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.caption


class Team(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    linkedin = models.URLField(max_length=200)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Project(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    team_lead = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="team")
    team_members = models.ManyToManyField(Team)
    github_link = models.URLField(max_length=200)
    youtube_link = models.URLField(max_length=200, blank=True, null=True)
    description = models.TextField(validators=[MinLengthValidator(20)])
    skills = models.ManyToManyField(Skill)
    excerpt = models.CharField(max_length=300, null=True)
    details = models.TextField(validators=[MinLengthValidator(20)], null=True)
    slug = models.SlugField(unique=True, db_index=True)

    def __str__(self) -> str:
        return f"{self.slug}"
