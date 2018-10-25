from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.
def hello(request):
    # return HttpResponse('<html>hello wb</html>')
    # return render(request,'index1.html',{'hello':'hello,blog1'})
    article = models.Article.objects.get(pk=1)
    return render(request, 'index1.html', {'article': article})

