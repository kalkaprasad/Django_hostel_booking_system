from django import forms
from kp1.models import Employee
# it is the models which are created in models python files
class Employeeform(forms.ModelForm):
    class Meta:
        model=Employee # it call the  models
        fields= "__all__" # here create the filed
