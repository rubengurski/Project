from flask import Flask
from flask import render_template
from flask import request, redirect
import csv
from datetime import datetime

app = Flask(__name__)

x=1
Overview=[]
amountMargherita=0
amountPepperoni=0
amountTuna=0
amounts=[]
TotalPrice=0
OverviewMario=[]
amountMargheritaMario=0
amountPepperoniMario=0
amountTunaMario=0
amountsMario=[]
TotalPriceMario=0
Orders=[]
allOrders=[]
scroll=''
uniqueID=''
# structure of a totalOrder dictionary:
# totalOrder = {
    # "uniqueID":'',
    # "pizza1":'',
    # "pizza2":'',
    # "pizza3":'',
    # "amount1":'',
    # "amount2":'',
    # "amount3":''
# }
totalOrder1 = {}; totalOrder2 = {}; totalOrder3 = {}; totalOrder4 = {}; totalOrder5 = {}


@app.route('/', methods=['POST', 'GET'])
def home():
    global Overview
    roundedTotalPrice = round(TotalPrice, 2)
    return render_template('Home.html', Overview=Overview, Margherita='Margherita', Pepperoni='Pepperoni', Tuna='Tuna', TotalPrice=roundedTotalPrice, scroll=scroll, amountMargherita=amountMargherita, amountPepperoni=amountPepperoni, amountTuna=amountTuna)

@app.route('/mario', methods=['POST', 'GET'])
def mario():
    roundedTotalPriceMario = round(TotalPriceMario, 2)
    return render_template('Mario.html', OverviewMario=OverviewMario, Margherita='Margherita', Pepperoni='Pepperoni', Tuna='Tuna', TotalPriceMario=roundedTotalPriceMario, amountMargheritaMario=amountMargheritaMario, amountPepperoniMario=amountPepperoniMario, amountTunaMario=amountTunaMario)

@app.route('/luigi', methods=['POST', 'GET'])
def luigi():
    global allOrders, totalOrder1, totalOrder2, totalOrder3, totalOrder4, totalOrder5
    pizza1="pizza1"; pizza2="pizza2"; pizza3="pizza3"; amount1="amount1"; amount2="amount2"; amount3="amount3"
    if amount1==0:
        amount1=''
    if amount2==0:
        amount2=''
    if amount3==0:
        amount3=''
    print(allOrders)
    n = 0
    return render_template('Luigi.html', Overview=Overview, allOrders = allOrders, uniqueID=uniqueID, n=n, pizza1=pizza1, pizza2=pizza2, pizza3=pizza3, amount1=amount1, amount2=amount2, amount3=amount3)

@app.route('/screen', methods=['POST', 'GET'])
def screen_customers():
    global allOrders, totalOrder1, totalOrder2, totalOrder3, totalOrder4, totalOrder5
    return render_template('Screen.html', allOrders = allOrders, uniqueID=uniqueID)

@app.route('/status', methods = ['POST'])
def sstatus():
    data = request.get_json()
    global status
    status = data['status']
    
    print(status)
    return '200', 200

@app.route('/addpizza', methods = ['POST'])
def add_pizza():
    global TotalPrice, scroll, amountMargherita, amountPepperoni, amountTuna
    addpizza = str(request.form['addpizza'])
    if addpizza not in Overview:
        if addpizza=='Margherita':
            TotalPrice+=5.99
            amountMargherita+=1
            Overview.append(addpizza)
        if addpizza=='Pepperoni':
            TotalPrice+=6.99
            amountPepperoni+=1
            Overview.append(addpizza)
        if addpizza=='Tuna':
            TotalPrice+=7.99
            amountTuna+=1
            Overview.append(addpizza)
    else:
        if addpizza=='Margherita':
            TotalPrice+=5.99
            amountMargherita+=1
        if addpizza=='Pepperoni':
            TotalPrice+=6.99
            amountPepperoni+=1
        if addpizza=='Tuna':
            TotalPrice+=7.99
            amountTuna+=1
    scroll='home'

    print('Data received:', addpizza, '\n current overview:', Overview)  # See console...
    return redirect('/')

@app.route('/removepizza', methods=['POST', 'GET'])
def overview_remove():
    global TotalPrice, scroll, amountMargherita, amountPepperoni, amountTuna
    scroll='home'
    removePizza=str(request.form['removePizza'])
    if removePizza=='removeMargherita':
        Overview.remove('Margherita')
        TotalPrice-= (5.99 * amountMargherita)
        amountMargherita=0
        return redirect('/')
    elif removePizza=='removePepperoni':
        Overview.remove('Pepperoni')
        TotalPrice-= (6.99 * amountPepperoni)
        amountPepperoni=0
        return redirect('/')
    elif removePizza=='removeTuna':
        Overview.remove('Tuna')
        TotalPrice-= (7.99 * amountTuna)
        amountTuna=0
        return redirect('/')

@app.route('/pay', methods=['POST', 'GET'])
def overview_pay():
    global uniqueID, allOrders, x, amounts
    current_time = datetime.now().time()
    uniqueID = current_time.hour * 3600 + current_time.minute * 60 + current_time.second
    amounts=[]
    if len(Overview)==0:
        return redirect('/')
    if x==1:
        totalOrder1["uniqueID"]=uniqueID
        y=1
        for item in Overview:
            if y<(len(Overview)+1):
                totalOrder1["pizza" + str(y)]=str(item)
                if item=="Margherita":
                    amounts.append(amountMargherita)
                if item=="Pepperoni":
                    amounts.append(amountPepperoni)
                if item=="Tuna":
                    amounts.append(amountTuna)
                y+=1
        z=1
        for amount in amounts:
            if z<(len(amounts)+1):
                totalOrder1["amount" + str(z)]=str(amount)
                z+=1
        print(totalOrder1)
        allOrders.append(totalOrder1)
        print(str(allOrders))
    elif x==2:
        totalOrder2["uniqueID"]=uniqueID
        y=1
        for item in Overview:
            if y<(len(Overview)+1):
                totalOrder2["pizza" + str(y)]=str(item)
                if item=="Margherita":
                    amounts.append(amountMargherita)
                if item=="Pepperoni":
                    amounts.append(amountPepperoni)
                if item=="Tuna":
                    amounts.append(amountTuna)
                y+=1
        z=1
        for amount in amounts:
            if z<(len(amounts)+1):
                totalOrder2["amount" + str(z)]=str(amount)
                z+=1
        print(totalOrder2)
        allOrders.append(totalOrder2)
        print(str(allOrders))
    elif x==3:
        totalOrder3["uniqueID"]=uniqueID
        y=1
        for item in Overview:
            if y<(len(Overview)+1):
                totalOrder3["pizza" + str(y)]=str(item)
                if item=="Margherita":
                    amounts.append(amountMargherita)
                if item=="Pepperoni":
                    amounts.append(amountPepperoni)
                if item=="Tuna":
                    amounts.append(amountTuna)
                y+=1
        z=1
        for amount in amounts:
            if z<(len(amounts)+1):
                totalOrder3["amount" + str(z)]=str(amount)
                z+=1
        print(totalOrder3)
        allOrders.append(totalOrder3)
        print(str(allOrders))
    elif x==4:
        totalOrder4["uniqueID"]=uniqueID
        y=1
        for item in Overview:
            if y<(len(Overview)+1):
                totalOrder4["pizza" + str(y)]=str(item)
                if item=="Margherita":
                    amounts.append(amountMargherita)
                if item=="Pepperoni":
                    amounts.append(amountPepperoni)
                if item=="Tuna":
                    amounts.append(amountTuna)
                y+=1
        z=1
        for amount in amounts:
            if z<(len(amounts)+1):
                totalOrder4["amount" + str(z)]=str(amount)
                z+=1
        print(totalOrder4)
        allOrders.append(totalOrder4)
        print(str(allOrders))
    elif x==5:
        totalOrder5["uniqueID"]=uniqueID
        y=1
        for item in Overview:
            if y<(len(Overview)+1):
                totalOrder5["pizza" + str(y)]=str(item)
                if item=="Margherita":
                    amounts.append(amountMargherita)
                if item=="Pepperoni":
                    amounts.append(amountPepperoni)
                if item=="Tuna":
                    amounts.append(amountTuna)
                y+=1
        z=1
        for amount in amounts:
            if z<(len(amounts)+1):
                totalOrder5["amount" + str(z)]=str(amount)
                z+=1
        print(totalOrder5)
        allOrders.append(totalOrder5)
        print(str(allOrders))
    x+=1
    return redirect('/reset')

@app.route('/reset', methods=['POST', 'GET'])
def reset():
    global Overview, TotalPrice, amountMargherita, amountPepperoni, amountTuna, amounts
    Overview = []
    amounts=[]
    amountMargherita=0; amountPepperoni=0; amountTuna=0
    TotalPrice = 0.00
    return redirect ('/confirmed')

@app.route('/confirmed', methods=['GET', 'POST'])
def payment_confirmed():
    return render_template('Confirmed.html', Overview=Overview, Margherita='Margherita', Pepperoni='Pepperoni', Tuna='Tuna', uniqueID = uniqueID)

@app.route('/addpizzamario', methods = ['POST'])
def add_pizza_mario():
    global TotalPriceMario, amountMargheritaMario, amountPepperoniMario, amountTunaMario
    addpizzamario = str(request.form['addpizzamario'])
    if addpizzamario not in OverviewMario:
        if addpizzamario=='Margherita':
            TotalPriceMario+=5.99
            amountMargheritaMario+=1
            OverviewMario.append(addpizzamario)
        if addpizzamario=='Pepperoni':
            TotalPriceMario+=6.99
            amountPepperoniMario+=1
            OverviewMario.append(addpizzamario)
        if addpizzamario=='Tuna':
            TotalPriceMario+=7.99
            amountTunaMario+=1
            OverviewMario.append(addpizzamario)
        global TotalPrice, scroll, amountMargherita, amountPepperoni, amountTuna
    else:
        if addpizzamario=='Margherita':
            TotalPriceMario+=5.99
            amountMargheritaMario+=1
        if addpizzamario=='Pepperoni':
            TotalPriceMario+=6.99
            amountPepperoniMario+=1
        if addpizzamario=='Tuna':
            TotalPriceMario+=7.99
            amountTunaMario+=1
    print('Data received:', addpizzamario, '\n current overview Mario:', OverviewMario)  # See console...
    return redirect('/mario')

@app.route('/removepizzamario', methods=['POST', 'GET'])
def overview_remove_mario():
    global TotalPriceMario, amountMargheritaMario, amountPepperoniMario, amountTunaMario
    removepizzaMario=str(request.form['removepizzaMario'])
    if removepizzaMario=='removeMargherita':
        OverviewMario.remove('Margherita')
        TotalPriceMario-= (5.99 * amountMargheritaMario)
        amountMargheritaMario=0
        return redirect('/mario')
    elif removepizzaMario=='removePepperoni':
        OverviewMario.remove('Pepperoni')
        TotalPriceMario-= (6.99 * amountPepperoniMario)
        amountPepperoniMario=0
        return redirect('/mario')
    elif removepizzaMario=='removeTuna':
        OverviewMario.remove('Tuna')
        TotalPriceMario-= (7.99 * amountTunaMario)
        amountTunaMario=0
        return redirect('/mario')

@app.route('/paymario', methods=['POST', 'GET'])
def overview_pay_mario():
    global uniqueID, allOrders, x, amountsMario
    current_time = datetime.now().time()
    uniqueID = current_time.hour * 3600 + current_time.minute * 60 + current_time.second
    amountsMario=[]
    if len(OverviewMario)==0:
        return redirect('/mario')
    if x==1:
        totalOrder1["uniqueID"]=uniqueID
        y=1
        for item in OverviewMario:
            if y<(len(OverviewMario)+1):
                totalOrder1["pizza" + str(y)]=str(item)
                if item=="Margherita":
                    amountsMario.append(amountMargheritaMario)
                if item=="Pepperoni":
                    amountsMario.append(amountPepperoniMario)
                if item=="Tuna":
                    amountsMario.append(amountTunaMario)
                y+=1
        z=1
        for amount in amountsMario:
            if z<(len(amountsMario)+1):
                totalOrder1["amount" + str(z)]=str(amount)
                z+=1
        print(totalOrder1)
        allOrders.append(totalOrder1)
        print(str(allOrders))
    elif x==2:
        totalOrder2["uniqueID"]=uniqueID
        y=1
        for item in OverviewMario:
            if y<(len(OverviewMario)+1):
                totalOrder2["pizza" + str(y)]=str(item)
                if item=="Margherita":
                    amountsMario.append(amountMargheritaMario)
                if item=="Pepperoni":
                    amountsMario.append(amountPepperoniMario)
                if item=="Tuna":
                    amountsMario.append(amountTunaMario)
                y+=1
        z=1
        for amount in amountsMario:
            if z<(len(amountsMario)+1):
                totalOrder2["amount" + str(z)]=str(amount)
                z+=1
        print(totalOrder2)
        allOrders.append(totalOrder2)
        print(str(allOrders))
    elif x==3:
        totalOrder3["uniqueID"]=uniqueID
        y=1
        for item in OverviewMario:
            if y<(len(OverviewMario)+1):
                totalOrder3["pizza" + str(y)]=str(item)
                if item=="Margherita":
                    amountsMario.append(amountMargheritaMario)
                if item=="Pepperoni":
                    amountsMario.append(amountPepperoniMario)
                if item=="Tuna":
                    amountsMario.append(amountTunaMario)
                y+=1
        z=1
        for amount in amountsMario:
            if z<(len(amountsMario)+1):
                totalOrder3["amount" + str(z)]=str(amount)
                z+=1
        print(totalOrder3)
        allOrders.append(totalOrder3)
        print(str(allOrders))
    elif x==4:
        totalOrder4["uniqueID"]=uniqueID
        y=1
        for item in OverviewMario:
            if y<(len(OverviewMario)+1):
                totalOrder4["pizza" + str(y)]=str(item)
                if item=="Margherita":
                    amountsMario.append(amountMargheritaMario)
                if item=="Pepperoni":
                    amountsMario.append(amountPepperoniMario)
                if item=="Tuna":
                    amountsMario.append(amountTunaMario)
                y+=1
        z=1
        for amount in amountsMario:
            if z<(len(amountsMario)+1):
                totalOrder4["amount" + str(z)]=str(amount)
                z+=1
        print(totalOrder4)
        allOrders.append(totalOrder4)
        print(str(allOrders))
    elif x==5:
        totalOrder5["uniqueID"]=uniqueID
        y=1
        for item in OverviewMario:
            if y<(len(OverviewMario)+1):
                totalOrder5["pizza" + str(y)]=str(item)
                if item=="Margherita":
                    amountsMario.append(amountMargheritaMario)
                if item=="Pepperoni":
                    amountsMario.append(amountPepperoniMario)
                if item=="Tuna":
                    amountsMario.append(amountTunaMario)
                y+=1
        z=1
        for amount in amountsMario:
            if z<(len(amountsMario)+1):
                totalOrder5["amount" + str(z)]=str(amount)
                z+=1
        print(totalOrder5)
        allOrders.append(totalOrder5)
        print(str(allOrders))
    x+=1
    return redirect('/resetmario')

@app.route('/resetmario', methods=['POST', 'GET'])
def reset_mario():
    global OverviewMario, TotalPriceMario, amountMargheritaMario, amountPepperoniMario, amountTunaMario, amountsMario
    OverviewMario = []
    amountsMario=[]
    amountMargheritaMario=0; amountPepperoniMario=0; amountTunaMario=0
    TotalPriceMario = 0.00
    return redirect ('/mario')

app.run(host='192.168.0.104')