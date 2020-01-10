import re

import requests
from font import mapCodeToFont,mapFontToNum

class Douyin_Personal_Info(object):
    # 执行js方法 _bytedAcrawler.sign("110677980134") 对参数进行签名
    def __init__(self,uid):
        self.uid = uid
        self.share_url = f"https://www.douyin.com/share/user/{self.uid}"
        self.headers = {
            'authority': 'www.douyin.com',
            'method': 'GET',
            'path': f'/share/user/{self.uid}',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en-GB;q=0.7,en;q=0.6',
            'cache-control': 'max-age=0',
            'cookie': '_ba=BA0.2-20191216-5199e-pxdItq5zU5PtrJKeBdkE; _ga=GA1.2.2099702045.1576461845; _gid=GA1.2.733290229.1578361134',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }


    def get_code_num(self,douyin_nums):
        douyin_nums = [each.replace('&#', '0') for each in douyin_nums]
        douyin_code_nums = [mapFontToNum[mapCodeToFont[num]] for num in douyin_nums]
        code_num = ''.join(douyin_code_nums)
        return code_num

    def get_text(self):
        response = requests.get(self.share_url,headers=self.headers)
        html = response.content.decode()
        #print(html)

        # 抖音昵称
        nick_name = re.findall(r'nickname">(.*?)<',html)[0]

        # 抖音ID、抖音号、short_id
        douyin_num_text = re.findall(r'抖音ID：     (.*?)   </p>',html)[0] # 获取完整抖音ID文本
        douyin_nums_text = re.findall(r'(<i.*</i>)',douyin_num_text)[0]    # 获取只包含数字的文本
        douyin_nums = re.findall('<i class="icon iconfont "> (.*?); <',douyin_nums_text)    # 提取加密数字
        code_num = self.get_code_num(douyin_nums)   # 获得真实数字
        douyin_id = douyin_num_text.replace(douyin_nums_text,code_num)  # 得到最终的 抖音ID

        # 关注数
        focus_nums_text = re.findall('class="focus block"><span class="num">    (.*?) </span><span class="text">关注',html)[0]
        focus_nums = re.findall('follow-num"> (.*?);',focus_nums_text)
        focus_num = self.get_code_num(focus_nums)

        # 粉丝数
        follower_nums_text = re.findall('class="follower block"><span class="num">    (.*?)</span><span class="text">粉丝',html)[0]
        follower_nums = re.findall('follow-num"> (.*?);',follower_nums_text)
        follower_num = self.get_code_num(follower_nums)

        # 点赞数
        liked_nums_text = re.findall('liked-num block"><span class="num">    (.*?) </span><span class="text">赞',html)[0]
        liked_nums = re.findall('follow-num"> (.*?);',liked_nums_text)
        liked_num = self.get_code_num(liked_nums)


        print(nick_name,douyin_id,focus_num,follower_num,liked_num)


if __name__ == '__main__':
    # 89923219116
    uid = '80609982443'
    douyin = Douyin_Personal_Info(uid)
    douyin.get_text()