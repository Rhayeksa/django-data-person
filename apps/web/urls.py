from django.urls import path

# from .view.auth.login import login
from .views.person.cancel_by_id import cancel_by_id as person_cancel_by_id
from .views.person.dashboard import dashboard as person_dashboard
from .views.person.delete_by_id import detele_by_id as person_detele_by_id
from .views.person.delete_edu_by_id import \
    delete_edu_by_id as person_delete_edu_by_id
from .views.person.delete_work_by_id import \
    delete_work_by_id as person_delete_work_by_id
from .views.person.detail_by_id import detail_by_id as person_detail_by_id
from .views.person.edit_by_id import edit_by_id as person_edit_by_id
from .views.person.registration import registration

app_name = "web"


urlpatterns = [
    # person
    path(route="", view=registration, name="registration"),
    path(route="person/", view=person_dashboard, name="person"),
    path(route="cancel/<str:id>/", view=person_cancel_by_id,
         name="person_cancel_by_id"),
    path(route="edit/<str:id>/", view=person_edit_by_id, name="person_edit_by_id"),
    path(route="detail/<str:id>/", view=person_detail_by_id,
         name="person_detail_by_id"),
    path(route="delete/<str:id>/", view=person_detele_by_id,
         name="person_detele_by_id"),
    path(route="delete-edu/<str:person_id>/<int:id>", view=person_delete_edu_by_id,
         name="person_delete_edu_by_id"),
    path(route="delete-work/<str:person_id>/<int:id>", view=person_delete_work_by_id,
         name="person_delete_work_by_id"),

]
