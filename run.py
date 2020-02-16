from slack import RTMClient
from pprint import pprint
from slackbot_settings import slack_token
import pathlib

from slack2cups.slack2cups import Slack2Cups

user_data = {}
s2c = Slack2Cups(pathlib.Path(__file__).resolve().parent)


def main():
    rtm_client = RTMClient(token=slack_token)
    rtm_client.start()


@RTMClient.run_on(event="message")
def get_print_data(**payload):
    global user_data
    data = payload['data']
    web_client = payload['web_client']
    pprint(data.keys())

    pprint(data)
    if "bot_id" in data:
        pass
    elif "text" in data:
        user_data.setdefault(data['user'], False)
        text_from_users = data['text']
        channel_id = data['channel']
        thread_ts = data['ts']
        # user = data['user']
        if user_data[data['user']]:
            if 'Yes' in text_from_users:
                web_client.chat_postMessage(
                    channel=channel_id,
                    text="Starting to print...",
                    thread_ts=thread_ts
                )
                s2c.text2pdf(user_data[data['user']])
            else:
                web_client.chat_postMessage(
                    channel=channel_id,
                    text="Canceled",
                    thread_ts=thread_ts
                )
            user_data[data['user']] = False
        else:
            web_client.chat_postMessage(
                channel=data['channel'],
                text="Are you sure to print this {}".format(data['text']),
                thread_ts=data['ts']
            )
            user_data[data['user']] = data['text']


if __name__ == "__main__":
    main()
