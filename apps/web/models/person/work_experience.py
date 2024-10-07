from django.db import models

from .person import Person


class WorkExperience(models.Model):

    person = models.ForeignKey(to=Person, on_delete=models.CASCADE)
    company_nm = models.CharField(max_length=105)
    industry = models.CharField(max_length=45)
    role = models.CharField(max_length=45)
    date_in = models.DateField()
    date_out = models.DateField()
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "work_experience"
