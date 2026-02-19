from transformers import pipeline #import pipeline from transformers library

# load pretrained AI sentiment model
classifier = pipeline("sentiment-analysis")

pipeline("sentiment-analysis",
         model="cardiffnlp/twitter-roberta-base-sentiment")

# function to predict sentiment
def predict(text):
    result = classifier(text)
    return result


