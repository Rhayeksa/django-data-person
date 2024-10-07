import uuid

from django.shortcuts import redirect, render

from ...forms.person.person import Person as FormPerson
from ...models.person.education import Education as ModelEducation
from ...models.person.person import Person as ModelPerson
from ...models.person.work_experience import \
    WorkExperience as ModelWorkExperience
from ..utils.nav import nav

# @login_required(login_url="auth:login")


def registration(request):

    # ModelPerson.objects.filter(created_at=None).delete() # delete person yang created_at == none dan lewat dari hari sekarang
    # ModelEducation.objects.filter(created_at=None).delete() # delete education yang created_at == none dan lewat dari hari sekarang
    # ModelWorkExperience.objects.filter(created_at=None).delete() # delete work_experience yang created_at == none dan lewat dari hari sekarang

    if request.method == "POST":
        form = {
            # "csrfmiddlewaretoken": request.POST["csrfmiddlewaretoken"],
            "person_id": uuid.uuid4(),
            "name": request.POST["name"],
            "email": request.POST["email"],
            "gender": request.POST["gender"],
            "age": request.POST["age"],
            "phone": request.POST["phone"],
            "photo": request.FILES["photo"] if request.FILES != {} else None,
            "address": request.POST["address"],
        }
        field = FormPerson(data=form, files=request.FILES)
        if field.is_valid():
            field.save()  # untuk sementara
            # logic save field use SQLAlchemy # best nya
            return redirect(to="web:person_edit_by_id", id=form["person_id"])
    else:
        field = FormPerson()

    context = {
        "nav_core": nav,
        "page": "registration",
        "field": field
    }

    return render(request=request, template_name="pages/person/form/form.html", context=context)
