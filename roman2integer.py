"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. 
Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""
class Roman_Numeral_Sys(object):
    def romanToInt(self, s):
        # create a dictionary to store the roman numerals and their values
        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,'M':1000}

        
        # initialize total to 0 to store the running sum of the converted Roman numeral
        total = 0
        # to keep track of consecutive occurences of the same Roman numeral
        count = 1
        len_string = len(s)

        # iterate through the input Roman numeral string from left to right [len(0) to ...]
        for i in range(len_string):

            # check if there is any invalid input
            if s[i] not in roman_dict:
                raise ValueError("Invalid Roman Numeral")
            
            # check if there are more than 3 consecutive occurences of the same Roman numeral
            if i < len_string - 1 and s[i] == s[i+1]:
                count += 1
                if count > 3:
                    raise ValueError("Invalid Roman Numeral")
            else:
                count = 1
            
            # Special Case Error Capture: check if there are two "V"
            if i < len_string - 1 and s[i] == 'V' and s[i+1] == 'V':
                raise ValueError("Invalid Roman Numeral")

            # check if any invalid combinations of Roman numerals are present
            if i < len_string - 1 and roman_dict[s[i]] < roman_dict[s[i+1]]:
                if s[i] not in ['I', 'X', 'C']:
                    raise ValueError("Invalid Roman Numeral")
                if roman_dict[s[i+1]] > roman_dict[s[i]] * 10:
                    raise ValueError("Invalid Roman Numeral")
                
            # compare the current Roman numeral to the next one
            # if the current Roman numeral is less than the next one, subtraction is required
            if i < len_string - 1 and roman_dict[s[i]] < roman_dict[s[i+1]]:
                total -= roman_dict[s[i]]
            else:
                total += roman_dict[s[i]] # else add the value of the current Roman numeral to the total
        return total
    
    def intToRoman(self, num):
        # create a dictionary to store the roman numerals and their values
        roman_dict = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL':40, 'L': 50, 'XC': 90, 'C': 100, 'CD':400, 'D': 500, 'CM': 900, 'M': 1000}

        index = 12
        roman_num = ""
        
        # check if num is within the range [1, 3999]
        if num < 1 or num > 3999:
            raise ValueError("Invalid Input. Enter a valid number from 1 to 3,999")
        while num:
            # extract the largest base value from the input integer
            div = num // list(roman_dict.values())[index]
            # remainder
            remainder = num % list(roman_dict.values())[index]
            # if the quotient is not 0, add the corresponding Roman numeral to the output string
            if div != 0:
                roman_num += div * list(roman_dict.keys())[index]
                div -= 1
            # update the input integer
            num = remainder
            # update the index to the next largest base value
            index -= 1

        return roman_num

    def welcomePage(self):
        print("Welcome to Roman Numeral Converter!")
        print("This program allows you to convert between Roman numerals and integers.")
        print("Please select the mode of operation:")
        print("1: Roman to Integer")
        print("2: Integer to Roman")
        print()

    def processModes(self):
        self.welcomePage()
        mode = input("Enter the mode(1 or 2): ")

        if mode == '1':
            try:
                usr_input = input("Enter a Roman numeral: ").upper()
                result = Roman_Numeral_Sys().romanToInt(usr_input)
                print("Integer value: ", result)
            except ValueError as e:
                print("Error:", e)
        elif mode == '2':
            try:
                usr_input = int(input("Enter an integer: "))
                result = Roman_Numeral_Sys().intToRoman(usr_input)
                print("Roman numeral: ", result)
            except ValueError as e:
                print("Error:", e)
        else:
            print("Invalid input. Enter '1' or '2'.")

if __name__ == "__main__":

    while True:
        romanNumeralSys = Roman_Numeral_Sys()
        romanNumeralSys.processModes()
        print()
        exit_command = input("Enter 'q' to exit or any other key to continue: ")
        if exit_command == 'q':
            break

        
        