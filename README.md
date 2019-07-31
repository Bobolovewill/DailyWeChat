# DailyWeChat
 
DailyWeChat 是基于 Python3 与 Itchat 的微信小工具。
可以定时给朋友或者群聊发送每日天气、提醒、每日一句，也可以智能自动回复好友信息。还有群助手功能。 操作简单，小白用户也可快速上手。
功能说明
支持对多个微信好友自动回复。
定时给好友与群聊组发送提醒，内容包括（天气、格言、自定义的话）。
群助手功能，可以群自动回复，查询最热门的垃圾分类、天气、日历、笑话、等等功能。
如果你没有好友可测试发送提醒，而且只有一个人也玩不了自动回复，怎么办呢（快哭了.jpg）。
你可以把『文件传输助手』当成女朋友添加（你说的这个女朋友到底是不是你的双手.jpg）。这样一个号也可以进行测试了，发提醒给文件传输助手，跟文件传输助手智能聊天。
1. 开启自动回复
将 is_auto_relay 设置为：True。
2.选择渠道
机器人渠道（1: 图灵机器人，2: 一个AI ,3 : 青云客，4 腾讯智能闲聊，5:天行机器人，6 海知智能)
bot_channel: 3
默认为青云客，但请注意这个回复机器人比较智障。。

3. 指定自动回复的好友名单
有两种模式

(1) 不使用自动回复所有好友的情况下，即：is_auto_reply_all：False 时。
这时设置可回复的白名单成员，如下：

is_auto_reply_all：False
# 指定自动回复的好友名单。
auto_reply_white_list:
  - '好友1'
  - '好友2'
(2) 开启自动回复所有好友的情况下，即：is_auto_reply_all：True 时。
选择不自动回复黑名单成员：如下

is_auto_reply_all：True
auto_reply_black_list:
    - '好友1'
    - '好友2'
4. 配置相关器人
除了青云客之外，其他的机器人都需要去对应的官网，注册并获取相应的 key。需要哪个就配置哪个。

图灵机器人
打开图灵机器人官网：http://www.turingapi.com 进行注册。
创建机器人，得到 apikey。将填入到 _config.yaml 文件中的：
注意：不要打开『密钥』选项。

turing_conf:
  apiKey: '你所获取apikey'
图灵机器人必须认证后才能使用，免费版用户，每天可使用 100 条信息，且用且珍惜。

天行机器人
打开天行数据注册页面：https://www.tianapi.com/signup.html 进行注册。
在个人中心的第一行，即可得到 apikey。
txapi_conf:
  app_key: '个人中心中的key'
  reply_name: '宝宝' # 回复的人的名字(可空)（也可在个人中心->机器人管理 修改）
  bot_name: '老公' # 机器人的名字（可空）
智能闲聊（腾讯）
打开 https://ai.qq.com/product/nlpchat.shtml 并登录。
点击免费使用 -> 接入能力 -> 创建应用 -> 创建成功后，会显示出 app_id ,app_key 。
点击应用管理 -> 『你创建的项目名』-> 接入能力 -> 智能闲聊 -> 了解更多 -> 接入能力->『选择项目』-> 确认接口。
将 app_id,app_key 填入 yaml 中。
qqnlpchat_conf:
    app_id: '你申请的api_id'
    app_key: '你申请的app_key'
配置「一个AI」
打开图灵机器人官网：http://www.yige.ai 进行注册。
创建应用，得到「API密钥」中的 「客户端访问令牌」
将填入到 _config.yaml 文件中的：

yigeai_conf:
  client_token: '客户访问令牌'
  首先，把 Python3 安装好，并配置好环境，个人建议新手安装 anaconda，具体安装教程，可自行谷歌搜索~

直接下载此项目或 clone 项目到本地。

使用 pip 安装依赖:

pip3 install -r requirements.txt
# 或者是使用 pip
# pip install -r requirements.txt
运行
在本地 cmd 中跳转项目目录下，运行:

python run.py
  
