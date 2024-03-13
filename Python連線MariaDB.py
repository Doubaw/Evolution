#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import mariadb
import sys
import random
from datetime import datetime
import string
import time
import hashlib
from os import system

total = 100000
number = 10000

#create table
def table():
    cur.execute("drop table if exists test;")
    sql='''create table test(
            sn               int(10) AUTO_INCREMENT,
            timestamp        datetime(6),
            first_name       VARCHAR(25),
            last_name        VARCHAR(25),
            chinese_name     NVARCHAR(25),
            passwd           VARCHAR(100),
            money            int(10),
            mail             VARCHAR(100),
            amount DECIMAL(15,2) CHECK (amount >= 0.0),
            PRIMARY KEY(sn,timestamp))ENGINE=InnoDB;'''
    cur.execute(sql)

#create email
def email():
    maillen=random.randint(6,24)
    mailend=random.choice(('@yahoo.com.tw','@gmail.com','@edu.pccu.tw','@email.com','@icloud.com','@sina.com','@qq.com','@mail.edu.tw','@ntpc.edu.tw','@users.idbloc.co','@mailhero.io'))
    mail=string.digits+string.punctuation+string.ascii_letters
    str_len=maillen-4
    email=random.sample(mail,str_len)
    email_start=list(email)
    random.shuffle(email_start)
    finmail=''.join(email_start)+mailend
    return finmail

#create chinename
def chinename():
    zh = bytes.fromhex(f'{random.randint(0xb0, 0xf7):x}{random.randint(0xa1, 0xfe):x}').decode('gb18030')    +bytes.fromhex(f'{random.randint(0xb0, 0xf7):x}{random.randint(0xa1, 0xfe):x}').decode('gb18030')    +bytes.fromhex(f'{random.randint(0xb0, 0xf7):x}{random.randint(0xa1, 0xfe):x}').decode('gb18030')
    return zh

#create name
def name():
    Big=''.join(random.choice(string.ascii_letters[26:]) for x in range(1))
    intrandom = int(random.randint(1, 9))
    Little=''.join(random.choice(string.ascii_letters[:26]) for x in range(intrandom))
    last_name = Big+Little
    return last_name

#create paasswd
def pd():
    passwd = ''.join(random.choice(string.digits+string.punctuation+string.ascii_letters) for x in range(5))   
    md5 = hashlib.md5(passwd.encode('utf8')).hexdigest()
    return md5

own = []
def multi():
    own = []
    for i in range(total):
        sn = int(i+1)
        now = datetime.now()
        timestamp = now.strftime('%Y-%m-%d %H:%M:%S.%f')
        first_name = '.'.join(random.choice(string.ascii_letters[26:]) for x in range(3))
        last_name = name()
        chinese_name = chinename()
        passwd = pd()
        money = int(random.randint(1, 10000000))
        mail = email()
        amount = int(random.randrange(1000000000, 1000000000000))
        own.append((sn,timestamp,first_name,last_name,chinese_name,passwd,money,mail,amount))
    return own       

one = []
count = total
def only():
    global count
    count += 1
    one = []
    for i in range(1):
        sn = int(count)
        now = datetime.now()
        timestamp = now.strftime('%Y-%m-%d %H:%M:%S.%f')
        first_name = '.'.join(random.choice(string.ascii_letters[26:]) for x in range(3))
        last_name = name()
        chinese_name = chinename()
        passwd = pd()
        money = int(random.randint(1, 10000000))
        mail = email()
        amount = int(random.randrange(1000000000, 1000000000000))
        one.append((sn,timestamp,first_name,last_name,chinese_name,passwd,money,mail,amount))
    return one

#create initialized data   
def add_multiple_contacts(cur, own):
    own = multi()
    cur.executemany("INSERT INTO test(sn,timestamp,first_name,last_name,chinese_name,passwd,money,mail,amount) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",own)
    conn.commit()

#create single data  
def instart_contact(cur, one):
    one = only()
    cur.executemany("INSERT INTO test(sn,timestamp,first_name,last_name,chinese_name,passwd,money,mail,amount) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",one)
    conn.commit()
    
#update data
def update_contact(cur, change, mail, timestamp, sn):
    cur.execute("UPDATE test SET amount=(amount-?), mail=?, timestamp=? WHERE sn=?",(change, mail, timestamp, sn))

#delete data
def remove_contact(cur, sn):
    cur.execute("DELETE FROM test WHERE sn=?", (sn, ))
    conn.commit()
    
#print data
def print_contacts(cur):
    contacts = []
    cur.execute("SELECT sn,timestamp,first_name,mail,amount FROM test")
    for (sn, timestamp, first_name, mail, amount) in cur:
        contacts.append(f"{sn} {timestamp} {first_name} {mail} {amount}")
    print("\n".join(contacts))
    
# def start_contact(cur):
#     cur.execute("SELECT min(timestamp) FROM test;")
#     starttime = cur.fetchone()
#     print(starttime)

count = total
def start_contact(cur):
    #sn must be the same as the initialized number(total)
    global count
    cur.execute("SELECT timestamp FROM test where sn=?",(count, ))
    starttime = cur.fetchone()
    print(starttime)
    
def end_contact(cur):
    cur.execute("SELECT max(timestamp) FROM test;")
    endtime = cur.fetchone()
    print(endtime)
    
def count_contact(cur):
    cur.execute("SELECT count(*) FROM test;")
    allcontact = cur.fetchone()
    print(allcontact)
    
def truncate_contacts(cur):
    cur.execute("TRUNCATE test")

try:
    conn = mariadb.connect(
    user="remoteuser",
    password="Aa123456",
    host="192.168.32.20",
    database="testdb",
    port=3306)
    cur = conn.cursor()
    
    table()
    add_multiple_contacts(cur, own)
    print("multiple")
#     print_contacts(cur)

    start_contact(cur)
    
    for i in range(number):
        instart_contact(cur, one)
    print("insert")
#     print_contacts(cur)
    
    seq = list(range(1,count+1))
    numb = random.sample(seq,count)
    for i in range(number):
        now = datetime.now()
        timestamp = now.strftime('%Y-%m-%d %H:%M:%S.%f')
        mail = email()   
        sn = numb[i]   
        change = int(random.randrange(100, 100000000))
        update_contact(cur, change, mail, timestamp, sn)
    print("update")
#     print_contacts(cur)

    seq = list(range(1,count+1))
    numb = random.sample(seq,count)
    for i in range(number): 
        sn = numb[i]  
        remove_contact(cur,sn)
    print("delete")
#     print_contacts(cur)

    
    end_contact(cur)
    count_contact(cur)
    
#     truncate_contacts(cur)
#     print("truncate")
#     print_contacts(cur)

except Exception as e:
    print(f"Error commiting transaction: {e}")
finally:    
    cur.close()
    conn.close()
    

system('pause')

