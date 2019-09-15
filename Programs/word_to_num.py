import math

def calculate(user_input, and_val = 0):
    if user_input == 0:
        return "zero"
    
    ones_place = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine "]
    teens = ["ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
    tens_place = ["twenty ", "thirty ", "fourty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]
    hundreds_place = ["", "one hundred ", "two hundred ", "three hundred ", "four hundred ", "five hundred ", "six hundred ", "seven hundred ", "eight hundred ", "nine hundred "]
    
    and_ones_place = ["", "and one ", "and two ", "and three ", "and four ", "and five ", "and six ", "and seven ", "and eight ", "and nine "]
    and_teens = ["and ten ", "and eleven ", "and twelve ", "and thirteen ", "and fourteen ", "and fifteen ", "and sixteen ", "and seventeen ", "and eighteen ", "and nineteen "]
    and_tens_place = ["and twenty ", "and thirty ", "and fourty ", "and fifty ", "and sixty ", "and seventy ", "and eighty ", "and ninety "]
    
    and_bit = and_val
    num_length = len(str(user_input))
    if num_length > 2:
        and_bit = 1
    
    def digit_1(d_1):
        return ones_place[d_1]
    
    def digit_2(and_bit, d_1, d_2):
        if and_bit == 0:
            if d_2 == 0:
                return ones_place[d_1]
            if d_2 == 10:
                return teens[d_1]
            else:
                return tens_place[math.floor(d_2 / 10)- 2]
        if and_bit == 1:
            if d_2 == 0:
                return and_ones_place[d_1]
            if d_2 == 10:
                return and_teens[d_1]
            else:
                return and_tens_place[math.floor(d_2 / 10) - 2]
            
    def digit_3(d_3):
        return hundreds_place[math.floor(d_3 / 100)]

    mod_num_1 = user_input % 10
    digit_1_num = digit_1(mod_num_1)
    user_input -= mod_num_1
    
    mod_num_2 = user_input % 100
    digit_2_num = digit_2(and_bit, mod_num_1, mod_num_2)
    user_input -= mod_num_2
    
    mod_num_3 = user_input % 1000
    digit_3_num = digit_3(mod_num_3)
    user_input -= mod_num_3
    
    if mod_num_2 == 10 or mod_num_2 == 0:
        return digit_3_num + digit_2_num
    else:
        return digit_3_num + digit_2_num + digit_1_num
    
def main():
    hundred_prepend = [" ", "thousand ", "million ", "billion ", "trillion ", "quadrillion ",
                       "quintrillion ", "sextillion ", "septillion ", "octillion ", "nonillion ", "decillion ",
                       "undecillion ", "duodecillion ", "tredecillion ", "quattuordecillion ", "quindecillion ", "sexdecillion ",
                       "septemdecillion ", "octodecillion ", "novemdecillion ", "vigintillion ", "unvigintillion ", "duovigintillion ",
                       "trevigintillion ", "quattuorvigintillion ", "quinvigintillion ", "sexvigintillion ", "septvigintillion", "octovigintillion ",
                       "nonvigintillion ", "trigintillion ", "untrigintillion ", "duotrigintillion ", "googol "]
    num_to_word = " "
    user_input = round(eval(input("Enter a number:")))
    user_input_str = str(user_input)
    input_r = user_input_str[::-1]
    while user_input != 0:
        num_digits = len(str(user_input))
        complete_hundreds = math.floor(num_digits / 3)
        partial_hundreds = 0
        if math.floor(num_digits % 3) > 0:
            partial_hundreds = 1
        total_hundreds = complete_hundreds + partial_hundreds
        
        for i in range(total_hundreds):
            if i != 0 and total_hundreds > 1:
                current_hundred = calculate(int((input_r[0 + (3 * i) : 3 + (3 * i)])[::-1]))
            else:
                current_hundred = calculate(int((input_r[0 + (3 * i) : 3 + (3 * i)])[::-1]), and_val = 1)
            if current_hundred != "zero":
                num_to_word = current_hundred + hundred_prepend[i] + num_to_word
            
        print("Word to number: " + num_to_word)
        num_to_word = " "
        user_input = round(eval(input("Enter a number:")))
        user_input_str = str(user_input)
        input_r = user_input_str[::-1]
    
main()
