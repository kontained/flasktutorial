from flask import render_template, url_for, flash, redirect
from application import application
from application.forms import RegistrationForm, LoginForm


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
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)


@application.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please try again.', 'danger')

    return render_template('login.html', title='Login', form=form)
