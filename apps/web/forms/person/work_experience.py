from django import forms

from ...models.person.work_experience import WorkExperience as ModelWorkExperience


class WorkExperience(forms.ModelForm):
    class Meta:
        model = ModelWorkExperience
        fields = "__all__"
        widgets = {
            "company_nm": forms.TextInput(
                attrs={
                    "class": "form-control"
                }),
            "industry": forms.TextInput(
                attrs={
                    "class": "form-control"
                }),
            "role": forms.TextInput(
                attrs={
                    "class": "form-control"
                }),
            "date_in": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }),
            "date_out": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }),
        }
