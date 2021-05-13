#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: May 2021
# This program shows the sum of 


def main():

    sum = 0
    loop_counter = 0
    
    integer_str = input("Enter an integer: ")
    try:
        integer = int(integer_str)
        while loop_counter <= integer:
            sum = sum + loop_counter
            loop_counter = loop_counter + 1

        print("The sum of all integers from 1 to {0} is {1}".format(integer, sum))
        
    except Exception:
        print("That is not a valid input!")

if __name__ == "__main__":
    main()
