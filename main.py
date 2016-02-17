from bs4 import BeautifulSoup
import requests

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import smtplib

#had to use smtp for work, feel free to use anything you like
def sendEmail(msgss):
    fromaddr = "me@mail"
    toaddr = "to@mail"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "FireEye Notification Alert"

    body = msgss
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.server', port)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


def loginAndCheck():
    url = 'https:url/'  #url to fireEye login page

    session = requests.session()

    client= session.get(url, verify = False)

    bsObj = BeautifulSoup(client.text, 'html.parser')
    csrftoken = bsObj.find(attrs={"name":"csrf-token"})['content']

    logindata = {'authenticity_token': csrftoken,
        'user[account]': 'username',
        'user[password]': 'password'}

    session.post(url, data=logindata) # login and send data

    client = session.get('https://url/botnets/host', verify = False)  # url to the hosts page
    bsObj = BeautifulSoup(client.text, 'html.parser')


    table = bsObj.find(class_ = "tableMain")
    issues = table.find_all("div", {"class": "severity-container"})
    counter = 0
    for issue in issues:
        print issue['title']
        if issue['title'] != 'Minor':
                counter = counter + 1

    msg = (str(counter) + ' IPs need to be dealt with ASAP on FireEye')
    print msg
    if(counter > 0):
        sendEmail(msg)
        print 'email sent'
    else:
        sendEmail('no fireEye issues')
        print 'email sent'


loginAndCheck()
