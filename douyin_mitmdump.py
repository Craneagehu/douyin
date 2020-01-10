import json

#函数名必须这样写 这是mitmdump规则
def response(flow):
    #下面这个网址是通过fiddler获取到的 但是有些数据我们无法解密，所以需要用mitmdump捕获数据包然后做分析
    # https://api.amemv.com/aweme/v1/user/follower/list/?user_id=96285518522&max_time=1576833686&count=20&retry_type=no_retry&iid=50691884166&device_id=39192129332&ac=wifi&channel=update&aid=1128&app_name=aweme&version_code=321&version_name=3.2.1&device_platform=android&ssmix=a&device_type=vivo+X9&device_brand=vivo&language=zh&os_api=25&os_version=7.1.2&uuid=864555034836351&openudid=8a6b32f84529b1d7&manifest_version_code=321&resolution=1080*1920&dpi=480&update_version_code=3212&_rticket=1576833686698&ts=1576833685&js_sdk_version=1.2.2&as=a1c5c99fc5594dd2fc6555&cp=9992da5f56ccff23e1Ui]m&mas=0184dbbbc985699dabb3d6e7e6dfc0b2edacacac6cc6664c26262c
    if 'aweme.snssdk.com/aweme/v1/user/follower/list' in flow.request.url:
        # amemv.com/aweme/v1/user/follower/list  --> 手机
        #  https://aweme.snssdk.com/aweme/v1/user/follower/list/?user_id=96285518522  --》模拟器
        for user in json.loads(flow.response.text)['followers']:
            user_info={}
            user_info['nickname'] = user['nickname']
            user_info['share_id'] = user['uid']
            user_info['douyin_id'] = user['short_id']
            #有的用户修改了抖音号
            if user_info['douyin_id'] == '0':
                user_info['douyin_id'] = user['unique_id']
            print(user_info)
 


