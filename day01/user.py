#!/usr/bin/env python3.7
#coding:utf-8

'''
locked.txt:
liuxiaoyu
xiaodong
tenglan

match.txt
alex 123456
xiaoyu 6543210
wulongyuan 6667770
'''

import sys

account_file="/home/chrisz/match.txt"
locked_file="/home/chrisz/locked.txt"

def deny_account(username):
    print("Your user is locked!")
    with open(locked_file,'a') as deny_f:
        deny_f.write('\n'+username)

def main():
    retry_count=0
    retry_limit=3
    while retry_count < retry_limit:
        username = input('\033[32:1m Please input username:\033[0m')
        if len(username)==0:
            print("username should NOT be null,please input again.")
            continue

        with open(locked_file,'r') as lock_f:
            for line in lock_f.readlines():
                if len(line)==0:
                    continue
                if username == line.strip():
                    sys.exit('\033[32:1m user %s locked!\033[0m'%username)

        password=input('\033[32:1m Please input password:\033[0m')
        with open(account_file,'r') as account_f:
            flag=False
            for line in account_f.readlines():
                user,pwd=line.strip().split()
                if username == user and password == pwd:
                    print("success!")
                    flag=True
                    break

        if flag==False:
            if retry_count < 2:
                print("Your username or password is incorrect,please input agian!")
            retry_account+=1
        else:
            print("Welcome user%s come" % username)
            break

    else:
        deny_account(username)

if __name__=='__main__':
    main()