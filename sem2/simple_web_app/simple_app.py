import flask
import tf
from flask import Flask, request

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")
@app.route('/')


def root():
    return flask.render_template('index.html')


@app.route('/test')
def wilson_test():
    if request.method == 'GET':
        n=request.args.get('name')
    if n != None:
        n = int(n)
        n = tf.test(n)
        if n == False:
            n = 'Число не является простым'
        else:
            n = 'Число простое'
    return flask.render_template('test.html', name = n)

if __name__ == '__main__':
   app.run(debug = False)
#Моего кода здесь очень мало. Почти все взято с сайта.
