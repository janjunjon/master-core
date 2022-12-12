import os
from slack_sdk import WebClient
from dotenv import load_dotenv
load_dotenv()

class Slack:
    @classmethod
    def notification(cls, description):
        slack_token = os.environ["SLACK_BOT_USER_OAUTH_TOKEN"]
        slack_channel = os.environ["SLACK_CHANNEL_ID"]
        slack_client = WebClient(token=slack_token)
        slack_client.chat_postMessage(
            channel=slack_channel,
            text=f'<@U04EH1W4STY> {description}'
        )