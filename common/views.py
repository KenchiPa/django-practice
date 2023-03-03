from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm


def signup(request):
    # POST 요청인 경우
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # form.cleaned_data.get(): 폼의 입력값을 개별적으로 얻고 싶을 경우에 사용하는 하무
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # 신규 사용자를 생성한 후에 자동 로그인 될 수 있도록 authenticate와 login 함수가 사용되었다.
            # authenticate 와 login 함수는
            # django.contrib.auth 모듈의 함수로 사용자 인증과 로그인을 담당.
            user = authenticate(username=username, password=raw_password)  # 사용자명과 비밀번호가 정확한지 검증.
            # 사용자 인증
            login(request, user)  # 로그인  사용자 세션을 생성
            return redirect('index')
    else:  # GET 요청인 경우 회원가입 화면
            form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


def page_not_found(request, exception):
    return render(request, 'common/404.html', {})


def internal_server_error(request, exception):
    return render(request, 'common/500.html', {})