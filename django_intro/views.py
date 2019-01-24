from django.http import HttpResponse
from django.shortcuts import render
import random



def index(request):
    return HttpResponse("Hello!!")
    
def html_tag(request):
    s = "<h1>안녕하세요</h1>"
    return HttpResponse(s)

def dinner(request):
    d_list = random.choice(["삼겹살", "치킨", "피자", "갈비"])
    return HttpResponse(d_list)
    
def lotto(request):
    num = random.sample(range(1,46),6)
    return HttpResponse(num)
    
def html_file(request):
    
    return render(request,"html_file.html")
