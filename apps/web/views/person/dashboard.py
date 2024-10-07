from django.shortcuts import render

from ..utils.nav import nav
from ...models.person.person import Person as ModelPerson

# @login_required(login_url="auth:login")


def dashboard(request):

    person = ModelPerson.objects.filter(
        created_at__isnull=False,
        deleted_at__isnull=True
    )

    context = {
        "nav_core": nav,
        "person": person,
    }

    return render(request=request, template_name="pages/person/dashboard.html", context=context)
