#!/usr/bin/env python


from __future__ import print_function
import sys

DEBUG = True

def log(*args, **kwargs):
    """
        for printing all the execution progress messages into stderr
        (and the output results go to stdout)
    """
    if not DEBUG:
        return
    kwargs["file"] = sys.stderr
    print(*args, **kwargs)


input_data = open(sys.argv[1])
filename, _ = sys.argv[1].split(".")
output_data = open(filename + ".out","w")

def solve_one():
    N = int(input_data.readline().rstrip())
    M = int(input_data.readline().rstrip())
    result = [0 for i in range(N)]
    dhash_fl_cus = {i:{} for i in range(N)}
    malted_flavour_prefs = {}
    malted_flavour_customers = {i:[] for i in range(N)}
    customer_prefs = {i:{} for i in range(M)}
    satisfied_customers = {}
    necessarily_malted = {}
    for customer_id in range(M):
        likes = input_data.readline().rstrip().split(' ')
        T = 1
        while T< len(likes):
            flavour = int(likes[T]) -1
            if likes[T+1]=='0':
                # import pdb; pdb.set_trace()
                dhash_fl_cus[flavour][customer_id] = '!'
                customer_prefs[customer_id][flavour] = '$'
            else:
                malted_flavour_prefs[customer_id] = flavour
                malted_flavour_customers[flavour].append(customer_id)
            T +=2

    while True:
        # log("  -- iterated dhash[customer->nonmalted]: ",customer_prefs)
        cur_malted_flavour = None
        # import pdb; pdb.set_trace()
        # looking for the unsatisfied customer that cant be satisfied by available
        # non-malted flavours
        # will have to treat her malted flavour cur_malted_flavour
        # as to be batched
        for customer in customer_prefs.keys():
            # keys in customer prefs store unsatisfied customers
            if len(customer_prefs[customer])==0:
                if customer not in malted_flavour_prefs:
                    return 'IMPOSSIBLE'
                cur_malted_flavour = malted_flavour_prefs[customer]
                break
        if cur_malted_flavour is None:
            break
        result[cur_malted_flavour] = 1

        for satisfied_customer in malted_flavour_customers[cur_malted_flavour]:
            if satisfied_customer not in customer_prefs:
                continue
            del customer_prefs[satisfied_customer]

        # turn off that it matters that other people like the unmalted flavour
        for customer in dhash_fl_cus[cur_malted_flavour].keys():
            if customer not in customer_prefs:
                continue
            del customer_prefs[customer][cur_malted_flavour]
    return " ".join([str(i) for i in result])

num_tests = int(input_data.readline().rstrip())
for i in range(1,num_tests+1):
    output_data.write("Case #%s: %s\n" %(i, solve_one()))




FLAVOURS = ['AROMA', 'BANANA', 'CINNAMON', 'DALE','EPHCALYPTUS', 'FOREST', 'GELLATINE', 'HALE', 'INDIGO', 'JELLYBEAN', 'KITKAT', 'LEMON', 'MNM', 'OREGAM']
def flavour(i):
    level = i/len(FLAVOURS)
    return FLAVOURS[i % len(FLAVOURS)] if level == 0 else FLAVOURS[i % len(FLAVOURS)] + str(level)

CUSTOMERS = ['ALICE', 'BOB', 'CASEY', 'DIANE', 'EMMA', 'FELIX', 'GEORGE', 'HARRY', 'IAN', 'JAY', 'KEVIN', 'LEO']
def customer(i):
    level = i/len(CUSTOMERS)
    return CUSTOMERS[i % len(CUSTOMERS)] if level == 0 else CUSTOMERS[i % len(CUSTOMERS)] + str(level)
