import requests

def sentimentAnalysis(txt):
    # using the Sentiment Analysis API
    url = "http://text-processing.com/api/sentiment/"

    posNo = 0
    negNo = 0

    for word in txt:
        req = requests.post(url,data="text="+word)
    #    print
    #    print req.text
    #    print
        (prob, label) = req.text.split('},')
        (lb, value) = label.split(": ")
        # final value is pos, neg or neu
        val = value[1:4]

        if (val == "pos"):
            posNo += 1
        elif (val == "neg"):
            negNo += 1

    if (posNo >= negNo):
        return "HAPPYYYYY"
    else:
        return "ANGRYYYYYY"

print sentimentAnalysis(["amazing", "great", "shit"])
