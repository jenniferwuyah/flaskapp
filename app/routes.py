from flask import Flask, render_template, request, flash, redirect, url_for
from forms import ContactForm, LoginForm
from flask.ext.mail import Message, Mail

mail = Mail()

app = Flask(__name__)

app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'jennwuyn@gmail.com'
app.config["MAIL_PASSWORD"] = 'Ephesians4:29'
 
mail.init_app(app)


@app.route('/')
def home():
  return render_template('index.html')
 
@app.route("/about")
def about():
	return render_template('about.html')


#################
# Admin Console #
#################
@app.route('/admin')
def admin():

	return render_template('admin.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()

  # if 'email' in session:
  #   return redirect(url_for('profile')) 
      
  # if request.method == 'POST':
  #   if form.validate() == False:
  #     return render_template('login.html', form=form)
  #   else:
  #     session['email'] = form.email.data
  #     return redirect(url_for('profile'))
                
  # elif request.method == 'GET':
	return render_template('login.html', form=form)

@app.route('/logout')
def logout():

  # if 'email' not in session:
  #   return redirect(url_for('login'))
    
  # session.pop('email', None)
  return redirect(url_for('home'))
 
if __name__ == '__main__':
  app.run(debug=True)
