from django.http import HttpResponse


def index(request):
    return HttpResponse(content='У меня получилось!!! Online))')


def second_page(request):
    return HttpResponse(content='А это вторая страница!!')
