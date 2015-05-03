from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Michael'} # this luser is so fake
    return render_template('index.html',
                            title='Home',
                            user=user)
