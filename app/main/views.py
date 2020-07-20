from random import random

from flask import render_template, redirect, url_for, session

from . import main
from .forms import SignIn, ApplyLeave, LeaveDecision


class leave:
    def __init__(self, name, reason, type, date, duration, description):
        self.id = str(random() * 10000 // 1)
        self.name = name
        self.reason = reason
        self.type = type
        self.date = date
        self.duration = duration
        self.description = description


class user:
    def __init__(self, name, password, isAdmin=False):
        self.name = name
        self.password = password
        self.leave = []
        self.isAdmin = isAdmin

    def add_leave(self, id):
        self.leave.append(id)


data = {}
status = {}
users = {'student': user('student', 'student'),
         'prof': user('prof', 'prof', True)}


@main.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = SignIn()
    if form.validate_on_submit():
        name = form.userName.data
        password = form.password.data
        for x in users:
            if x == name and users[x].password == password:
                session['name'] = form.userName.data
                return redirect(url_for('.apply_leave'))
        return redirect(url_for('.index'))
    return render_template('sign_in.html', form=form)


@main.route('/applyLeave', methods=['GET', 'POST'])
def apply_leave():
    try:
        if session['name'] in users:
            form = ApplyLeave()
            if form.validate_on_submit():
                name = form.name.data
                reason = form.reason.data
                type = form.leave_type.data
                date = form.leave_from.data
                duration = form.leave_duration.data
                # image = FileField('Image File', validators=[regexp('^[^/\\]\.jpg$')])
                description = form.description.data
                _ = leave(name, reason, type, date, duration,
                          description)
                data[_.id] = _
                users[session['name']].add_leave(_.id)
                status[_.id] = 0
                return redirect(url_for('.logs'))
            return render_template('apply_leave.html', form=form)
    except KeyError:
        pass
    return redirect(url_for('.index'))


@main.route('/logs', methods=['GET', 'POST'])
def logs():
    try:
        if session['name'] in users:
            form = LeaveDecision()
            _ = {}
            if users[session['name']].isAdmin:
                _ = data
            else:
                for x in data:
                    if x in users[session['name']].leave:
                        _[x] = data[x]
            if form.accept.data or form.reject.data or form.meet.data:
                if form.accept.data:
                    status[form.id.data] = 1
                elif form.reject.data:
                    status[form.id.data] = -1
                elif form.meet.data:
                    status[form.id.data] = 0
                return f'{form.id.data} {status[form.id.data]}'
                return redirect(url_for('.logs'))
            return render_template('log.html', log=_, form=form,
                                   isProf=users[session['name']].isAdmin,
                                   status=status)
    except KeyError:
        return redirect(url_for('.index'))
