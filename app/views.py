from flask import Flask, request, render_template, flash, redirect, url_for
from flask.ext.login import login_user, login_required, current_user, logout_user
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from app import app
from app import lm
from app import db

@lm.user_loader
def load_user(userid):
	return User.objects.get(id=userid)

class User(db.Document):
	# id = db.IntField()
	username = db.StringField(required=True)
	first_name = db.StringField(max_length=25)
	last_name = db.StringField(max_length=25)
	email = db.EmailField(max_length=35)
	password = db.StringField(max_length=35)

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)

	def __unicode__(self):
		return self.id

	def __repr__(self):
		return '<User %r>' % (self.username)

class SignUpForm(Form):
	username = TextField("Username", [
		validators.Length(min=4, max=25),
		validators.Required()
	])
	first_name = TextField("First Name", [validators.Length(min=4, max=25)])
	last_name = TextField("Last Name", [validators.Length(min=4, max=25)])
	email = TextField("Email", [
		validators.Length(min=6, max=35),
		validators.Email(message="This is not a valid email, dude.")
	])
	password = PasswordField("Password", [
		validators.Required(),
		validators.EqualTo('confirm', message="Passwords must match")
	])
	confirm = PasswordField("Confirm Password")

class LoginForm(Form):
	username = TextField("Username", [
		validators.Length(min=4, max=25),
		validators.Required()
	])
	password = PasswordField("Password", [validators.Required()])


@app.route("/", methods=["GET", "POST"])
def index():
	if current_user.is_authenticated() == True and current_user.is_anonymous() == False:
		return render_template("index.html", user=current_user)
	return render_template("index.html", user=None)

@app.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm(request.form)
	if request.method == "POST" and form.validate():
		user = User.objects(username=form.username.data).first()
		if user == None:
			return redirect( url_for("signup") )
		else:
			if user.username == form.username.data and user.password == form.password.data:
				login_user(user=user, remember=True)
				return redirect( url_for("index"))
	return render_template("login.html", form=form)

@app.route("/signup", methods=["GET", "POST"])
def signup():
	form = SignUpForm(request.form)
	if request.method == "POST" and form.validate():
		user = user = User.objects(username=form.username.data).first()
		if user == None:
			user = User(
				username=form.username.data,
				first_name=form.first_name.data,
				last_name=form.last_name.data,
				email=form.email.data,
				password=form.password.data
			)
			user.save()
			return redirect( url_for("login") )
	return render_template("signup.html", form=form)

@app.route("/logout", methods=["GET"])
@login_required
def logout():
	logout_user()
	return redirect( url_for("index") )