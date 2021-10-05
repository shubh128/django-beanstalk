from django.http.response import HttpResponse, JsonResponse


def greeting(request):
    return HttpResponse('Hello World!')


def jsongreeting(request):
    return JsonResponse({'Hello': 'World'})
