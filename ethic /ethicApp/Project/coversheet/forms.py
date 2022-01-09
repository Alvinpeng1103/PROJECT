from django import forms

ROLE_CHOICES = [('chiefinvestigator', 'chiefinvestigator'), ('others', 'others')]
OTHER_CHOICES = [('Yes', "Yes"), ('No', "No")]

class CoverSheetForm(forms.Form):

    summary = forms.CharField(widget=forms.Textarea(attrs = {"rows":"8", "cols": "150"}))
    protocol = forms.CharField(widget=forms.Textarea(attrs = {"rows":"2", "cols": "150"}))
    investigatorname = forms.CharField(widget=forms.Textarea(attrs = {"rows":"1", "cols": "50"}))
    investigatorid = forms.CharField(widget=forms.Textarea(attrs = {"rows":"1", "cols": "50"}))
    center = forms.CharField(widget=forms.Textarea(attrs = {"rows":"1", "cols": "50"}))
    role = forms.ChoiceField(choices = ROLE_CHOICES, initial = "chiefinvestigator")
    otherinternalinvestigators = forms.ChoiceField(choices = OTHER_CHOICES,  initial = "No")
    internalinvestigatorsnumber = forms.CharField(widget=forms.NumberInput(attrs = {"min":"0", "max": "100", "value": "0"}))
    otherexternalinvestigators = forms.ChoiceField(choices = OTHER_CHOICES,  initial = "No")
    externalinvestigatorsnumber = forms.CharField(widget=forms.NumberInput(attrs = {"min":"0", "max": "100", "value": "0"}))
    responsible = forms.CharField(widget=forms.Textarea(attrs = {"rows":"1", "cols": "150"}))
    currentstate = forms.CharField(widget=forms.Textarea(attrs = {"rows":"1", "cols": "150"}))
    HRECname = forms.CharField(widget=forms.Textarea(attrs = {"rows":"1", "cols": "150"}))
    action = forms.CharField(widget=forms.Textarea(attrs = {"rows":"3", "cols": "150"}))
    title = forms.CharField(widget=forms.Textarea(attrs = {"rows":"1", "cols": "150"}))
    contractaction = forms.CharField(widget=forms.Textarea(attrs = {"rows":"3", "cols": "150"}))
    otherrelevantdetails = forms.CharField(widget=forms.Textarea(attrs = {"rows":"8", "cols": "150"}))
    
    
    






    



