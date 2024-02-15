from django import forms
from .models import Account, Destination
from django.core.validators import URLValidator
# Import needed field
from django.forms import ModelChoiceField
from django.core.exceptions import ValidationError

# Custom Validator
def validate_json(value):
    try:
        import json
        json.loads(value)
        print(value)
        print(json.loads(value))
    except json.JSONDecodeError:
        raise ValidationError("Invalid JSON format")
    
# Create Add Record Form
class AddAccountForm(forms.ModelForm):
	email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
	account_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Account Name", "class":"form-control"}), label="")
	website = forms.CharField(
		widget=forms.widgets.TextInput(attrs={"placeholder":"Website", "class":"form-control"}),
		label="",
		validators=[URLValidator()],
		required=False)

	class Meta:
		model = Account
		fields = ('email', 'account_name', 'website')
		

class AddDestinationForm(forms.ModelForm):
    # Account Dropdown
    account = ModelChoiceField(queryset=Account.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), empty_label="Select an Account")
    url = forms.URLField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"URL", "class":"form-control"}), label="")
    http_method = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"HTTP Method", "class":"form-control"}), label="")
    headers = forms.CharField(
                widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}),
                required=True,
                label="",
            )

    
    class Meta:
        model = Destination
        fields = ('account', 'url', 'http_method', 'headers')

