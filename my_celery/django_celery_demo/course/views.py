from django.shortcuts import render
from . import mytask
from django.http import JsonResponse
# Create your views here.

def do(request):
    #执行异步任务
    print('start do request')
    # mytask.CourseTask.delay()
    mytask.CourseTask.apply_async(args=('hello',),queue='work_queue')
    print('end do request')
    return JsonResponse({'result':'ok'})


