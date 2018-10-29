# coding: utf-8
from smtplib import SMTPAuthenticationError

import pytest

from day10.EmailSender import EmailSender


def test_class():
    obj = EmailSender()

    with pytest.raises(SMTPAuthenticationError):
        obj.login()
