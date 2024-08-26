from django import forms
from .models import student

class studentForm(forms.ModelForm):
    class Meta:
        model = student
        fields =  ['studentId', 'firstName', 'lastname', 'emailAdd', 'sex', 'birthday', 'course', 'yearLevel', 'status', 'address', 'image']
       
        