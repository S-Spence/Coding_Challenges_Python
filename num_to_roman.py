class Solution:
    
    def intToRoman(self, num: int) -> str:
        """A function to convert integers to roman numerals"""
        # Rules for translation
        translation = {
            1: "I", 
            4: "IV", 
            5: "V", 
            9: "IX", 
            10: "X", 
            40: "XL", 
            50: "L",
            90: "XC",
            100: "C", 
            400: "CD",
            500: "D", 
            900: "CM",
            1000: "M"
        }
        
        test_divisibility = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ""
        
        """Start with the largest denomination and work down, calcuating how many values
           of each denomination are needed."""
        for i in test_divisibility:
            if num != 0:
                quotient = num//i
                
                if quotient != 0:
                    print(quotient)
                    for j in range(quotient):
                        roman += translation[i]
            num = num % i
        return roman

test = Solution()
print(test.intToRoman(1996))
