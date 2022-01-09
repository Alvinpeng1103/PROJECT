from django.forms import ModelForm


from accounts.models import Application

class PISform(ModelForm):
    class Meta:
        model=Application
        fields=['PIS_rt']

class PCFform(ModelForm):
    class Meta:
        model=Application
        fields=['PCF_rt']