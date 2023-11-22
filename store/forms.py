import phonenumbers

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailField

from store.models import *


class UserCreationFormWithEmail(UserCreationForm):
    email = EmailField(label="Email address", required=True, help_text="Required.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class ClientForm(forms.ModelForm):
    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if not phone:
            raise forms.ValidationError("Input your phone number")
        try:
            parsed_phone = phonenumbers.parse(phone, None)
            if not phonenumbers.is_possible_number(parsed_phone):
                raise forms.ValidationError("Wrong number")
        except phonenumbers.NumberParseException as error:
            raise forms.ValidationError(error.args[0])
        return phonenumbers.format_number(
            parsed_phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL
        )

    class Meta:
        model = Client
        fields = ["name", "email", "phone"]


class DealershipForm(forms.ModelForm):
    class Meta:
        model = Dealership
        fields = ["name", "clients", "available_car_types"]


class CarTypeForm(forms.ModelForm):
    class Meta:
        model = CarType
        fields = ["brand", "model_auto", "price"]


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["car_type", "color", "year", "blocked_by_order", "owner"]
        exclude = ["blocked_by_order", "owner"]


class OrderForm(forms.Form):
    dealership = forms.ModelChoiceField(queryset=Dealership.objects.all())
    client = forms.ModelChoiceField(queryset=Client.objects.all())
    car = forms.ModelMultipleChoiceField(
        queryset=Car.objects.filter(blocked_by_order__isnull=True).filter(
            owner__isnull=True
        )
    )


class QuantityForm(forms.ModelForm):
    class Meta:
        model = OrderQuantity
        fields = ["order", "quantity", "is_paid"]
