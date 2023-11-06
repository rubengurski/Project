from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)

Overview=[]
TotalPrice=float(0)
scroll=''

@app.route('/', methods=['POST', 'GET'])
def init():
    return render_template('Home.html', Overview=Overview, Margherita='Margherita', Pepperoni='Pepperoni', Tuna='Tuna', TotalPrice=TotalPrice, scroll=scroll)

@app.route('/addpizza', methods = ['POST'])
def add_pizza():
    global TotalPrice, scroll
    addpizza = str(request.form['addpizza'])
    if addpizza not in Overview:
        if addpizza=='Margherita':
            TotalPrice+=5.99
            Overview.append(addpizza)
        if addpizza=='Pepperoni':
            TotalPrice+=6.99
            Overview.append(addpizza)
        if addpizza=='Tuna':
            TotalPrice+=7.99
            Overview.append(addpizza)
    scroll='home'

    print('Data received:', addpizza, '\n current overview:', Overview)  # See console...
    return redirect('/')

@app.route('/pay', methods=['POST', 'GET'])
def overview_pay():
    global TotalPrice, scroll
    scroll='home'
    submit=str(request.form['submit'])
    if submit=='Pay & Proceed':
        return redirect('/confirmed')

@app.route('/removepizza', methods=['POST', 'GET'])
def overview_remove():
    global TotalPrice, scroll
    scroll='home'
    removePizza=str(request.form['removePizza'])
    if removePizza=='removeMargherita':
        Overview.remove('Margherita')
        TotalPrice-=5.99
        return redirect('/')
    elif removePizza=='removePepperoni':
        Overview.remove('Pepperoni')
        TotalPrice-=6.99
        return redirect('/')
    elif removePizza=='removeTuna':
        Overview.remove('Tuna')
        TotalPrice-=7.99
        return redirect('/')

@app.route('/confirmed', methods=['GET', 'POST'])
def payment_confirmed():
    if 'Margherita' in Overview:
        pizzaName1='Margherita'
        
    return render_template('Confirmed.html')