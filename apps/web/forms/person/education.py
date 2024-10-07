from django import forms

from ...models.person.education import Education as ModelEducation


class Education(forms.ModelForm):
    class Meta:
        model = ModelEducation
        fields = "__all__"
        widgets = {
            "education_nm": forms.TextInput(
                attrs={
                    "class": "form-control"
                }),
            "category": forms.Select(
                attrs={
                    "class": "form-control"
                }),
            "major": forms.TextInput(
                attrs={
                    "class": "form-control"
                }),
            "date_in": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }),
            "date_out": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }),
        }
