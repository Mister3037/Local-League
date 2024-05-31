from django import forms

from users.models import CustomUser


class RegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email", "password", "location", "phone", )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.save()

        return user
