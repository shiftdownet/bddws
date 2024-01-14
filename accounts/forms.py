from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm


from .models import CustomUser


class LoginFrom(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label = '社員番号'
        self.fields['password'].label = 'パスワード'
        self.fields['username'].widget.attrs['placeholder'] = '0000000 (7桁)'
        self.fields['password'].widget.attrs['placeholder'] = '半角英数字８文字以上'

    class Meta:
        model = CustomUser


class SetPasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['old_password'].label = '古いパスワード'
        self.fields['new_password1'].label = '新しいパスワード'
        self.fields['new_password2'].label = '新しいパスワード(確認用)'
        self.fields['old_password'].widget.attrs['placeholder'] = ''
        self.fields['new_password1'].widget.attrs['placeholder'] = '半角英数字８文字以上'
        self.fields['new_password2'].widget.attrs['placeholder'] = ''
