'''This is my Flask Blog Website!'''
from flask import Flask, render_template
APP = Flask(__name__)

@APP.route('/guild')
def guild():
    '''Returns the index template'''
    return render_template('guild.html')

if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0', port=80)
