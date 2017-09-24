# Eugene Thomas
# SoftDev Pd. 7
# HW4 -- Fill Up Yer Flask
# 2017-09-24

from flask import Flask
app = Flask(__name__)

@app.route('/') 
def hello():
    html = "<html><head>Eugene Thomas<br>"
    html += "SoftDev Pd. 7<br>"
    html += "HW4 -- <i>Fill Up Yer Flask</i><br>"
    html += "2017-09-24<br><br></head>"
    html += "<h1>WELCOME TO THE DOOR SELECTOR</h1><br>"
    html += "<b>Choose one of the following...</b><br><br>"
    html += "<a href='/door1'>Door 1</a><br>"
    html += "<a href='/door2'>Door 2</a><br>"
    html += "<a href='/door3'>Door 3</a></html>"
    return html

@app.route('/door1') 
def door1():
    return "DOOR 1" 


@app.route('/door2') 
def door2():
    return "DOOR 2"

@app.route('/door3') 
def door3():
    return "DOOR 3"

if __name__ == "__main__":
    app.debug = True
    app.run()
