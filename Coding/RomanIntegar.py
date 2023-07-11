class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {'I' : 1, 'III' : 3, 'IV' : 4 ,'V' : 5, 'X' : 10, 'L' : 50, 
        'XC' : 90 , 'C' : 100, 'D' : 500, 'CM' : 900 ,'M' : 1000}
        result = 0

        for i in range(0, len(s) - 1):
            num = symbols[s[i]]
            secnum = symbols[s[i + 1]]

            if num >= secnum :
                result += num
            else:
                result -= num

        
        return result + symbols[s[-1]]