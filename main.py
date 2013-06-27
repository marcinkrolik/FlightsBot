#!/usr/bin/python
from SkyScannerTest import *
import boto.ses
import os

def main():
    
    datacsv = 'data.csv'
    body = ''
    data = readCsv(datacsv)
    test = SkyScannerTest()
    
    for d in data:
        print "======>" + ";".join(d)
        test.setUp()
        body += "%s - %s \n%s <-> %s : %s \n" % (d[2], d[3], d[0], d[1], ";".join(test.test(d)))
        test.tearDown()
    body += "\n\nPrepared by fully automated Kromar"
    sendMail(body)
    #fileout = open('log.txt', 'w')
    #fileout.write(body)
    #fileout.close()    
#'''    
def sendMail(body):
    
    REGION = 'us-east-1'
    FROM = 'kromar.box@gmail.com'
    SUBJECT = 'Your subject'
    TO = ['marcin.krolik@gmail.com', 'zmudakat@gmail.com']
    
    conn = boto.ses.connect_to_region(REGION, aws_access_key_id = os.environ['AWSKEY'], aws_secret_access_key = os.environ['AWSPASS'])
    conn.send_email(FROM, SUBJECT, body, TO)
#'''
if __name__ == '__main__':
    main()