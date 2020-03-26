from django.db import models
from django_countries.fields import CountryField


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
