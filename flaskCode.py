from flask import Flask, render_template, url_for
app = Flask(__name__)

skate_news_data = [
    {
        'title':'Skateboarding is Cool',
        'author': 'Sheng Huang',
        'date_posted': 'April 20, 2021',
        'content':'First Post Yay!!!'
    },
    {
        'title':'Skateboarding is not Cool',
        'author': 'Sheng Huang',
        'date_posted': 'May 20, 2021',
        'content':'2nd Post Yay!!!'
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

if __name__ == '__main__':
  app.run(debug=True)
  
