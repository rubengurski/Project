from flask import Flask
from flask import render_template
from flask import request, redirect
import csv
from datetime import datetime

app = Flask(__name__)

Overview=[]
OverviewMario=[]
Orders=[]
TotalPrice=0
TotalPriceMario=0
scroll=''
uniqueID=''
totalOrder = []
allOrders = []

@app.route('/', methods=['POST', 'GET'])
def home():
    global Overview
    
    return render_template('Home.html', Overview=Overview, Margherita='Margherita', Pepperoni='Pepperoni', Tuna='Tuna', TotalPrice=TotalPrice, scroll=scroll)

@app.route('/mario', methods=['POST', 'GET'])
def mario():
    return render_template('Mario.html', OverviewMario=OverviewMario, Margherita='Margherita', Pepperoni='Pepperoni', Tuna='Tuna', TotalPriceMario=TotalPriceMario)

@app.route('/luigi', methods=['POST', 'GET'])
def luigi():
    global uniqueID
    global totalOrder
    global allOrders
    print(totalOrder)
    n = 0
    return render_template('Luigi.html', Overview=Overview, uniqueID=uniqueID, totalOrder = totalOrder, allOrders = allOrders, n=n)

@app.route('/screen', methods=['POST', 'GET'])
def screen_customers():
    return render_template('Screen.html')

@app.route('/status', methods = ['POST'])
def sstatus():
    data = request.get_json()
    status = data['status']
    print(status)
    return '200', 200

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

@app.route('/addpizzamario', methods = ['POST'])
def add_pizza_mario():
    global TotalPriceMario
    addpizzamario = str(request.form['addpizzamario'])
    if addpizzamario not in OverviewMario:
        if addpizzamario=='Margherita':
            TotalPriceMario+=5.99
            OverviewMario.append(addpizzamario)
        if addpizzamario=='Pepperoni':
            TotalPriceMario+=6.99
            OverviewMario.append(addpizzamario)
        if addpizzamario=='Tuna':
            TotalPriceMario+=7.99
            OverviewMario.append(addpizzamario)
    scroll='home'

    print('Data received:', addpizzamario, '\n current overview Mario:', OverviewMario)  # See console...
    return redirect('/mario')

@app.route('/removepizzamario', methods=['POST', 'GET'])
def overview_remove_mario():
    global TotalPriceMario
    scroll='home'
    removepizzamario=str(request.form['removepizzamario'])
    if removepizzamario=='removeMargherita':
        OverviewMario.remove('Margherita')
        TotalPriceMario-=5.99
        return redirect('/mario')
    elif removepizzamario=='removePepperoni':
        OverviewMario.remove('Pepperoni')
        TotalPriceMario-=6.99
        return redirect('/mario')
    elif removepizzamario=='removeTuna':
        OverviewMario.remove('Tuna')
        TotalPriceMario-=7.99
        return redirect('/mario')

@app.route('/paymario', methods=['POST', 'GET'])
def overview_mario_pay():
    global uniqueID
    global totalOrder
    global allOrders
    current_time = datetime.now().time()
    uniqueID = current_time.hour * 3600 + current_time.minute * 60 + current_time.second
    totalOrder.append(uniqueID)
    for item in Overview:
        totalOrder.append(item)
    print(totalOrder)
    allOrders.append((totalOrder))

    return redirect('/resetmario')

@app.route('/resetmario', methods=['POST', 'GET'])
def reset_mario():
    global OverviewMario
    global TotalPriceMario
    OverviewMario = []
    TotalPriceMario = 0.00
    return redirect ('/mario')

@app.route('/pay', methods=['POST', 'GET'])
def overview_pay():
    global uniqueID
    global totalOrder
    global allOrders
    current_time = datetime.now().time()
    uniqueID = current_time.hour * 3600 + current_time.minute * 60 + current_time.second
    totalOrder.append(uniqueID)
    for item in Overview:
        totalOrder.append(item)
    print(totalOrder)
    allOrders.append((totalOrder))

    return redirect('/reset')

@app.route('/reset', methods=['POST', 'GET'])
def reset():
    global Overview
    global TotalPrice
    Overview = []
    TotalPrice = 0.00
    return redirect ('/confirmed')

@app.route('/confirmed', methods=['GET', 'POST'])
def payment_confirmed():
    return render_template('Confirmed.html', Overview=Overview, Margherita='Margherita', Pepperoni='Pepperoni', Tuna='Tuna', uniqueID = uniqueID)
app.run(host='192.168.0.101')
