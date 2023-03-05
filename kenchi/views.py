from django.shortcuts import render

import logging
logger = logging.getLogger('kenchi')

# Create your views here.


def index(request):
    logger.info("INFO 레벨로 출력")
    return render(request, 'kenchi/index.html', {})