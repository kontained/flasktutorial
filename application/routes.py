from flask import render_template, url_for, flash, redirect, request
from application import application, db, bcrypt
from application.forms import RegistrationForm, LoginForm
from application.models import User, Post
from flask_login import login_user, logout_user, login_required, current_user


posts = [
    {
        'author': 'Author 1',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '2019-01-26',
    },
    {
        'author': 'Author 2',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '2019-01-27',
    }
]


@application.route('/')
@application.route('/home')
def home():
    return render_template('home.html', posts=posts)


@application.route('/about')
def about():
    return render_template('about.html', title='About')


@application.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(
            f'Account created for {form.username.data}! You can now login.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


@application.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password.', 'danger')

    return render_template('login.html', title='Login', form=form)


@application.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@application.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')