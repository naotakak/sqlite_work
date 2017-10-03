#!usr/bin/python
'''
Brian Leung
PD 7 Brown SoftDev
10/3/2017
'''
#Imports
from flask import Flask, render_template, request
app = Flask(__name__)

#Just the landing page
@app.route("/")
def landing():
	#print(request.args)
	#All our input things go in the landing page.
	return render_template("landing.html")

#Here is the echo page.
@app.route("/echoecho")
def echo():
	return render_template("echo.html",name = request.args['user'], method = request.method)

#Run the Flask
if __name__ == "__main__":
	app.debug = True
	app.run()