from django.db import models


class Person(models.Model):
    GENDER = (
        ("1", "Pria"),
        ("0", "Wanita"),
    )

    person_id = models.CharField(max_length=45, primary_key=True)
    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=25, unique=True)
    gender = models.CharField(max_length=5, choices=GENDER)
    age = models.IntegerField()
    phone = models.CharField(max_length=25)
    photo = models.ImageField(upload_to="photo/", null=True, blank=True)
    address = models.TextField()
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "person"
