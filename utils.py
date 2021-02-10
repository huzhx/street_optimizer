import re
import requests

def shift_num(num):
    ''' Return a string
    if num < 10 make it 10
    if num % 10 == 0 add 5
    else get rid of the num at the unit's digit
    '''
    num = int(num)
    if (num < 10):
        num = 10
    elif (num % 10 == 0):
        num += 5
    else:
        num = num // 10 * 10
    return str(num)

def remove_num(addr):
    ''' Input address in string 
        Return a string
    if a number is concatenated with a string like xxxstr, leave the number since it is normally part of the street name. 
    However, if a number appears alone or concatenated after a string like strxxx, remove the number
    '''
    addr = re.sub(r'([a-zA-Z ]+)(\d+)(\W|\s|$)', r'\1', addr.strip())
    return addr.strip()

def consume_api(api_endpoint, payload):
    resp = requests.post(api_endpoint, json=payload)
    if (resp.status_code != 200 and resp.status_code != 201):
        raise Exception('POST {} {}'.format(api_endpoint, resp.status_code))
    return resp.json()

def strip_apt_term(addr):
    ''' Input addresses in string
        Return a string
    '''
    apt_terms = ["apartment", "ap", "apt", "basement", "box", "bsmt", "building", "bldg", "department", "dept", "floor", "fl", "front", "frnt", "hanger", "hngr", "key", "lobby", "lbby", "lot", "lower", "lowr", "no", "office", "ofc", "penthouse", "ph", "pier", "rear", "room", "rm", "side", "slip", "space", "spc", "stop", "suite", "ste", "trailer", "trlr", "unit", "upper", "uppr", "#"]
    
    for apt_term in apt_terms:
        if (apt_term in addr):
            addr = addr.split(apt_term)[0].strip()
    return addr