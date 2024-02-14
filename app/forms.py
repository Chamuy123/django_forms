from django import *
from app.models import *

class Topic_forms(forms.Form):
    tname=forms.CharField()

def validator_for_webpage(Data):
    if Data.lower().startswith("a"):
        raise forms.ValidationError('starts with a')

def validator_for_webpagelen(Data):
    if len(Data)<5:
        raise forms.ValidationError('lenth of webpage')

class Webpage_forms(forms.Form):
    tl=[[to.tname,to.tname] for to in Topic.objects.all()]
    tname=forms.ChoiceField(choices=tl)
    name=forms.CharField(validators=[validator_for_webpage,validator_for_webpagelen])
    email=forms.EmailField(validators=[validator_for_webpage])
    re_email=forms.EmailField()
    url=forms.URLField()
    pw=forms.CharField(widget=forms.PasswordInput)
    re_pw=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['re_email']
        p=self.cleaned_data['pw']
        rp=self.cleaned_data['re_pw']
        if e != re or p!=rp :
            raise forms.ValidationError('confirmation data ')


class Accessrecord_forms(forms.Form):
    al=[[wo.pk,wo.name] for wo in Webpage.objects.all()]
    name=forms.ChoiceField(choices=al)
    author=forms.CharField()
    date=forms.DateField()
