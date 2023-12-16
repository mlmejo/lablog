from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "student_name",
            "student_id",
            "year_level",
            "course",
            "department",
            "time",
            "date",
        ]
        widgets = {
            "time": forms.TimeInput(attrs={"type": "time"}),
            "date": forms.DateInput(attrs={"type": "date"}),
        }
