from django.shortcuts import redirect, render

from ...forms.person.person import Person as FormPerson
from ...models.person.person import Person as ModelPerson
from ...models.person.education import Education as ModelEducation
from ...models.person.work_experience import WorkExperience as ModelWorkExperience
from ..utils.nav import nav


# @login_required(login_url="auth:login")
def detail_by_id(request, id):
    person = None
    opt_gender = ModelPerson.GENDER
    try:
        person = ModelPerson.objects.get(person_id=id, deleted_at__isnull=True)
    except:
        return redirect(to="web:registration")
    field = FormPerson(instance=person)

    edu = ModelEducation.objects.filter(
        created_at__isnull=False,
        deleted_at__isnull=True,
        person=id,
    )
    work = ModelWorkExperience.objects.filter(
        created_at__isnull=False,
        deleted_at__isnull=True,
        person=id,
    )

    context = {
        "nav_core": nav,
        "page": "detail_by_id",
        "field": field,
        # "field_edu": field_edu,
        # "field_work": field_work,
        "person": person,
        "opt_gender": opt_gender,
        "edu": edu,
        "work": work
    }

    return render(request=request, template_name="pages/person/form/form.html", context=context)
