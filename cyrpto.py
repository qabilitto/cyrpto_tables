import inquirer,terminaltables
from urllib.request import urlopen
import json
from pprint import pprint
import operator

with urlopen('https://api.coinmarketcap.com/v2/listings/') as url:
    raw_data = url.read()
    info=json.loads(raw_data)
page=0
headers=['id','name','symbol','website_slug']
while True:
    data=[list(info['data'][i].values()) for i in range(page*10,(page+1)*10)]
    tab=terminaltables.ascii_table.AsciiTable(data)
    tab.inner_row_border=True
    print(tab.table)

    option=[
        inquirer.List('opt',message='What do you want?',
        choices=['listing','sorting','search'])
    ]
    a=inquirer.prompt(option)
    if a['opt']=='listing':
        command=[
            inquirer.List('opt',choices=['next','back'])
        ]
        ans=inquirer.prompt(command)
        if ans['opt']=='next':
            page+=1
        else:
            page-=1
    elif a['opt']=='sorting':
        command=[
            inquirer.List('column',message='Select column',
            choices=headers)
        ]
        answer=inquirer.prompt(command)
        info['data'].sort(key=operator.itemgetter(answer['column']))
    
    else:
        command=[
            inquirer.Text('val',message='Type value')
        ]
        answer=inquirer.prompt(command)
        data=[list(row.values()) for row in info['data'] for i in list(row.values()) if type(i) is str and answer['val'] in i]
        tab=terminaltables.ascii_table.AsciiTable(data)
        tab.inner_row_border=True
        print(tab.table)
        command=[
            inquirer.List('c',message='Do you want to continue?',choices=['yes','no'])
        ]
        
        a=inquirer.prompt(command)
        if a['c']=='yes':
            continue
        else:
            break

       



