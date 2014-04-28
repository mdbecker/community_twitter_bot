from twitter import *
import json
import time

auth = json.load(open('oauth.json'))
t = Twitter(auth=OAuth(
    auth['access_token'], auth['access_token_secret'], auth['api_key'],
    auth['api_secret'],
))
auth_users = auth['users']
sleep_min = t.application.rate_limit_status(resources='direct_messages')[
    'resources']['direct_messages']['/direct_messages']['limit'] / 15.0
while True:
    dm = t.direct_messages()
    for mess in dm:
        if mess['sender']['screen_name'] in auth_users and ' #rt' in mess['text']:
            out = (mess['text'].replace(' #rt', '') + ' ^{0}').format(
                auth_users[mess['sender']['screen_name']])
            print out

    print sleep_min
    time.sleep(sleep_min * 60 * 2)
