import os
import re

from flask import Flask, abort, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from linebot.models import MessageEvent, TextMessage, TextSendMessage

my_user_id = 'U4e2ae82cdfa65642fdb6e40744409bac'

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET',
                           '2ac67b792cac1e4668d055b0563fcf00')
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN',
                                 '+3HeydgL8vDkFK1gd13XZqCMJNZ2K/19YPse89GN3RlXcm/2oudAi7RAiOVGBZBOkWICEjqRgPv3uY7sfHT1DJfV+rXbqVg82UEiORd2o1gX/KkkVMCrDyZmVlMdgn4sXozgeSDpyjicIAPqlBrp2gdB04t89/1O/w1cDnyilFU=')
if channel_secret is None or channel_access_token is None:
    print('Specify LINE_CHANNEL_SECRET and LINE_CHANNEL_ACCESS_TOKEN as environment variables.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)
line_bot_api.push_message(my_user_id, TextSendMessage(text="start"))

# 此為 Webhook callback endpoint

@app.route("/is-server-alive")
def is_server_alive():
    return 'server is alive'

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body（負責）
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

# decorator 負責判斷 event 為 MessageEvent 實例，event.message 為 TextMessage 實例。所以此為處理 TextMessage 的 handler


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    msg = str(event.message.text).upper().strip() # 使用者輸入的內容
    # profile = line_bot_api.get_profile(event.source.user_id)
    # user_name = profile.display_name #使用者名稱
    # uid = profile.user_id # 發訊者ID

    # 決定要回傳什麼 Component 到 Channel
    if re.match("-", msg):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text))
        return
    elif re.match("SB", msg):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="我還沒完成".format(event.message.text)))
        return


if __name__ == "__main__":
    app.run(debug=True, port=9427)
