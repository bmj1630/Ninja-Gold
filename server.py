from flask import Flask, redirect, render_template, redirect, session, request
import random
app = Flask(__name__)
app.secret_key = "keep it secret keep it safe"

activity = []

@app.route('/')
def index():
    if "gold" not in session:
        session['gold'] = 0
    return render_template("index.html", activity = activity)

@app.route('/process_money', methods = ["Post"])
def process():
    # print(request.form)
    if (request.form['get_money'] == 'farm'):
        amount = random.randint(10,20)
        session['gold'] += amount
        activity.append("The farm grants you " + str(amount) + " gold.")

    if (request.form['get_money'] == 'cave'):
        amount = random.randint(5,10)
        session['gold'] += amount
        activity.append("The cave grants you " + str(amount) + " gold.")

    if (request.form['get_money'] == 'house'):
        amount = random.randint(2,5)
        session['gold'] += amount
        activity.append("The house grants you " + str(amount) + " gold.")
    
    if(request.form['get_money'] == 'casino'):
        amount = random.randint(-50,50)
        session['gold'] += amount
        if (amount < 0):
            activity.append("The casino punishes you " + str(amount) + "gold.")
        elif(amount == 0):
            activity.append("The casino gives you nothing")
        else:
            activity.append("The casino grants you " + str(amount) + "gold.")

    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)