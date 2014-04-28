from twitter import *
from twitter.api import TwitterHTTPError
import json
import time

conf = json.load(open('config.json'))
t = Twitter(auth=OAuth(
    conf['access_token'], conf['access_token_secret'], conf['api_key'],
    conf['api_secret'],
))
conf_users = conf['users']
sleep_min = t.application.rate_limit_status(resources='direct_messages')[
    'resources']['direct_messages']['/direct_messages']['limit'] / 15.0
screen_name = t.account.settings()['screen_name']
while True:
    try:
        dm = t.direct_messages()
        for mess in dm:
            if mess['sender']['screen_name'] in conf_users and u' #rt' in mess['text']:
                out = (mess['text'].replace(u' #rt', u'') + u' ^{0}').format(
                    conf_users[mess['sender']['screen_name']])
                print out
                my_tweets = set([m['text'] for m in
                    t.statuses.user_timeline(screen_name=screen_name,
                        count=200)])
                print out in my_tweets
                if out not in my_tweets:
                    t.statuses.update(status=out)
                t.direct_messages.destroy(_id=mess['id'])

        print sleep_min
        time.sleep(sleep_min * 60 + 10)
    except TwitterHTTPError:
        print 'error, backing off'
        time.sleep(sleep_min * 15 * 60)
