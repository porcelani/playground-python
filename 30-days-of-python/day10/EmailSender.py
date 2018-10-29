# coding: utf-8

import smtplib


class EmailSender:

    def __init__(self):
        pass

    def login(self):
        host = "smtp.gmail.com"
        port = 587
        username = "user"
        password = "pass"

        email_conn = smtplib.SMTP(host, port)
        email_conn.ehlo()
        email_conn.starttls()
        email_conn.login(username, password)
