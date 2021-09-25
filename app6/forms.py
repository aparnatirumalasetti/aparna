from django import forms
from .models import Edubridge
class EdubridgeForm(forms.ModelForm):
    class Meta:
        model=Edubridge
        fields= "__all__"
