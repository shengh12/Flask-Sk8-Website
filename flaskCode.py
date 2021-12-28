from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ea109067810c1cb3a44106ece4e0d0b4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    
    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"
    
    
skate_news_data = [
    {
        'title':'Skateboarding is Cool',
        'author': 'Sheng Huang',
        'date_posted': 'April 21, 2021',
        'content':'2nd Post Yay!!!'
    },
    {
        'title':'Skateboarding is not Cool',
        'author': 'Sheng Huang',
        'date_posted': 'April 20, 2021',
        'content':'First Post Yay!!!'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('homePage.html', title="Home")

@app.route("/news")
def news():
    return render_template('SK8News.html', posts=skate_news_data, title="Sk8 Posts")


@app.route("/tricks")
def tricks():
    return render_template('tricks.html', title="Sk8 Tricks")

@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
                           
if __name__ == '__main__':
  app.run(debug=True)
  
