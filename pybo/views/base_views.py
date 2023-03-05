from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from ..models import Question
import logging
logger = logging.getLogger('pybo')


def index(request):
    logger.info("INFO 레벨로 출력")
    return render(request, 'kenchi/index.html', {})


def base(request):
    page = request.GET.get('page', '1')  # 페이지  default
    kw = request.GET.get('kw', '')  # 검색어
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            # filter 함수에서 모델 속성에 접근하기 위해서는 이처럼 __(언더바 2개) 를 이용하여 하위 속성에 접근할 수 있다.
            # subject__contains=kw 대신 subject__icontains=kw 을 사용하면 대소문자를 가리지 않고 찾아 준다.
            Q(subject__icontains=kw) |  # 제목 검색 제목에 kw 문자열이 포함되었는지를 의미.
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)  # 해당 페이지의 데이터만 조회하도록 쿼리가 변경된다.
    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)