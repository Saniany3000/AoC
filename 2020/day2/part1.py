"""
--- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?


"""
import pandas as pd
from collections import Counter


## Cleaning and arrange data

pwd = pd.read_csv('data.txt',sep=' ', names=['min_max','letter','pwd'])
pwd[['minimun','maximun']] = pwd.min_max.str.split('-',expand=True)
pwd.minimun = pwd.minimun.astype(int)
pwd.maximun = pwd.maximun.astype(int)
pwd['letter'] = pwd['letter'].str.replace(':','')
pwd.drop(columns=['min_max'],inplace=True)
pwd = pwd[['pwd','letter','minimun','maximun']]
pwd['letter_count'] = 0
pwd['policy_flag'] = 0

def check_policy(df):
    for i, row in df.iterrows():
        if row['letter'] in row['pwd']:
            pwd_dict = Counter(row['pwd'])
            value = pwd_dict[row['letter']]
            value = int(value)
            df.set_value(i,'letter_count',value)
            if value >= int(row['minimun']) and value <= int(row['maximun']):
                df.set_value(i,'policy_flag',1)
            else:
                df.set_value(i,'policy_flag',0)
        else:
            pass

check_policy(pwd)

pwd.policy_flag.sum()


### method 2 separate lambdas

pwd['method_2_letter_present_flag'] = 0

pwd['method_2_letter_present_flag'] = pwd.apply(lambda x: 1 if x.letter in x.pwd else 0, axis=1)

pwd['method_2_letter_count'] = pwd.apply(lambda x: Counter(x.pwd)[x.letter] if x.method_2_letter_present_flag == 1 else 0, axis=1)

pwd['method_2_policy_flag'] = pwd.apply(lambda x: 1 if x.method_2_letter_count >= x.minimun and x.method_2_letter_count <= x.maximun else 0, axis=1)

pwd['method_2_policy_flag'].sum()


### method 3 one big ass lambda

pwd['method_3'] = pwd.apply(lambda x: 1 if x.letter in x.pwd and (Counter(x.pwd)[x.letter] >= x.minimun and Counter(x.pwd)[x.letter] <= x.maximun) else 0, axis=1)

pwd['method_3'].sum() 
