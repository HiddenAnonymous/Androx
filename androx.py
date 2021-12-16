#Ethical hacking course by Hidden Anonymous
#In deed, this is a White, Gray and Black hat #hacking course, knowledge in ond course xD :)

import csv
import sys
from data import hacking
from data import wifi
from data import programming
from data import malwares
from data import cryptography
from data import steganography
from data import cryptos
from data import reverse
from data import social
from data import tricks

def main():
   menu()

#####Welcome banner#####

def menu():
    print("\033[0;32;40m\n#####################")
    print("\033[1;32;40m\n Androx \033[0;32;40m\n By Hidden Anonymous \033[0;31;40m\n { Crack the system } ")
    print("\033[0;32;40m\n#####################")
     
    print()

#####Course subjects#####

    choice = input("""
                      1: Hacking
                      2: Wifi
                      3: Programming
                      4: Malwares
                      5: Cryptography
                      6: Steganography
                      7: Cryptos
                      8: Reverse Engineering
                      9: Social Engineering
                      10: Tricks
                       	
                      Choose subject: """)

#####Logic if user chooses an option#####

    if choice == "1":
        lecc1()
        print(hacking)
        
    elif choice == "2":
        lecc2()
        print(wifi)
        
    elif choice=="3":
        lecc3()
        print(programming)
        
    elif choice == "4":
        lecc4()
        print(malwares)

    elif choice == "5":
        lecc5()
        print(cryptography)

    elif choice=="6":
    	lecc6()
    	print(steganography)

    elif choice == "7":
        lecc7()
        print(cryptos)

    elif choice == "8":
        lecc8()
        print(reverse)

    elif choice=="9":
       lecc9()
       print(social)

    elif choice == "10":
    	lecc10()	   	
    	print(tricks)
    else:
        print("You must only select a number")
        print("Please try again")
        menu()
        
##### Def pass #####

def lecc1():
	pass
def lecc2():
	pass
def lecc3():
    pass
def lecc4():
	pass
def lecc5():
	pass
def lecc6():
	pass
def lecc7():
	pass
def lecc8():
    pass
def lecc9():
	pass
def lecc10():
	pass
	
##### Program initiated #####

main()