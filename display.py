import json


def displayData(option):
    option = int(option)
    opt = ['student', 'lexturer', 'general staff', 'all']
    with open('details.json', 'r') as json_file:
        data = json.load(json_file)
        for d in data['data']:
            if d['type'] != opt[option - 1]:
                if option != 4:
                    continue
            print('*'*60)
            print('Type: ' + d['type'])
            print('First Name: ' + d['details']['first_name'])
            print('Last Name: ' + d['details']['last_name'])
            print('Birth Date: ' + d['details']['birth_date'])
            print('Email: ' + d['details']['email'])
            print('*'*60)
