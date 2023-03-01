from django.http import HttpResponse
# from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
        page = request.GET.get('page', '1')  # 페이지  default
        question_list = Question.objects.order_by('-create_date')
        paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
        page_obj = paginator.get_page(page)  # 해당 페이지의 데이터만 조회하도록 쿼리가 변경된다.
        context = {'question_list': page_obj}
        return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
        # question = Question.objects.get(id=question_id)
        question = get_object_or_404(Question, pk=question_id)
        context = {'question': question}
        return render(request, 'pybo/question_detail.html', context)

# answer_create, question_create 함수는 함수내에서 request.user를 사용하므로 로그인이 필요한 함수이다.
# 로그아웃 상태에서 @login_required 어노테이션이 적용된 함수가 호출되면 자동으로 로그인 화면으로 이동

@login_required(login_url='common:login')
def answer_create(request, question_id):
        """
        pybo 답변등록
        """
        question = get_object_or_404(Question, pk=question_id)
        if request.method == "POST":
                form = AnswerForm(request.POST)
                if form.is_valid():
                        answer = form.save(commit=False)
                        answer.author = request.user  # author 속성에 로그인 계정 저장
                        answer.create_date = timezone.now()
                        answer.question = question
                        answer.save()
                        return redirect('pybo:detail', question_id=question.id)
        else:
                form = AnswerForm()
                # return HttpResponseNotAllowed('Only POST is possible.')
        context = {'question': question, 'form': form}
        return render(request, 'pybo/question_detail.html', context)

        # 1 ForeignKey로 연결되어있을때 사용할 수 있는 방법
        ##question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
        # 2 Answer 모델을 직접 사용하는 방법
        ##answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
        ##answer.save()
        ##return redirect('pybo:detail', question_id=question.id)


@login_required(login_url='common:login')
def question_create(request):
        # POST 요청
        if request.method == 'POST':
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