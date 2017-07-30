import time
import requests
def sarahah_post(user, msg):
    s = requests.Session()

    homeurl = 'https://' + user + '.sarahah.com/'
    home = s.get(homeurl)

    csrftoken = home.text.split(
        '<input name="__RequestVerificationToken" type="hidden" value="')[1].split('"')[0]
    recipientid = home.text.split('<input id="RecipientId" type="hidden" value="')[1].split('"')[0]

    msgurl = homeurl + 'Messages/SendMessage'
    headers = {
        'Origin': 'https://' + user + '.sarahah.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': '*/*',
        'Referer': 'https://' + user + '.sarahah.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.8',
        'X-Requested-With': 'XMLHttpRequest',
    }
    data = {
        '__RequestVerificationToken': csrftoken,
        'userId': recipientid,
        'text': msg,
    }

    #print(msgurl)
    #print(data)
    #print(headers)

    r = s.post(msgurl, data=data, headers=headers)
    if (r.status_code == "200"):
        print("[Sarahah Spammer] ~ successfully sent a message to %s".format(user)) 
    #print(r.text)

while(True):
    sarahah_post("username", "content")
    time.sleep(1)
