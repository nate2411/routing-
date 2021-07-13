from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/user/<name>')
def user(name):
    if name == "JAYDEN":
        return redirect(url_for('adminpage', name=name))
    else:
        return redirect(url_for('guest', name=name))


@app.route('/guest/<name>')
def guest(name):
    return "I am a guess. My name is %s" % name

@app.route('/')
def user_page(name):
    return "The admin is %s" % name


@app.route('/payment/<int:sal>')
def payment_page(sal):
    if sal > 5000:
        return redirect("https://www.sahomeloans.com/")
    else:
        return redirect("http://www.fnb.co.za")


@app.route('/admin/<name>')
def adminpage(name):
    return "The admin is %s" % name

if __name__ == "__main__":
    app.debug = True
    app.run()
