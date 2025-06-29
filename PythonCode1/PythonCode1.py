import sys
import math
import calendar
import module1
import json

def calculate_area(base,height):
    print("__name__", __name__)
    return 1/2 * (base*height)

if __name__ == "__main__":
    print("Main File")
    a = calculate_area(10,20)
    print(a)


def codeRW():
    with open("txt.txt", "r") as f:
        for line in f:
            tokens = line.split(' ')
            print("This line has {0} words".format(len(tokens)))
    isClosed = f.closed
    print("Was the file closed? {0}".format(isClosed))

codeRW()

def codeJSON():
    book = {}
    book['key1'] = {
        'name': 'access1',
        'address': '1 red street, ny',
        'phone': 5559899898
        }
    book['key2'] = {
        'name': 'access2',
        'address': '2 red street, ny',
        'phone': 5559891234
        }
    s = json.dumps(book)
    print(s)


def code13M():
    print(module1.calcS(5))

def code12():
    print(calendar.month(2025,6))
    print(math.sqrt(16))
    print(math.pow(16,2))
    print(math.log10(1000))
    print(math.floor(2.3))
    print(math.ceil(2.3))

def code10():
    point = (5,9,10,12)
    tmp = point[0]
    print(tmp)

def code11():
    d1 = {
        "Tom": 5556789099,
        "Rob": 5556781234,
        "Joe": 5559091332
    }
    print("Tom" in d1)
    print(d1["Tom"])
    d1["Sam"] = 5555553213
    print(d1)

    for k,v in d1.items():
        print(k,v)

total = 0
def code9(a,b):
    global total 
    total = a + b
    return total

def code8(exp):
    total = 0
    for item in exp:
        total = total + item
    return total

tomL = [2100, 3400, 3500]
joeL = [200,500,700]

tomT = code8(tomL)
joeT = code8(joeL)
total = tomT + joeT

def code7():
    j = 0
    for i in range(1,6,1):
        print(i * i)
    while(j <= 5):
        print(j)
        j = j + 1



def code6():
    loc = "chair"
    locs = ["garage", "livingroom", "chair", "closet"]
    for i in locs:
        if(i == loc):
            print("Keys Found", i)
            break
        else:
            print("Keys Not Found", i)


def code5():
    total = 0
    exp = [2340, 2500, 2100, 3100, 2900]
    for i in range(len(exp)):
        print("Month {0} - {1}".format((i+1), exp[i]))
        total = total + exp[i]
    print(total)

def code4():
    exp = [2340, 2500, 2100, 3100, 2980]
    #total = exp[0] + exp[1] + exp[2] + exp[3] + exp[4]
    total = 0
    for i in exp:
        total = total + i
    print("Totat Expense ${0}".format(total))

def code2():
    num = input("Enter a number ")
    num = int(num)
    if(num % 2 == 0):
        print("Number is Even")
    else:
        print("Number is Odd")

def code3():
    indian = ["somosa", "daal", "naan"]
    chinese = ["egg", "soup", "rice"]
    italian = ["pizza", "ziti", "risotto"]
    dish = input("Enter a dish name: ")
    if(dish in indian):
        print("indian food")
    elif(dish in chinese):
        print("chinese food")
    elif(dish in italian):
        print("italian food")
    else:
        print("not on the menu")

def code1():
    food = ["bread","pasta","fruits"]
    bathroom = ["shampoo","soap"]
    items = food + bathroom
    print("I will shop for these items {0}".format(items))
    print("I am buying {0} items".format(len(items)))
    check1 = "soap" in items
    print(check1)
    item1 = "bread"
    item2 = "pasta"
    item3 = "fruits"
    items = [item1,item2,item3,'veggies']
    items.insert(1,"butter")
    print(items)
    print(items[0])
    print(items[2])
    items[3] = item1
    print(items)
    print(items[2:4])
    print(items[-1])
    text = "jello store"
    print(text)
    print(text[0:5])
    text2 = 'let\'s go'
    tmp = text + " " + text2
    print(tmp)
    print(text2)
    rent = 1220
    gas = 202.5
    groceries = 305.6
    nyc_bal = 188
    bal_pitt = 247
    total_dist = nyc_bal + bal_pitt
    print(total_dist)
    mph = 65
    time = total_dist / mph
    print(time)
    calc = 10 + 2 * 3
    print(calc)
    calc = 10 + (2 * 3)
    print(calc)
    sum1 = 12 + 34
    divide = 12 / 34
    print(divide)
    mod = 11 % 2
    print(mod)
    pow1 = 3**2
    print(pow1)
    print("${0}".format(rent))
    total = rent + gas + groceries
    print("${0}".format(total))
    rent = 1400
    tax = 120
    total = rent + gas + groceries + tax
    print("${0}".format(total))


