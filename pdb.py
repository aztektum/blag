from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
        <img src='http://www.gifbin.com/bin/062010/poster-1276852649_chilling-sloth.gif'>
    </html>
    ''' 

if __name__ == '__main__':
    app.run()
