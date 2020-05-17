from flask import Flask, render_template, request,url_fpr
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('home.html')

@app.route('/about')
def student():
   return render_template('about.html')

@app.route('/signup',methods = ['POST', 'GET'])
def details():
   if request.method == 'POST':
      data=request.form
      return render_template("signup.html",data = result)

@app.route('/status')
def status():
    return render_template('status.html')


def student():
   return render_template('about.html')


if __name__ == '__main__':
   app.run(debug = True)