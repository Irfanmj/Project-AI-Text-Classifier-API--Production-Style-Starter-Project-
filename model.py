from transformers import pipeline #import pipeline from transformers library

# load pretrained AI sentiment model
classifier = pipeline("sentiment-analysis")

# function to predict sentiment
def predict(text):
    result = classifier(text)
    return result

pipeline("sentiment-analysis",
         model="cardiffnlp/twitter-roberta-base-sentiment")
