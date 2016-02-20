import requests, json

url = "http://text-processing.com/api/sentiment/"

txt = "text=great"

req = requests.post(url,data=txt)
print
print req.text
print
(prob, label) = req.text.split('},')
(lb, value) = label.split(": ")
val = value[1:4]

# final value is pos, neg or neu
print val
