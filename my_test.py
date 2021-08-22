import re
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
mo = phone_num_regex.search('私の電話番号は415-555-4242です.')
if __name__ == '__main__':
    print(mo.group())