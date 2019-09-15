import math as m

ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", ]
teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
ten = ["", "ten", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def num2text(num):
    text = ""
    
#    if(tenthoud(num) != 0):
#        if((m.floor(num/10000) % 10) != 1):
#            text = text + ten[tenthoud(num)] + " "
#    if(thoud(num) != 0):
#        if((m.floor(num/1000) % 10) != 1):
#            text = text + ones[thoud(num)] + " thousand "
#        else:
#            text = text + teens[thoud(num)] + " thousand "
    if((num / 1000000000) > 1):
        text = text + printhun(m.floor(num/1000000000)) + " billion "
    if((num / 1000000) > 1):
        text = text + printhun(m.floor(num/1000000)) + " million "
    if((num / 1000) > 1):
        text = text + printhun(m.floor(num/1000)) + " thousand "
    text = text + printhun(num)
    
    return(text)

def printhun(num):
    text = ""
    if(hund(num) != 0):
        text = text + ones[hund(num)] + " hundered and "
    if(tend(num) != 0):
        if((m.floor(num/10) % 10) !=  1):
            text = text + ten[tend(num)] + " "
    if(unitd(num) != 0):
        if((m.floor(num/10) % 10) != 1):
            text = text + ones[unitd(num)] + " "
        else:
            text = text + teens[unitd(num)]
    
    return(text)

def unitd(num):
    return(num % 10)
    
def tend(num):
    return(m.floor(num/10) % 10)
    
def hund(num):
    return(m.floor(num/100) % 10)
    
def thoud(num):
    return(m.floor(num/1000) % 10)

def tenthoud(num):
    return(m.floor(num/10000) % 10)