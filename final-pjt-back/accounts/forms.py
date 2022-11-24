from django import forms
from .models import User, ProfileImage

class ProfileImageForm(forms.ModelForm):
    
    class Meta:
        model = ProfileImage
        fields = ('profile_image',)

    