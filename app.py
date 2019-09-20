from flask import Flask, render_template
import pyautogui

app = Flask(__name__)

# DEFAULTS
curOp = 'None'

@app.route('/')
def index():
    return render_template('index.html', op = curOp)

@app.route('/run', methods=['GET', 'POST'])
def run():
    #Enter automation code here
    curOp = 'Running...'
    return render_template('index.html', op = curOp)

if __name__ == '__main__':
    app.config['DEBUG'] = True

    app.run()
