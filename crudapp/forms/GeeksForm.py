from django import forms
from .models import GeeksModel



class GeekForm(forms.ModelForm):
    class Meta:
        model=GeeksModel
        
        fields=[
			"title",
			"description"
		]