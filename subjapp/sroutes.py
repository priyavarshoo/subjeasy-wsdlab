# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for
from subjapp import app, db, bcrypt
from subjapp.sforms import RegForm, LoginForm
from subjapp.smodels import User, Post

db.create_all()

posts = [
    {
        'author': 'Abc',
        'title': 'Smart Writing',
        'content': 'Smart pen can be provided to students to take notes and write answers in exams directly as if writing on paper',
        'date_posted': 'January 29, 2021'
    },
    {
        'author': 'Pqr',
        'title': 'Prevent malpractices',
        'content': 'Keep a live count down timer so that it pressurizes students causing them to study for subsequent exams and avoid malpractices',
        'date_posted': 'January 16, 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/register', methods=['GET', 'POST'])
def register():
    db.create_all()
    form = RegForm()
    if form.validate_on_submit():
        form.validate_username(form.username.data)
        form.validate_email(form.email.data)
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can log in now', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
            
    return render_template('login.html', title="Register", form=form)

