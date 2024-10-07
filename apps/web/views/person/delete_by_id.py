import uuid
from datetime import datetime

from django.shortcuts import redirect, render

from ...models.person.education import Education as ModelEducation
from ...models.person.person import Person as ModelPerson
from ...models.person.work_experience import \
    WorkExperience as ModelWorkExperience


def detele_by_id(request, id):
    try:
        person = ModelPerson.objects.get(person_id=id)
    except:
        return redirect(to="web:registration")

    if person.deleted_at == None:
        person.deleted_at = datetime.now()
        uuid_str = str(uuid.uuid4())
        person.email = f"{person.email}-del-{uuid_str[0:6]}"
        person.save()

    ModelEducation.objects.filter(
        person=id,
        deleted_at__isnull=True
    ).update(deleted_at=datetime.now())
    ModelWorkExperience.objects.filter(
        person=id,
        deleted_at__isnull=True
    ).update(deleted_at=datetime.now())

    return redirect(to="web:person")
