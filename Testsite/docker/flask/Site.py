'''This is my Flask Blog Website!'''
from flask import Flask, render_template
APP = Flask(__name__)

@APP.route('/guild')
def guild():
    '''Returns the guild template'''
    return render_template('guild.html')

@APP.route('/guild/info')
def info():
    '''Returns the info template'''
    return render_template('info.html')

@APP.route('/guild/test')
def test():
    '''Returns the info template'''
    return render_template('index.html')

@APP.route('/guild/apply')
def apply():
    '''Returns the info template'''
    return render_template('apply.html')

if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0', port=80)
