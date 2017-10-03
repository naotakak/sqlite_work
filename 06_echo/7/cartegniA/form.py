from flask import Flask, render_template, request
app = Flask(__name__) #create instance of class

#assign following fxn to run when root route requested
@app.route("/")
def form1():
        #print app
        #print request.headers
        print request.method
        #print request.args
        print request.form
        return render_template("form.html")

@app.route("/auth")
def auth():
    print "\n\n\n\n\n"
    print "*** DIAG: THIS FLASK OBJ ***"
    print app
    print "*** DIAG request.args ***"
    print request.args
    return "Right. Off you go."

if __name__ == "__main__":
    app.debug = True
    app.run()
