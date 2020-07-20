from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, \
    TextAreaField, SelectField, IntegerField, DateField, HiddenField
from wtforms.validators import DataRequired


class SignIn(FlaskForm):
    userName = StringField('', validators=[DataRequired()], id='user_name',
                           render_kw={
                               "placeholder": "user name",
                               "class": 'form-control'})
    password = PasswordField('', validators=[DataRequired()], id='password',
                             render_kw={
                                 "placeholder": "password",
                                 "class": 'form-control'})
    rememberMe = BooleanField('Remember me', render_kw={'value': "remember-me"})
    submit = SubmitField('Sign In')


class ApplyLeave(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], id='user_name',
                       render_kw={
                           "placeholder": "Name",
                           "class": 'form-control'})
    reason = TextAreaField('Reason For Leave', validators=[DataRequired()],
                           id='reason',
                           render_kw={
                               "placeholder": "Reason for leave",
                               "class": 'form-control'})
    leave_type = SelectField('Leave Type', choices=[('paid', 'paid'), ('sick',
                                                                     'sick')],
                             id='leave type',
                             render_kw={"class": 'form-control'})
    leave_from = DateField('Leave from', id='leave_form',
                           render_kw={"class": 'form-control'})
    leave_duration = IntegerField('Leave duration', id='leave_duration',
                                  render_kw={"class": 'form-control'})
    # image = FileField('Image File', validators=[regexp('^[^/\\]\.jpg$')])
    description = TextAreaField('Image Description')

    submit = SubmitField('Sign In')


class LeaveDecision(FlaskForm):

    accept = SubmitField('accept', render_kw={"class": "btn btn-default",
                                              "value": "accept"})
    reject = SubmitField('reject', render_kw={"class": "btn btn-default",
                                              "value": "reject"})
    meet = SubmitField('meet', render_kw={"class": "btn btn-default",
                                          "value": "meet"})
    id = HiddenField('')
    confirm = BooleanField('confirm', render_kw={"class": 'form-control'})
