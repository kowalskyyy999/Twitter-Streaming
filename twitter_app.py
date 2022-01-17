import config  # Configuration for API KEY & ACCESS TOKEN Twiiter
import tweepy
import json
import argparse

from unidecode import unidecode

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filter", type=str, help="filter tracking tweets")
args = parser.parse_args()


class TweetStreamer(tweepy.Stream):
    def on_data(self, data):
        try:
            messages = json.loads(data.decode('utf-8'))
            text = messages['text']
            print(text)
            return True
        
        except BaseException as e:
            print('Error on data: %s' %str(e))

        return True

    def on_request_error(self, status):
        print(status)
        return True
    
def main():
    stream = TweetStreamer(config.API_KEY, config.API_KEY_SECRET, 
            config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
    stream.filter(track=[args.filter])


if __name__ == "__main__":
    main()


