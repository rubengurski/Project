from flask import Flask
from flask import render_template
from flask import request, redirect
import csv
from datetime import datetime

app = Flask(__name__)

Overview=[]
Orders=[]
TotalPrice=0
scroll=''
uniqueID=''

@app.route('/', methods=['POST', 'GET'])
def home():
    global Overview
    
    return render_template('Home.html', Overview=Overview, Margherita='Margherita', Pepperoni='Pepperoni', Tuna='Tuna', TotalPrice=TotalPrice, scroll=scroll)

@app.route('/mario', methods=['POST', 'GET'])
def mario():
    return render_template('Mario.html')

@app.route('/luigi', methods=['POST', 'GET'])
def luigi():
    global uniqueID
    with open('order_' + str(uniqueID) + '.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['Pizza'], row['uniqueID'])
            Orders['Pizza']=uniqueID
    print(str(Orders))
    return render_template('Luigi.html', Overview=Overview, uniqueID=uniqueID, Orders=Orders)

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

@app.route('/pay', methods=['POST', 'GET'])
def overview_pay():
    global uniqueID
    current_time = datetime.now().time()
    uniqueID = current_time.hour * 3600 + current_time.minute * 60 + current_time.second
    with open('order_' + str(uniqueID) + '.csv', 'a', newline='') as csvfile:
        fieldnames = ['Pizza', 'uniqueID']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for pizza in Overview:
            writer.writerow({'Pizza':pizza})
        writer.writerow({'Pizza':None})
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
