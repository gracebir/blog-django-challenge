from django.forms import ModelForm, CharField, PasswordInput
from .models import BlogPost
from django.contrib.auth.models import User

class UserForm(ModelForm):
    password = CharField(widget=PasswordInput(
        attrs={'class' : 'your-custom-class'})
    )
    password_confirm = CharField(widget=PasswordInput())
    class Meta:
        model = User
        fields = ['username','password']
    def clean(self):
        cleaned_data = super(UserForm(), self).clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            self.add_error("confirm_password", "Password does not match")


class BlogForm(ModelForm):
    class Meta:
        model = BlogPost
        fieds = '__all__'
        exclude = ['slug', 'author']