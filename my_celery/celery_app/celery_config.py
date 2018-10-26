from datetime import timedelta
from celery.schedules import crontab

BROKER_URL='redis://:foobared@localhost:6379/1'

CELERY_RESULT_BACKEND='redis://:foobared@localhost:6379/2'

CELERY_TIMEZONE='Asia/Shanghai'

#导入指定的任务模块
CELERY_IMPORTS=(
    'celery_app.task1',
    'celery_app.task2'
)

'''
#导入定时任务模块
#每10s执行一次task1
#每天16：24执行一次task2
'''
CELERYBEAT_SCHEDULE={
    'task1':{
        'task':'celery_app.task1.add',
        'schedule':timedelta(seconds=10),
        'args':(2,8)
    },
    'task2': {
        'task': 'celery_app.task2.multipy',
        'schedule': crontab(hour=16,minute=31),
        'args': (2, 5)
    }

}