#!/usr/bin/env python3

import requests
import argparse
import json


URL = 'https://lookup.binlist.net/'

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('list', nargs='*', help = "card number")
    parser.add_argument("-f", "--file", help = "json file")
    args = parser.parse_args()
    return args

def get_card_info(n):
    r = requests.get(URL + str(n), headers={'Accept-Version': '3'})
    if 200 <= r.status_code < 300:
        card_data = r.json()
        return True, card_data
    else:
        return False, r.status_code

def read_file(filename):
    with open('./{}'.format(filename)) as f:
        cards_list = json.loads(f.read())
    for card in cards_list:
        yield card['CreditCard']['CardNumber']

def print_info(info):
    if info[0]:
        print(json.dumps(info[1], indent=2))
    else:
        print('error! status code: {}'.format(info[1]))

get_bank_name = lambda x: x['bank']['name'] if x['bank'].get('name') else None

def main():
    args = get_args()
    bank_set = set()
    if args.file:
        for card_number in read_file(args.file):
            result = get_card_info(card_number)
            if result[0]:
                # print(json.dumps(result[1], indent=2))
                bank_set.add(get_bank_name(result[1]))
            # print_info(result)
    else:
        for card_number in args.list:
            result = get_card_info(card_number)
            if result[0]:
                # print(json.dumps(result[1], indent=2))
                bank_set.add(get_bank_name(result[1]))
            # print_info(result)

    try:
        bank_set.remove(None)
    except:
        pass

    for bank in sorted(bank_set):
        print(bank)


if __name__ == "__main__":
    main()

    



    
    
