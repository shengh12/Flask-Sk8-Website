from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ea109067810c1cb3a44106ece4e0d0b4'

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
    return render_template('SK8News.html', posts=skate_news_data, title="Sk8 News")


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
  
