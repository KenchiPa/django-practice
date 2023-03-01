from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# UserForm을 따로 만들지 않고 UserCreationForm을 그대로 사용해도 되지만 아래처럼
# 이메일 등의 속성을 추가하기 위해서는 UserCreationForm 클래스를 상속하여 만들어야 한다.
class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")