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

        from_email = "email@gmail.com"
        to_list = ["to@gmail.com"]

        email_conn = smtplib.SMTP(host, port)
        email_conn.ehlo()
        email_conn.starttls()
        email_conn.login(username, password)
        email_conn.sendmail(from_email, to_list, "Hello there this is an email message")
        email_conn.quit()
