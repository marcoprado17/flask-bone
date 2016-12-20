# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
from flask import url_for, render_template, current_app, g
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message
from extensions import mail
from src.r import R


class EmailManager:
    def __init__(self):
        pass

    def send_register_email(self, recipient_email):
        app = current_app._get_current_object()
        ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])
        token = ts.dumps(recipient_email, salt=app.config["EMAIL_TOKEN_SALT"])

        g.confirm_url = url_for('register.email_confirmed', token=token, _external=True)
        g.email = recipient_email

        html = render_template("email/register.html")
        message = Message(sender=app.config["MAIL_USERNAME"], recipients=[recipient_email], subject=R.string.email.register.subject % dict(title=R.string.micro_blog), html=html)
        mail.send(message)
