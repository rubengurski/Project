totalOrder = {}

allOrders=[]

overview=['Margherita', 'Pepperoni', 'Tuna']
overview2=['Tuna', 'Maragherita', 'yee']

totalOrder["uniqueID"]=23543
for item in overview:
    totalOrder.update({"pizza":item})

allOrders.append(totalOrder)
print(str(totalOrder))

totalOrder.clear()

x=1
totalOrder["uniqueID"]=23000
for item in overview2:
    if x<(len(overview2)+1):
        totalOrder["pizza" + str(x)]=str(item)
        x+=1

allOrders.append(totalOrder)

print(str(totalOrder))
print(str(allOrders))

# for order in allOrders:
#     print("Order nr: " + str(totalOrder["uniqueID"]))
#     print(str(totalOrder["pizza1"]))
#     print(str(totalOrder["pizza2"]))
#     if "pizza3"!=None:
#         print(str(totalOrder["pizza3"]))
