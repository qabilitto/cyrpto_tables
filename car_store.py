import inquirer
from terminaltables import AsciiTable
from collections import namedtuple
import string
import operator
import re
import subprocess
Car=namedtuple('Car',['model','color','year','engine','mileage','price'])



car_details_question=[
    inquirer.Text('model',message='Enter car model',validate=lambda _,x : re.match('\w+',x)),
    inquirer.Text('color',message='Enter car color',validate=lambda _,x : re.match('\w+',x)),
    inquirer.Text('year',message='Enter car year',validate=lambda _,x: isinstance(int(x),int) and int(x) in range(1960,2019)),
    inquirer.Text('engine',message='Enter car engine',validate=lambda _,x: isinstance(int(x),int)),
    inquirer.Text('mileage',message='Enter car milage',validate=lambda _,x: isinstance(int(x),int)),
    inquirer.Text('price',message='Enter car price',validate=lambda _,x: isinstance(float(x),float)),
]
content=[]
data=[]
header=['model','color','year','engine','mileage','price']
data.append(['model','color','year','engine','mileage','price'])

def addcar():
   
    car_details_asnwer=inquirer.prompt(car_details_question)
    car_details_asnwer['year']=int(car_details_asnwer['year'])
    car_details_asnwer['engine']=int(car_details_asnwer['engine'])
    car_details_asnwer['mileage']=int(car_details_asnwer['mileage'])
    car_details_asnwer['price']=float(car_details_asnwer['price'])
    return car_details_asnwer
while True:
    #subprocess.Popen('clear')
    table=AsciiTable(data)
    table.inner_row_border=True
    print(table.table)
    questions=[
        inquirer.Text('con',message='Do you want to add car?')
    ]
    asn=inquirer.prompt(questions)
    if asn['con']=='yes':
        content.append([*Car(**addcar())])
        content.sort(key=operator.itemgetter(2))
        data=[data[0]]
        data.extend(content)
    req=[
        inquirer.List('options',message='What do you want to do?',
        choices=['sorting','buy','add'])
    ]
    a=inquirer.prompt(req)

    if a['options']=='sorting':
        requests=[
            inquirer.List('sortings',message='Do you want to sort by another options?',
            choices=['model','color','year','engine','mileage','price'])
            ]
        answer=inquirer.prompt(requests)
        content.sort(key=operator.itemgetter(header.index(answer['sortings'])))
        data=[data[0]]
        data.extend(content)
    elif a['options']=='buy':
        rq=[
           inquirer.Text('money',message='Enter money'),
           inquirer.Text('model',message='Enter model')
       ]
        ans=inquirer.prompt(rq)
        ans['money']=float(ans['money'])
        for i in content:
            if i[0]==ans['model']:
                if i[5]==ans['money']:
                   content.remove(i)
                elif i[5] > ans['money']:
                    print('you don\'t have enough money')
                else:
                    print('you are very mubarek here your money:',ans['money']-i[5])
                    content.remove(i)
                break
        data=[data[0]]
        data.extend(content)
    else:
        content.append([*Car(**addcar())])
        content.sort(key=operator.itemgetter(2))
        data=[data[0]]
        data.extend(content)