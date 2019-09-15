import math

def calculate(user_input):
    and_bit = 0
    x = user_input
    num_length = len(str(user_input))
    if num_length > 2:
        and_bit = 1
    
    def digit_1(d_1):
        if d_1 == 0:
            return ""
        if d_1 == 1:
            return "one "
        if d_1 == 2:
            return "two "
        if d_1 == 3:
            return "three "
        if d_1 == 4:
            return "four "
        if d_1 == 5:
            return "five "
        if d_1 == 6:
            return "six "
        if d_1 == 7:
            return "seven "
        if d_1 == 8:
            return "eight "
        if d_1 == 9:
            return "nine "
    
    def digit_2(and_bit, d_1, d_2):
        if and_bit == 0:
            if d_2 == 0:
                if d_1 == 0:
                    return " "
                if d_1 == 1:
                    return "one "
                if d_1 == 2:
                    return "two "
                if d_1 == 3:
                    return "three "
                if d_1 == 4:
                    return "four "
                if d_1 == 5:
                    return "five "
                if d_1 == 6:
                    return "six "
                if d_1 == 7:
                    return "seven "
                if d_1 == 8:
                    return "eight "
                if d_1 == 9:
                    return "nine "
            if d_2 == 10:
                if d_1 == 0:
                    return "ten"
                if d_1 == 1:
                    return "eleven"
                if d_1 == 2:
                    return "twelve"
                if d_1 == 3:
                    return "thirteen"
                if d_1 == 4:
                    return "fourteen"
                if d_1 == 5:
                    return "fifteen"
                if d_1 == 6:
                    return "sixteen"
                if d_1 == 7:
                    return "seventeen"
                if d_1 == 8:
                    return "eighteen"
                if d_1 == 9:
                    return "nineteen"
            if d_2 == 20:
                return "twenty "
            if d_2 == 30:
                return "thirty "
            if d_2 == 40:
                return "fourty "
            if d_2 == 50:
                return "fifty "
            if d_2 == 60:
                return "sixty "
            if d_2 == 70:
                return "seventy "
            if d_2 == 80:
                return "eighty "
            if d_2 == 90:
                return "ninety "
        if and_bit == 1:
            if d_2 == 0:
                if d_1 == 0:
                    return ""
                if d_1 == 1:
                    return "and one "
                if d_1 == 2:
                    return "and two "
                if d_1 == 3:
                    return "and three "
                if d_1 == 4:
                    return "and four "
                if d_1 == 5:
                    return "and five "
                if d_1 == 6:
                    return "and six "
                if d_1 == 7:
                    return "and seven "
                if d_1 == 8:
                    return "and eight "
                if d_1 == 9:
                    return "and nine "
            if d_2 == 10:
                if d_1 == 0:
                    return "and ten"
                if d_1 == 0:
                    return "and eleven"
                if d_1 == 0:
                    return "and twelve"
                if d_1 == 0:
                    return "and thirteen"
                if d_1 == 0:
                    return "and fourteen"
                if d_1 == 0:
                    return "and fifteen"
                if d_1 == 0:
                    return "and sixteen"
                if d_1 == 0:
                    return "and seventeen"
                if d_1 == 0:
                    return "and eighteen"
                if d_1 == 0:
                    return "and nineteen"
            if d_2 == 20:
                return "and twenty "
            if d_2 == 30:
                return "and thirty "
            if d_2 == 40:
                return "and fourty "
            if d_2 == 50:
                return "and fifty "
            if d_2 == 60:
                return "and sixty "
            if d_2 == 70:
                return "and seventy "
            if d_2 == 80:
                return "and eighty "
            if d_2 == 90:
                return "and ninety "
            
    def digit_3(d_3):
        if d_3 == 0:
            return ""
        if d_3 == 100:
            return "one hundred "
        if d_3 == 200:
            return "two hundred "
        if d_3 == 300:
            return "three hundred "
        if d_3 == 400:
            return "four hundred "
        if d_3 == 500:
            return "five hundred "
        if d_3 == 600:
            return "six hundred "
        if d_3 == 700:
            return "seven hundred "
        if d_3 == 800:
            return "eight hundred "
        if d_3 == 900:
            return "nine hundred "

    single_digit = 0
    if user_input < 10:
        single_digit = 1
    
    mod_num_1 = user_input % 10
    digit_1_num = digit_1(mod_num_1)
    user_input -= mod_num_1
    
    mod_num_2 = user_input % 100
    digit_2_num = digit_2(and_bit, mod_num_1, mod_num_2)
    user_input -= mod_num_2
    
    mod_num_3 = user_input % 1000
    digit_3_num = digit_3(mod_num_3)
    user_input -= mod_num_3    
    
    
    print("Number to word: " + digit_3_num + digit_2_num + digit_1_num)

def main():
    user_input = round(eval(input("Enter a number:")))
    print("Entered " + str(user_input))
    calculate(user_input)
    
    
main()
