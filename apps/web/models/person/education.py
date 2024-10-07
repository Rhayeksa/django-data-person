from django.db import models

from .person import Person


class Education(models.Model):
    CATEGORY = (
        ("High School", "High School"),
        ("University", "University"),
        ("Course", "Course"),
    )

    person = models.ForeignKey(to=Person, on_delete=models.CASCADE)
    education_nm = models.CharField(max_length=105)
    category = models.CharField(max_length=45, choices=CATEGORY)
    major = models.CharField(max_length=45)
    date_in = models.DateField()
    date_out = models.DateField()
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "education"
