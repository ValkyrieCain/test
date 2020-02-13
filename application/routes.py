from flask import render_template, redirect, url_for
from application import app, db
from application.models import Movies
from application.forms import PostRating

@app.route('/')
@app.route('/home')
def home():
	postData= Movies.query.all()
	return render_template('home.html', title='Home',posts=postData)
@app.route('/register')
def register():
	return render_template('register.html', title='Register')
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
