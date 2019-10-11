#!/usr/bin/env python
import math
#ref : https://www.programiz.com/python-programming/modules/math
#https://stackoverflow.com/questions/8982163/how-do-i-tell-python-to-convert-integers-into-words
#I used the above reference to look at for some ideas and then came out with the
#below logic myself based on trying to divide the digitplace value in (base 10 power x) way
#so as to find out if a given digit is in 10s place, 100splace, 1000s place or millionth place
#veena.s.rao@oracle.com

#Takes a number and returns words as read out
def num2eng(num):
  ones = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
  tens = ["units","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
  if num < 0:
    return ("Only positive numbers please")
  if num < 20:
    return (ones[num] + " ")
  if num < 100:
    return (tens[(num//10)]+ " " + ones[(num%10)] + " ")
  if num < 1000: 
    words = num2eng(num//100) + "hundred " + num2eng(num%100) + " "
    return words
  if num < pow(10,6):
    words = num2eng(num//1000) + "thousand " + num2eng(num%1000) + " "
    return words
  if num < pow(10,9):
    words = num2eng(num//pow(10,6)) + "million " + num2eng(num%pow(10,6)) + " "
    return words
  if num < pow(10,12):
    words = num2eng(num//pow(10,9)) + "billion " + num2eng(num%pow(10,9)) + " "
    return words
  if num < pow(10,15):
    words = num2eng(num//pow(10,12)) + "trillion " + num2eng(num%pow(10,12)) + " "
    return words
  else:
    return "Too big"
  
def main():
  while (1): 
    num = int (input("Enter a Number: "))
    print(num)
    print (num2eng(num))

main()
