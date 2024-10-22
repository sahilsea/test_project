from flask import Flask , render_template , send_from_directory
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '6ec924337ec3665a51edafeba6ef5bfb'

posts = [

    {
        'country': 'Santorini Greece',
        'image': 'country-1.jpg',
    },
    {
        'country': 'Vernazza, Italy',
        'image': 'country-2.jpg',
    },
    {
        'country': 'San Francisco',
        'image': 'country-3.jpg',
    },
    {
        'country': 'Navagio, Greece',
        'image': 'country-4.jpg',
    },
    {
        'country': 'Ao Nang, Thailand',
        'image': 'country-5.jpg',
    },
    {
        'country': 'Phi Phi Island, Thailand',
        'image': 'country-6.jpg',
    }
    
]


@app.route("/home")
@app.route("/")
def hello():
    return render_template ('index.html', posts = posts)


@app.route("/about")
def about():
    return "About Page"

# @app.route("/login")
# def login():
#     return render_template ('login.html', title = 'Login')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login2.html', title='Login', form = form)

if __name__ == '__main__':
    app.run(debug=True)
