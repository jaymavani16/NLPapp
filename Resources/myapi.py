import paralleldots

class API:

    def __init__(self):
        paralleldots.set_api_key('SYFV1bRbnd5wAVH32OTAfUysCETDDtw6knKph1YSP70')

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response

    def named_entity_recognise(self,text):
        response = paralleldots.ner(text)
        return response

    def Abuse_detect(self,text):
        response = paralleldots.abuse(text)
        return response