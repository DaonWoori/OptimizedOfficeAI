from django import forms
from django.forms import ModelForm
from .models import Review_Models, User

# forms.py : 사용자로부터 입력받는 값들을 정의하는 파일

# 사용자의 데이터를 입력받을 수 있는 양식 ㅡ> 모델 폼 사용
class FileUploadForm(ModelForm):
    class Meta:
        model = Review_Models                               # 사용할 모델 불러오기
        fields = ['title', 'ratings', 'content', 'imgfile'] # 모델 필드 중 사용자의 입력이 필요한 필드 지정

# 회원 가입과 관련해 사용자로부터 얻는 데이터에 대한 form -> 이메일, 패스워드, 패스워드 확인
class RegistrationForm(forms.Form):
    
    username = forms.CharField(label='ID')
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

# 로그인과 관련해 사용자로부터 얻는 데이터에 대한 form -> 이메일, 패스워드 
class LoginForm(forms.Form):

    username = forms.CharField(label='ID')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

# 계정 탈퇴와 관련해 사용자로부터 얻는 데이터에 대한 form -> 패스 워드 (단, 로그인 상태에서 가능하므로 패스 워드만 입력 받음)
class DeleteAccountForm(forms.Form):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)