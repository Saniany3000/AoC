import pandas as pd



MANDATORY_PASSPORT_KEYS = [
    'iyr',
    'ecl', 
    'cid', 
    'eyr',
    'pid', 
    'hcl', 
    'byr'
]

def process_input():
    # TODO: process input to return a list per passport
    pass

def method1(passports_list):
    valid_passport_cnt = 0

    for passport in passports_list:
        conds = [True if k in passport else False for k in MANDATORY_PASSPORT_KEYS]
        
        if all(conds):
            valid_passport_cnt += 1


    return valid_passport_cnt


if __name__ == "main":
    passports_list = process_input()
    print(method1(passports_list))
