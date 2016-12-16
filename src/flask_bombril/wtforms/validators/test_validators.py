# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
from unittest import TestCase

from flask_wtf import FlaskForm
from wtforms import Field, StringField
from wtforms import ValidationError

from app_contexts.unit_test_app import unit_test_app as app
from flask_bombril.r import R
from flask_bombril.wtforms.validators.validators import Required, Email, Unique, Length
from src.extensions import db


class User(db.Model):
    email = db.Column(db.String(256), primary_key=True, unique=True)


class AlwaysError(object):
    def __init__(self):
        pass

    def __call__(self, form, field):
        raise ValidationError("AlwaysError")


@app.route("/", methods=["POST"])
def required():
    return ""


class TestValidators(TestCase):
    # ==================================================================================================================
    #
    #
    #
    #
    # Required Validator
    # ==================================================================================================================
    class RequiredMockForm(FlaskForm):
        field = Field(validators=[Required()])

    class RequiredMockFormWithAlwaysError(FlaskForm):
        field = Field(validators=[Required(), AlwaysError()])

    def test_required(self):
        with app.test_client() as c:
            # Testing validator call
            c.post("/", data=dict(
                field="a"
            ))
            form = self.RequiredMockForm()
            self.assertTrue(form.validate_on_submit())

            c.post("/")
            form = self.RequiredMockForm()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)
            self.assertEqual(form.field.errors[0], R.string.validators.required_field)

            c.post("/", data=dict(
                field=None
            ))
            form = self.RequiredMockForm()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)
            self.assertEqual(form.field.errors[0], R.string.validators.required_field)

            # Testing validator stop
            # stop=True
            c.post("/")
            form = self.RequiredMockFormWithAlwaysError()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)

    # ==================================================================================================================
    #
    #
    #
    #
    # Email Validator
    # ==================================================================================================================
    class EmailMockForm(FlaskForm):
        email = Field(validators=[Email()])

    class EmailMockFormStopTrueWithAlwaysError(FlaskForm):
        email = Field(validators=[Email(stop=True), AlwaysError()])

    class EmailMockFormStopFalseWithAlwaysError(FlaskForm):
        email = Field(validators=[Email(stop=False), AlwaysError()])

    def test_email(self):
        with app.test_client() as c:
            # Testing validator call
            valid_emails = [
                "marco.pdsv@gmail.com",
                "cp.vidoca@bol.com.br",
                "marcoprado17@hotmail.com",
                "ab@b.com",
                "marco aurelio@gmail.com"
            ]
            invalid_emails = [
                "marco@@",
                "@gmail.com",
                "@gmail.com.br",
                "@@@@",
                "....@...",
                "marco",
                "m.m",
                "marco.pdsv@b",
                "marco.pdsv@b asd sd",
                "a@bbb"
            ]

            def assert_valid_email(valid_email):
                c.post("/", data=dict(
                    email=valid_email
                ))
                form = self.EmailMockForm()
                self.assertTrue(form.validate_on_submit())

            def assert_invalid_email(invalid_email):
                c.post("/", data=dict(
                    email=invalid_email
                ))
                form = self.EmailMockForm()
                self.assertFalse(form.validate_on_submit())
                self.assertEqual(len(form.email.errors), 1)
                self.assertEqual(form.email.errors[0], R.string.validators.invalid_email_format)

            for email in valid_emails:
                assert_valid_email(email)

            for email in invalid_emails:
                assert_invalid_email(email)

            # Testing validator stop
            assert len(invalid_emails) > 1
            # stop=True
            c.post("/", data=dict(
                email=invalid_emails[0]
            ))
            email_mock_form = self.EmailMockFormStopTrueWithAlwaysError()
            self.assertFalse(email_mock_form.validate_on_submit())
            self.assertEqual(len(email_mock_form.email.errors), 1)
            # stop=False
            c.post("/", data=dict(
                email=invalid_emails[0]
            ))
            email_mock_form = self.EmailMockFormStopFalseWithAlwaysError()
            self.assertFalse(email_mock_form.validate_on_submit())
            self.assertEqual(len(email_mock_form.email.errors), 2)

    # ==================================================================================================================
    #
    #
    #
    #
    # Unique Validator
    # ==================================================================================================================
    class UniqueMockForm(FlaskForm):
        email = StringField(validators=[
            Unique(
                model=User,
                field=User.email
            )
        ])

    class UniqueMockFormCustomMessage(FlaskForm):
        email = StringField(validators=[
            Unique(
                model=User,
                field=User.email,
                message=R.string.validators.email_already_registered
            )
        ])

    class UniqueMockFormCustomCallableMessage(FlaskForm):
        email = StringField(validators=[
            Unique(
                model=User,
                field=User.email,
                message=lambda: R.string.validators.email_already_registered
            )
        ])

    class UniqueMockFormStopTrue(FlaskForm):
        email = StringField(validators=[
            Unique(
                model=User,
                field=User.email,
                stop=True
            ),
            AlwaysError()
        ])

    class UniqueMockFormStopFalse(FlaskForm):
        email = StringField(validators=[
            Unique(
                model=User,
                field=User.email,
                stop=False
            ),
            AlwaysError()
        ])

    def test_unique(self):
        with app.app_context():
            db.drop_all()
            db.create_all()
            with app.test_client() as c:
                # Testing validator call
                email = "marco.pdsv@gmail.com"

                c.post("/", data=dict(
                    email=email
                ))
                form = self.UniqueMockForm()
                self.assertTrue(form.validate_on_submit())

                db.session.add(User(email=email))
                db.session.commit()

                c.post("/", data=dict(
                    email=email
                ))
                form = self.UniqueMockForm()
                self.assertFalse(form.validate_on_submit())
                self.assertEqual(len(form.email.errors), 1)
                self.assertEqual(form.email.errors[0], R.string.validators.unique_field)

                c.post("/", data=dict(
                    email=email
                ))
                form = self.UniqueMockFormCustomMessage()
                self.assertFalse(form.validate_on_submit())
                self.assertEqual(len(form.email.errors), 1)
                self.assertEqual(form.email.errors[0], R.string.validators.email_already_registered)

                c.post("/", data=dict(
                    email=email
                ))
                form = self.UniqueMockFormCustomCallableMessage()
                self.assertFalse(form.validate_on_submit())
                self.assertEqual(len(form.email.errors), 1)
                self.assertEqual(form.email.errors[0], R.string.validators.email_already_registered)

                # Testing validator stop
                # stop=True
                c.post("/", data=dict(
                    email=email
                ))
                form = self.UniqueMockFormStopTrue()
                self.assertFalse(form.validate_on_submit())
                self.assertEqual(len(form.email.errors), 1)
                # stop=False
                c.post("/", data=dict(
                    email=email
                ))
                form = self.UniqueMockFormStopFalse()
                self.assertFalse(form.validate_on_submit())
                self.assertEqual(len(form.email.errors), 2)

    # ==================================================================================================================
    #
    #
    #
    #
    # Length Validator
    # ==================================================================================================================
    class LengthMockFormMin1MaxNone(FlaskForm):
        field = Field(validators=[Length(min_length=1)])

    class LengthMockFormMin3MaxNone(FlaskForm):
        field = Field(validators=[Length(min_length=3)])

    class LengthMockFormMinNoneMax1(FlaskForm):
        field = Field(validators=[Length(max_length=1)])

    class LengthMockFormMinNoneMax6(FlaskForm):
        field = Field(validators=[Length(max_length=6)])

    class LengthMockFormMin3Max6(FlaskForm):
        field = Field(validators=[Length(min_length=3, max_length=6)])

    class LengthMockFormMin3Max6CustomMessage(FlaskForm):
        field = Field(validators=[Length(min_length=3, max_length=6, message=R.string.validators.test_message)])

    class LengthMockFormMin3Max6CustomCallableMessage(FlaskForm):
        field = Field(validators=[Length(min_length=3, max_length=6, message=lambda:R.string.validators.test_message)])

    class LengthMockFormMin3Max6StopTrue(FlaskForm):
        field = Field(validators=[Length(min_length=3, max_length=6, stop=True), AlwaysError()])

    class LengthMockFormMin3Max6StopFalse(FlaskForm):
        field = Field(validators=[Length(min_length=3, max_length=6, stop=False), AlwaysError()])

    def test_length(self):
        # Testing Length creation
        with self.assertRaises(AssertionError):
            Length()
        with self.assertRaises(AssertionError):
            Length(min_length=-2)
        with self.assertRaises(AssertionError):
            Length(max_length=-2)
        with self.assertRaises(AssertionError):
            Length(min_length=-2, max_length=-2)
        with self.assertRaises(AssertionError):
            Length(min_length=6, max_length=3)

        with app.test_client() as c:
            # Testing validator call
            c.post("/", data=dict(
                field="aaa"
            ))
            form = self.LengthMockFormMin3MaxNone()
            self.assertTrue(form.validate_on_submit())

            c.post("/", data=dict(
                field="aaaa"
            ))
            form = self.LengthMockFormMin3MaxNone()
            self.assertTrue(form.validate_on_submit())

            c.post("/", data=dict(
            ))
            form = self.LengthMockFormMin1MaxNone()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)
            self.assertEqual(form.field.errors[0], R.string.validators.field_min_length_singular % dict(min_length=1))

            c.post("/", data=dict(
                field=""
            ))
            form = self.LengthMockFormMin1MaxNone()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)
            self.assertEqual(form.field.errors[0], R.string.validators.field_min_length_singular % dict(min_length=1))

            c.post("/", data=dict(
                field="aa"
            ))
            form = self.LengthMockFormMin3MaxNone()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)
            self.assertEqual(form.field.errors[0], R.string.validators.field_min_length_plural % dict(min_length=3))

            c.post("/", data=dict(
                field="aaa"
            ))
            form = self.LengthMockFormMinNoneMax6()
            self.assertTrue(form.validate_on_submit())

            c.post("/", data=dict(
                field="aaaaaa"
            ))
            form = self.LengthMockFormMinNoneMax6()
            self.assertTrue(form.validate_on_submit())

            c.post("/", data=dict(
                field="aa"
            ))
            form = self.LengthMockFormMinNoneMax1()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)
            self.assertEqual(form.field.errors[0], R.string.validators.field_max_length_singular % dict(max_length=1))

            c.post("/", data=dict(
                field="aaaaaaa"
            ))
            form = self.LengthMockFormMinNoneMax6()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)
            self.assertEqual(form.field.errors[0], R.string.validators.field_max_length_plural % dict(max_length=6))

            c.post("/", data=dict(
                field="aa"
            ))
            form = self.LengthMockFormMin3Max6()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)
            self.assertEqual(form.field.errors[0], R.string.validators.field_length_range %
                             dict(min_length=3, max_length=6))

            c.post("/", data=dict(
                field="aaa"
            ))
            form = self.LengthMockFormMin3Max6()
            self.assertTrue(form.validate_on_submit())

            c.post("/", data=dict(
                field="aaaaa"
            ))
            form = self.LengthMockFormMin3Max6()
            self.assertTrue(form.validate_on_submit())

            c.post("/", data=dict(
                field="aaaaaaa"
            ))
            form = self.LengthMockFormMin3Max6()
            self.assertFalse(form.validate_on_submit())

            c.post("/", data=dict(
                field="aaaaaaa"
            ))
            form = self.LengthMockFormMin3Max6CustomMessage()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)
            self.assertEqual(form.field.errors[0], R.string.validators.test_message)

            c.post("/", data=dict(
                field="aaaaaaa"
            ))
            form = self.LengthMockFormMin3Max6CustomCallableMessage()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)
            self.assertEqual(form.field.errors[0], R.string.validators.test_message)

            c.post("/", data=dict(
                field="aaaaaaa"
            ))
            form = self.LengthMockFormMin3Max6StopTrue()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)

            c.post("/", data=dict(
                field="aaaaaaa"
            ))
            form = self.LengthMockFormMin3Max6StopFalse()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 2)
