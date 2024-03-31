import flask
from flask import Flask, render_template, request, redirect, make_response

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def loginHtml():
    return flask.render_template('loging.html')

@app.route('/Home/', methods=['GET', 'POST'])
def Home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        resp = make_response(render_template('Home.html', name=name))
        resp.set_cookie('username', name)
        return resp
    else:

        return (Flask.redirect('/'))
@app.route('/logout')
def logout():
    # Удаление cookie с данными пользователя
    resp = make_response(redirect('/'))
    resp.delete_cookie('username')
    return resp
if __name__=="__main__":
    app.run(debug=True)