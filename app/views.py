# coding=utf-8
# Представления — это обработчики, которые отвечают на запросы веб-браузера.
# Представления в Flask пишутся как Python функции.
# Каждая функция представления сопоставляется с одним или несколькими запросами URL.
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db
from forms import LoginForm
from models import User, ROLE_USER, ROLE_ADMIN, Team

@app.route('/')
@app.route('/index')
# эту страницу увидят только зарегистрированные пользователи
#@login_required
def index():
    if 'nickname' in session:
        return render_template("main_page.html")
    return render_template("login.html")

@app.route('/login', methods = ['POST'])
def login():
    error = None
    users = User.query.all()
    login_user = None
    # request.form['nickname'] in users['nickname']
    for user in users:
        if request.form['nickname'] == user.nickname:
            login_user = user

    if login_user is not None:
        if request.form['password'] == login_user['password']:
            session['nickname'] = request.form['nickname']
            return redirect(url_for('main_page'))
        else:
            error = 'Invalid password combination'
            return render_template("login.html", error=error)
    else:
        error = 'Invalid login combination'
        return render_template("login.html", error=error)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        users = User.query.all()
        existing_user = False
        for user in users:
            if request.form['nickname'] == user.nickname:
                existing_user = True

        if existing_user == False:
            nickname = request.form['nickname']
            u = User(nickname=request.form['nickname'], email=request.form['email'], password = request.form['password'])
            db.session.add(u)
            db.session.commit()
            return redirect(url_for('index'))
        error = "That username already exists!"
        return render_template('register.html',
                               error = error)

    return render_template('register.html', error = error)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/main_page')
def main_page():
    return render_template('main_page.html')

@app.route('/create_team', methods = ['GET', 'POST'])
def create_team():
    error = None
    users = User.query.all()
    us = []
    for user in users:
        if user.team_id is None or  user.team_id == 0:
            us.append(user)

    return render_template('create_team.html',
                           users = us,
                           error = error)

@app.route('/diagnose_team')
def diagnose_team():
    users = User.query.all()
    for user in users:
        user.team_id = 0
        db.session.commit()
    return render_template('main_page.html')

@app.route('/pass_test')
def pass_test():
    return render_template('pass_test.html')

@app.route('/check_team',  methods = ['GET', 'POST'])
def check_team():
    if request.method == 'POST':
        teamNumber =[]
        toTeam = []
        for i in range(0, 9):
            teamNumber.append(int(request.form['memberId' + str(i)]))

        user = User.query.filter_by(id = teamNumber[1]).first()
        if any(teamNumber.count(tn) > 1 for tn in teamNumber) == False:
           team = Team(members = len(teamNumber))
           db.session.add(team)
           db.session.commit()
           for i in range(0,9):
                user = User.query.filter_by(id=teamNumber[i]).first()
                user.team_id = team.__getitem__(id)
                db.session.add(user)
                db.session.commit()
           return str(Team.query.all())

        else:
            error = "Dublicates"
            users = User.query.all()
            us = []
            for user in users:
                if user.team_id is None or user.team_id == 0:
                    us.append(user)
            return render_template('create_team.html',
                           users = us,
                           error = error)

    #return render_template('main_page.html')
































