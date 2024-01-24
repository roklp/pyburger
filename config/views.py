from django.http import HttpResponse

def main(request):
    return HttpResponse("반갑다, 도태훈이다.")

def burger_list(request):
    return HttpResponse("버거 목록이다.")
