import requests
import paralleldots

paralleldots.set_api_key("Enter your API key here")
class api:
    def get_sentiment(self,sentiment):

        return paralleldots.sentiment(sentiment)


    def get_ner(self,ner):
        return paralleldots.ner(ner)

    def get_emotion(self, text):
        return paralleldots.summarize(text)