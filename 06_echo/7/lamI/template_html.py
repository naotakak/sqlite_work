'''
Irene Lam
SoftDev pd7
K#06: Echo Echo Echo
2017-10-02
'''

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello_world():
    print("\n=============headers=============")
    print(request.headers)
    print("\n=============args=============")
    print(request.args)
    print("\n=============form=============")
    print(request.form)

    return render_template("Forms.html")

@app.route("/reply")
def reply():
    '''
    Passes the name input and the request method used
    '''
    return render_template("Reply.html", name = request.args["firstname"], method = request.method)

if __name__ == "__main__":
    app.debug = True
    app.run()


