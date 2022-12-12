from django.forms import ModelForm

from .models import Customer


class CustomerCreationForm(ModelForm):
    class Meta:
        model = Customer
        fields = (
            "phone",
            "identity_type",
            "identity_number",
        )
