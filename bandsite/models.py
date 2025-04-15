from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField(default="")
    photo = models.ImageField(upload_to='members_photos/', null=True, blank=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    cover = models.ImageField(upload_to='album_covers/')
    description = models.TextField(default='')

    def __str__(self):
        return self.title

class Concert(models.Model):
    location = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField(default="")

    def __str__(self):
        return f"{self.location} - {self.date.strftime('%d %B %Y')}"

class Review(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.rating}/5"
