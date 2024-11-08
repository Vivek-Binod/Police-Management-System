from django.db import models
from django.utils import choices, timezone
from django.urls import reverse_lazy
from civilian.models import CustomUser, CivilianModel
from policeAdmin.models import AdminModel
# Create your models here.


class Station(models.Model):
    location = models.CharField(max_length=100)
    number_of_officers = models.PositiveIntegerField(default=0)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.location


class Crime(models.Model):
    statusChoice = [
        ("Completed", "Completed"),
        ("Investigating", "Investigating"),
        ("Request Pending", "Request Pending"),
    ]

    crime_type = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=50)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=statusChoice)
    submitted_by = models.ForeignKey(CivilianModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.crime_type}"

    def get_absolute_url(self):
        return reverse_lazy("submittedDetails", kwargs={"pk": self.pk})


class PoliceModel(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    rank = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    current_crime = models.ForeignKey(Crime, on_delete=models.CASCADE, null=True)
    add_by = models.ForeignKey(AdminModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Witness(models.Model):
    genderChoice = [("M", "Male"), ("F", "Female")]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    statement = models.TextField()
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=genderChoice)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    crime = models.ForeignKey(Crime, on_delete=models.CASCADE)
    added_by = models.ForeignKey(PoliceModel, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse_lazy("witnessDetail", kwargs={"pk": self.pk})


class Suspect(models.Model):
    genderChoice = [("M", "Male"), ("F", "Female")]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=genderChoice)
    date_of_birth = models.DateField()
    crime = models.ForeignKey(Crime, on_delete=models.CASCADE)
    added_by = models.ForeignKey(PoliceModel, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse_lazy("suspectDetail", kwargs={"pk": self.pk})


class Victim(models.Model):
    genderChoice = [("M", "Male"), ("F", "Female")]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=genderChoice)
    date_of_birth = models.DateField()
    crime = models.ForeignKey(Crime, on_delete=models.CASCADE)
    added_by = models.ForeignKey(PoliceModel, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse_lazy("victimDetail", kwargs={"pk": self.pk})


class Evidence(models.Model):
    name = models.CharField(max_length=50)
    crime = models.ForeignKey(Crime, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    description = models.TextField()
    added_by = models.ForeignKey(PoliceModel, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("evidenceDetail", kwargs={"pk": self.pk})


class Criminal(models.Model):
    statusChoice = [("In Jail", "In Jail"), ("Free", "Free")]
    genderChoice = [("M", "Male"), ("F", "Females")]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=statusChoice)
    gender = models.CharField(max_length=10, choices=genderChoice)
    date_of_birth = models.DateField()
    crime = models.ManyToManyField(Crime)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse_lazy("criminalDetails", kwargs={"id": self.pk})
