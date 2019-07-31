# coding=utf-8

"""
http://api.qingyunke.com/
青云客智能聊天机器人API
可直接使用
"""
import requests

URL = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'


def get_qingyunke(text, userId=''):
    try:
        # print('发出消息:{}'.format(text))
        resp = requests.get(URL.format(text))
        if resp.status_code == 200:
            # print(resp.text)
            re_data = resp.json()
            if re_data['result'] == 0:
                return_text = re_data['content']
                return return_text
            else:
                error_text = re_data['content']
                print('青云客机器人错误信息：{}'.format(error_text))

        print('青云客机器人获取失败')
    except Exception as e:
        print(e)
        print('青云客机器人获取失败')


get_auto_reply = get_qingyunke

if __name__ == '__main__':
    text = '少年阿宾'
    rt = get_qingyunke(text)
    print('回复：', rt)
