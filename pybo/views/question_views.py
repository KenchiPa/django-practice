from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question


@login_required(login_url='common:login')
def question_create(request):
        # POST 요청
        if request.method == 'POST':
                print("question_create POST 요청으로 들어왔다.")
                form = QuestionForm(request.POST)  # request.POST에 담긴 subject, content 값이 QuestionForm의 subject, content 속성에 자동으로 저장되어 객체가 생성
                # 폼이 유효하다면: form에 저장된 subject, content의 값이 올바르지 않다면 form에는 오류 메시지가 저장
                if form.is_valid():
                        question = form.save(commit=False)  # 임시 저장하여 question 객체를 리턴
                        question.author = request.user  # author 속성에 로그인 계정 저장
                        question.create_date = timezone.now()  # 실제 저장을 위해 작성일시를 설정
                        question.save()  # 데이터를 실제로 저장
                        return redirect('pybo:index')
        # GET 요청
        else:
                form = QuestionForm()
        context = {'form': form}
        # return render(request, 'pybo/question_form1.html', context)
        return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_modify(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        if request.user != question.author:
                messages.error(request, '수정권한이 없습니다.')  # messages는 장고가 제공하는 모듈로 넌필드 오류(non-field error)를 발생시킬 경우에 사용.
                return redirect('pybo:detail', question_id=question_id)
        if request.method == "POST":
                form = QuestionForm(request.POST, instance=question)  # request.POST의 값으로 덮어쓴다.
                if form.is_valid():
                        question = form.save(commit=False)
                        question.modify_date = timezone.now()  # 수정일시 저장
                        question.save()
                        return redirect('pybo:detail', question_id=question.id)
        else:
                form = QuestionForm(instance=question)  # GET요청인 경우 질문수정 화면에 조회된 질문의 제목과 내용이 반영될 수 있도록.
                                                        # 폼 생성시 이처럼 instance 값을 지정하면 폼의 속성 값이 instance의 값으로 채워진다.
        context = {'form': form}
        return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_delete(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        if request.user != question.author:
                messages.error(request, '삭제권한이 없습니다.')
                return redirect('pybo:detail', question_id=question_id)
        question.delete()
        return redirect('pybo:index')


@login_required(login_url='common:login')
def question_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question.id)

