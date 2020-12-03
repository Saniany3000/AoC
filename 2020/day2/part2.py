"""
While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

"""

position = pwd.copy()

position.rename(columns={'minimun':'position_1','maximun':'position_2'},inplace=True)

position['func_position_1'] = 'na'
position['func_position_2'] = 'na'

def get_positions(df):
    for i,row in df.iterrows():
        word_list = list(row['pwd'])
        if len(word_list)>=2:
            df.set_value(i,'func_position_1', word_list[row['position_1']-1])
            df.set_value(i,'func_position_2', word_list[row['position_2']-1])
        elif len(count_letter_postion)==1:
            df.set_value(i,'func_position_1', word_list[row['position_1']-1])
            df.set_value(i,'func_position_2', 'not_a_letter')
        elif len(count_letter_postion)==0:
            df.set_value(i,'func_position_1', 'not_a_letter')
            df.set_value(i,'func_position_2', 'not_a_letter')
        else:
            pass
get_positions(position)

position['position_eval_flag'] = 0

def evaluate_positions(df):
    for i,row in df.iterrows():
        if row['func_position_1'] == row['letter'] and row['func_position_2'] == row['letter']:
            df.set_value(i,'position_eval_flag',0)
        elif row['func_position_1'] == row['letter'] and row['func_position_2'] != row['letter']:
            df.set_value(i,'position_eval_flag',1)
        elif row['func_position_1'] != row['letter'] and row['func_position_2'] == row['letter']:
            df.set_value(i,'position_eval_flag',1) 
        elif row['func_position_1'] != row['letter'] and row['func_position_2'] != row['letter']:
            df.set_value(i,'position_eval_flag',0)     

evaluate_positions(position)

position['position_eval_flag'].sum()