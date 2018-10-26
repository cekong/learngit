from celery import Celery

app=Celery('demo')
#加载配置模块
app.config_from_object('celery_app.celery_config')