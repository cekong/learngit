import time
import TencentYoutuyun

appid = 'xxx'
secret_id = 'xxxxxxx'
secret_key = 'xxxxxxxx'
userid= 'xxx'

#end_point = TencentYoutuyun.conf.API_TENCENTYUN_END_POINT  # 腾讯云
#end_point = TencentYoutuyun.conf.API_YOUTU_VIP_END_POINT   # 人脸核身服务(需联系腾讯优图商务开通权限，否则无法使用)
end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT        # 优图开放平台


youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)

ret = youtu.fooddetect('you_path_one.jpg',data_type = 0, seq = '')
print(ret)