from django import forms
from polls.models import VendorCategory
from polls.models import Vendor


class VendorCategoryForm(forms.ModelForm):
    class Meta:
        model = VendorCategory
        fields = "__all__"


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = "__all__"
