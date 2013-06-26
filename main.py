#!/usr/bin/python
from SkyScannerTest import *
import boto.ses
import os

def main():
    
    body = ''
    
    data = (("GDN", "MNL", "10.07.2013", "10.08.2013"),
            ("GDN", "CGK", "10.07.2013", "10.08.2013"),
            ("WAW", "CGK", "10.08.2013", "10.09.2013"),
            ("WAW", "CGK", "10.09.2013", "10.10.2013"))
    test = SkyScannerTest()
    
    for d in data:
        test.setUp()
        body += "%s - %s \n%s <-> %s : %s \n" % (d[2], d[3], d[0], d[1], ";".join(test.test(d)))
        test.tearDown()
    body += "\n\nPrepared by fully automated Kromar"
    sendMail(body)    
    #test.setUp()
    #r2 = test.test(d[1])
    #test.tearDown()
    
    #print r1
    #print r2
def sendMail(body):
    
    REGION = 'us-east-1'
    FROM = 'kromar.box@gmail.com'
    SUBJECT = 'Your subject'
    BODY = 'Body here'
    TO = ['marcin.krolik@gmail.com', 'zmudakat@gmail.com']
    
    conn = boto.ses.connect_to_region(REGION, aws_access_key_id = os.environ['AWSKEY'], aws_secret_access_key = os.environ['AWSPASS'])
    conn.send_email(FROM, SUBJECT, body, TO)

if __name__ == '__main__':
    main()