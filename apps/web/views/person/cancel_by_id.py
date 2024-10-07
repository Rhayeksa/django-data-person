from django.shortcuts import redirect

from ...models.person.education import Education as ModelEducation
from ...models.person.person import Person as ModelPerson
from ...models.person.work_experience import \
    WorkExperience as ModelWorkExperience


def cancel_by_id(request, id):
    try:
        person = ModelPerson.objects.get(person_id=id)
    except:
        return redirect(to="web:registration")

    ModelEducation.objects.filter(
        person=id,
        created_at__isnull=True
    ).delete()
    ModelEducation.objects.filter(
        person=id,
        updated_at__isnull=False
    ).update(updated_at=None, deleted_at=None)

    ModelWorkExperience.objects.filter(
        person=id,
        created_at__isnull=True
    ).delete()

    if person.created_at == None:
        ModelPerson.objects.filter(person_id=id).delete()
        return redirect(to="web:registration")

    return redirect(to="web:person_detail_by_id", id=person.person_id)
