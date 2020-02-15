import json
import os


def write_json(data, filename='details.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def get_option(opt):
    with open('details.json') as json_file:
        data = json.load(json_file)
        temp = data['data']
        y = dataCreation(opt)
        temp.append(y)

    write_json(data)
    os.system('clear')
    print('Data saved!')


def dataCreation(option):
    option = int(option)
    Type_ = ['student', 'lexturer', 'general staff']
    print('Please enter ' + Type_[option - 1] + ' details:')
    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    birth_date = input('Birth Date: ')
    email = input('Email: ')

    details = {
        'type': Type_[option - 1],
        'details': {
            'first_name': first_name,
            'last_name': last_name,
            'birth_date': birth_date,
            'email': email
        }
    }
    return details
