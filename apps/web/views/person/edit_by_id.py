import uuid
from datetime import datetime

from django.db.models import Q
from django.shortcuts import redirect, render

from ...forms.person.education import Education as FormEducation
from ...forms.person.person import Person as FormPerson
from ...forms.person.work_experience import \
    WorkExperience as FormWorkExperience
from ...models.person.education import Education as ModelEducation
from ...models.person.person import Person as ModelPerson
from ...models.person.work_experience import \
    WorkExperience as ModelWorkExperience
from ..utils.nav import nav

# @login_required(login_url="auth:login")


def edit_by_id(request, id):
    person = None
    try:
        person = ModelPerson.objects.get(person_id=id, deleted_at__isnull=True)
    except:
        return redirect(to="web:registration")
    # edu = ModelEducation.objects.filter(  # tampilkan yang created_atnya ada atau null dan deleted_at nya null yang person_idnya = id
    #     # ~Q(created_at__isnull=True),
    #     # created_at=None,
    #     deleted_at__isnull=True,
    #     person=id
    # )
    ModelEducation.objects.filter(
        person=id,
        updated_at__isnull=False,
        deleted_at__isnull=True,
    ).update(updated_at=None)
    edu = ModelEducation.objects.filter(
        deleted_at__isnull=True,
        updated_at__isnull=True,
        person=id,
    )

    ModelWorkExperience.objects.filter(
        person=id,
        updated_at__isnull=False,
        deleted_at__isnull=True,
    ).update(updated_at=None)
    work = ModelWorkExperience.objects.filter(
        deleted_at__isnull=True,
        updated_at__isnull=True,
        person=id,
    )

    field = FormPerson(instance=person)
    field_edu = FormEducation()
    field_work = FormWorkExperience()

    opt_gender = ModelPerson.GENDER
    opt_edu_category = ModelEducation.CATEGORY

    if request.method == "POST":
        if "add_edu" in request.POST:
            form = {
                "person": person.person_id,
                "education_nm": request.POST["education_nm"],
                "category": request.POST["category"],
                "major": request.POST["major"],
                "date_in": request.POST["date_in"],
                "date_out": request.POST["date_out"],
            }
            field_edu = FormEducation(data=form)
            if field_edu.is_valid():
                field_edu.save()
                return redirect(to="web:person_edit_by_id", id=person.person_id)

        if "add_work" in request.POST:
            form = {
                "person": person.person_id,
                "company_nm": request.POST["company_nm"],
                "industry": request.POST["industry"],
                "role": request.POST["role"],
                "date_in": request.POST["date_in"],
                "date_out": request.POST["date_out"],
            }
            field_work = FormWorkExperience(data=form)
            if field_work.is_valid():
                field_work.save()
                return redirect(to="web:person_edit_by_id", id=person.person_id)

        if "finish" in request.POST:
            form = {
                "person_id": person.person_id,
                "name": request.POST["name"],
                "email": request.POST["email"],
                "gender": request.POST["gender"],
                "age": request.POST["age"],
                "phone": request.POST["phone"],
                "photo": request.FILES["photo"] if request.FILES != {} else None,
                "address": request.POST["address"],
            }
            form.update(
                {"created_at": datetime.now()} if person.created_at == None
                else {"created_at": person.created_at, "updated_at": datetime.now()}
            )

            field = FormPerson(instance=person, data=form, files=request.FILES)
            if field.is_valid():
                field.save()
                ModelEducation.objects.filter(
                    updated_at__isnull=False,
                    person_id=id
                ).update(
                    deleted_at=datetime.now(),
                    updated_at=None
                )
                ModelEducation.objects.filter(
                    person_id=id,
                    updated_at__isnull=True,
                    deleted_at__isnull=True,
                    created_at__isnull=True,
                ).update(created_at=datetime.now())

                ModelWorkExperience.objects.filter(
                    updated_at__isnull=False,
                    person_id=id
                ).update(
                    deleted_at=datetime.now(),
                    updated_at=None
                )
                ModelWorkExperience.objects.filter(
                    person_id=id,
                    updated_at__isnull=True,
                    deleted_at__isnull=True,
                    created_at__isnull=True,
                ).update(created_at=datetime.now())

                return redirect(to="web:person_detail_by_id", id=person.person_id)

    context = {
        "nav_core": nav,
        "page": "edit_by_id",
        "field": field,
        "field_edu": field_edu,
        "field_work": field_work,
        # "field_edu": None,
        # "field_work": None,
        "person": person,
        "edu": edu,
        "work": work,
        "opt_gender": opt_gender,
        "opt_edu_category": opt_edu_category,
    }

    return render(request=request, template_name="pages/person/form/form.html", context=context)
