from datetime import datetime

from django.shortcuts import redirect

from ...models.person.work_experience import \
    WorkExperience as ModelWorkExperience


def delete_work_by_id(request, person_id, id):

    model = ModelWorkExperience.objects.get(person_id=person_id, id=id)

    if model.created_at == None:
        model.delete()
    else:
        model.updated_at = datetime.now()
        model.deleted_at = datetime.now()
        model.save()

    return redirect(to="web:person_edit_by_id", id=person_id)
