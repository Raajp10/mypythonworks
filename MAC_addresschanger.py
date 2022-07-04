#! /usr/bin/eny python 
 

import subprocess
import optparse
import random
import re
import time

def get_args():
    #import optparse and create OptionalParser's object
    parser = optparse.OptionParser()
    #adding optional arguments using parser.add_option() and give dest to the variable name
    parser.add_option("-i","--interface",dest="interface",help="interface use to change mac address name")
    parser.add_option("-s","--select",dest="select",help="manual for y otherwise use n")
    parser.add_option("-m","--manual",dest="m_addr",help="Enter mac address manually  after selecting select y then enter mac address manually like 11:22:33:44:55:66 ") 
    parser.add_option("-t","--time",dest="timer",help="Enter the next time for you want change mac address by default it changes after 60 seconds")
    parser.add_option("-T","--endtime",dest="endtime",help="Stop the changing after T time")

    #provide the users options to object.parse_args()
    [options,arguments]=parser.parse_args()

    if not options.interface:
        #if interface is not specified
        parser.error("interface is must be specified for knowing more about it use => --help")

    elif not options.select:
        #if options is not specified
        parser.error("option is must be required for create manual mac or auto created and for knowing more about it use =>--help")

    return options

def mac_address(interface,select,m_addr):
    #subprocess.call run any program until it can't completed
    subprocess.call(["sudo","ifconfig", interface, "down"]) 
    
    #ask user to add manually or auto created MAC address
    if(select=="y"):
        subprocess.call(["sudo","ifconfig", interface,"hw","ether", m_addr])
    else:
        x=[]
        #create auto MAC address by using random.randint()
        for z in range(12):
            x.append(str(random.randint(0,9)))
        y=x[0]+x[1]+":"+x[2]+x[3]+":"+x[4]+x[5]+":"+x[6]+x[7]+":"+x[8]+x[9]+":"+x[10]+x[11]
        print("New auto generate MAC address is = "+y) 
        subprocess.call(["sudo","ifconfig", interface,"hw","ether", y])

    subprocess.call(["sudo","ifconfig", interface, "up"])

def man_time(timer=60):
    return time.sleep(timer)     

def current_mac(interface):
    #subprocess.check_output() store the output message
    msg=subprocess.check_output(["sudo","ifconfig",interface])
    
    # for using regit and import re module we can search for mac addresses using re.search
    if re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(msg)): #\w stands for alphanumeric values
        return re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(msg)).group(0) #return 0 number element
    else:
        return "No MAC address found"


while(True):
    #create parser objects and their requirements by get_args() function
    options= get_args()
    print("Your current MAC is : "+current_mac(options.interface))
    
    #change MAC address with mac_address
    mac_address(options.interface, options.select, options.m_addr)
    print("Now, Your current MAC is : "+current_mac(options.interface))

    if not options.timer:
        man_time(60)
    else:
        man_time(int(options.timer))
