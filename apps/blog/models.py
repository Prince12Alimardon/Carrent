from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=212)

    def __str__(self):
        return self.category


class Tag(models.Model):
    tag = models.CharField(max_length=212)

    def __str__(self):
        return self.tag


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=212)
    slug = models.SlugField(blank=True, unique=True)
    image = models.ImageField(upload_to='blog')
    content = models.TextField()
    tag = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author_img = models.ImageField(upload_to='Author', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True, null=True, blank=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})


class About(models.Model):
    title = models.CharField(max_length=212)
    content = models.TextField()
    img = models.ImageField(upload_to='About')

    def __str__(self):
        return self.title


class Our_Team(models.Model):
    person_name = models.CharField(max_length=212)
    team_img = models.ImageField(upload_to='Team')
    person_profession = models.CharField(max_length=212)
    person_about = models.TextField()

    def __str__(self):
        return self.person_name


class History(models.Model):
    history_title = models.CharField(max_length=212)
    history_img = models.ImageField(upload_to='History')
    history_content = models.TextField()

    def __str__(self):
        return self.history_title


class How_it_works(models.Model):
    hiw_content = models.TextField(null=True, blank=True)
    step_num = models.IntegerField()
    step_name = models.CharField(max_length=212)

    def __str__(self):
        return self.step_name


class Comment(models.Model):
    name = models.CharField(max_length=212)
    email = models.EmailField()
    website = models.URLField(null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name
