from django import template
import markdown
from django.utils.safestring import mark_safe
register = template.Library()


# 애너테이션을 적용하면 템플릿에서 해당 함수를 필터로 사용 할 수 있게 된다.
@register.filter
def sub(value, arg):
    return value - arg  # 기존 값 value에서 입력으로 받은 값 arg를 빼서 return


# markdown 모듈과 mark_safe 함수를 이용하여 입력 문자열을 HTML로 변환하는 필터 함수이다.
# 마크다운에는 몇 가지 확장 기능이 있는데 파이보는 위처럼 nl2br과 fenced_code를 사용하도록 설정.
# nl2br은 줄바꿈 문자를 <br> 로 바꾸어 준다.
# fenced_code 는 위에서 살펴본 마크다운의 소스코드 표현을 위해 필요하다.
@register.filter
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))