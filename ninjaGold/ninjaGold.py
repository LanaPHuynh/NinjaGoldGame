from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "my secret key"
app.yourGold = int(0)
import random

@app.route("/")
def game():
    session['yourGold'] = app.yourGold
    return render_template("index.html")


@app.route("/process_money", methods=['POST'])
def process_money():
    print(request.form)
    print(request.form['building'])
    if request.form['building'] == 'farm':
        random_number = random.randint(10,20)
        app.yourGold += int(random_number)
    if request.form['building'] == 'cave':
        random_number = random.randint(5,10)
        app.yourGold += int(random_number)
    if request.form['building'] == 'house':
        random_number = random.randint(2,5)
        app.yourGold += int(random_number)
    if request.form['building'] == 'casino':
        items = [-50, 50]
        random.choice(items)
        app.yourGold += int(random.choice(items))
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)