from django.db import models

# Create your models here.

# Teams for Home Page
class Team(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Players(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to='player/')
    date_of_birth = models.DateField(null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class TeamTable(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    played = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    drawn = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    gd = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.team}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email

class News(models.Model):
    title = models.CharField(max_length=100)
    information = models.TextField()
    images = models.ImageField(null=True, blank=True, upload_to="news_images/")

    def __str__(self):
        return self.title




