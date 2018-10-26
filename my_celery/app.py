from celery_app import task1
from celery_app import task2


result1=task1.add.delay(2,4)

result2=task2.multipy.delay(2,4)

print(result1)
print(result2)
print("end.....")