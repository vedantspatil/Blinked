from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
# default null,blank->false  null for database(empty allowed or not),similarly blank for form

class User(models.Model):
    """
        User Model

        profile photo stored in profilePhoto/year/month/date
        Gender stored as 'M' or 'F'

        username, password are not NULL fields
    """
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=256)
    name = models.CharField(default="", max_length=50, null=True, blank=True)
    country = CountryField(default="", null=True, blank=True)
    # ref: https://stackoverflow.com/questions/8077840/choicefield-in-django-model
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, null=True, blank=True, choices=GENDER_CHOICES)
    dateOfBirth = models.DateField(null=True, blank=True)
    profilePhoto = models.ImageField(default="https://userpic.codeforces.com/no-avatar.jpg", blank=True, null=True,
                                     # optional in both form and db
                                     upload_to="profilePhoto/%Y/%m/%D/")

    mobileNumber = models.CharField(default="", max_length=20, null=True, blank=True)
    address = models.TextField(default="", null=True, blank=True)
    summary = models.TextField(default="", null=True, blank=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.username)


class School(models.Model):
    schoolName = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return "{}".format(self.schoolName)


class Education(models.Model):
    """
        Education Model

        certificate is stored as TEXTFIELD

        degree, fieldOfStudy, certificate are not NULL fields
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    degree = models.CharField(max_length=200)
    fieldOfStudy = models.CharField(max_length=200)
    startYear = models.IntegerField(null=True, blank=True)
    endYear = models.IntegerField(null=True, blank=True)
    certificate = models.TextField()
    additionalNotes = models.TextField(default="", null=True, blank=True)
    legitimate = models.BooleanField(default=True)


    def __str__(self):
        return "{} ({})".format(self.user.username, self.degree)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
    	return self.title

    def get_absolute_url(self):
    	return reverse('post-detail', kwargs={'pk': self.pk})


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    icon = models.CharField(default="", max_length=200, null=True, blank=True)
    title = models.CharField(default="", max_length=200, blank=True)
    # location: str
    country = CountryField(default="", null=True, blank=True)
    TYPE_CHOICES = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
    )
    type = models.TextField(null=True, blank=True, choices=TYPE_CHOICES)
    deadline = models.DateField(null=True, blank=True)
    qualifications = models.TextField(default="Qualifications are adjustable", null=False, blank=False)
    description = models.TextField()
    publish_date = models.DateField(null=True, blank=True)
    vacancy = models.IntegerField(null=True, blank=True)
    salary_min = models.IntegerField(null=True, blank=True)
    salary_max = models.IntegerField(null=True, blank=True)
    benefits = models.TextField(default="", blank=True)

    def __str__(self):
        return "{} ({})".format(self.title, self.salary_max, self.country)


class Qualification(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    degree = models.CharField(max_length=200)

    def __str__(self):
        return "{} ({})".format(self.job.title, self.degree)

