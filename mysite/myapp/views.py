from django.shortcuts import render
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def home(request):
    html = """
    <html>
        <body>
            <h1>Добро пожаловать на мой первый Django сайт!</h1>
            <p>Здесь я буду практиковаться и изучать Django.</p>
        </body>
    </html>
    """
    logger.info(f"Главная страница была посещена с IP: {request.META.get('REMOTE_ADDR')}")
    return HttpResponse(html)

def about(request):
    html = """
    <html>
        <body>
            <h1>Немного обо мне</h1>
            <p>Меня зовут Виталий, и я начинающий разработчик на Django.</p>
        </body>
    </html>
    """
    logger.info(f"Страница 'О себе' была посещена с IP: {request.META.get('REMOTE_ADDR')}")
    return HttpResponse(html)


# Create your views here.
