from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from application import app, db, bcrypt
from application.models import Movies, Users
from application.forms import PostRating, RegistrationForm, LoginForm

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(email=form.email.data, password=hash_pw)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

@app.route('/')
@app.route('/home')
def home():
	postData= Movies.query.all()
	return render_template('home.html', title='Home',posts=postData)

@login_required
@app.route('/movies', methods=['GET', 'POST'])
def movies():
    form = PostRating()
    if form.validate_on_submit():
        postRating = Movies(
            title = form.title.data,
            genre = form.genre.data,
            director = form.director.data,
            rating = form.rating.data
        )

        db.session.add(postRating)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('movies.html', title='Movies', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))
