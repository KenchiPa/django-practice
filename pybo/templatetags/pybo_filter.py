from django import template

register = template.Library()


# 애너테이션을 적용하면 템플릿에서 해당 함수를 필터로 사용 할 수 있게 된다.
@register.filter
def sub(value, arg):
    return value - arg  # 기존 값 value에서 입력으로 받은 값 arg를 빼서 return
