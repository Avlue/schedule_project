import schedule
import time
import csv 

def write_csv():
    name = input('Enter your name: ')
    age = in(input('Enter your age: '))
    with open('users.csv', 'a') as  csv_file:
        writer = csv.writer(csv_file, delimiter='/')
        writer.writerow(
            (name, age)
        )
    answer = input('Continue? Yes or No: ')
    if answer == 'y':
        write_csv()
    else:
        print('Stop!')

def mailing():
    with open('users.csv', 'r') as csv_file:
        data = csv_file.readlines()
        names = [i.replace('\n', '') for i in data]
        for i in names:
            name = i.split('/')
            if int(name[-1]) >= 18:
                print(f'Skidki segodnya! {name[0]}')

schedule.every(3).seconds.do(mailing)

while True:
    schedule.run_pending
    time.sleep(1)

write_csv()
mailing()