from django import forms

from ...models.person.person import Person as ModelPerson


class Person(forms.ModelForm):
    class Meta:
        model = ModelPerson
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control"
                }),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control"
                }),
            "gender": forms.Select(
                attrs={
                    "class": "form-select",
                }),
            "age": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": "1"
                }),
            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "minlength": "10",
                    "maxlength": "20"
                }),
            "photo": forms.FileInput(
                attrs={
                    "class": "form-control"
                }),
            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": "7"
                }),
        }
