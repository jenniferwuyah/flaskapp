from flask_wtf import Form 
from wtforms import TextField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Email
 
class ContactForm(Form):
	name = TextField("Name",  [InputRequired("Please enter your name.")])
	email = TextField("Email",  [InputRequired("Please enter your email address."), Email("This field requires a valid email address")])
	subject = TextField("Subject",  [InputRequired("Please enter a subject.")])
	message = TextAreaField("Message",  [InputRequired("Please enter a message.")])
	submit = SubmitField("Send")

class LoginForm(Form):
	email = TextField("Email",  [InputRequired("Please enter your email address."), Email("Please enter your email address.")])
	password = PasswordField('Password', [InputRequired("Please enter a password.")])
	submit = SubmitField("Sign In")

	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

	def validate(self):
		if not Form.validate(self):
			return False

		user = User.query.filter_by(email = self.email.data).first()
		if user and user.check_password(self.password.data):
			return True
		else:
			self.email.errors.append("Invalid e-mail or password")
			return False