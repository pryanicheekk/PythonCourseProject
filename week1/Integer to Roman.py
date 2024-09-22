class Solution(object):
    def intToRoman(self, num):
        while (num != 0):
            answer = ""
            if (num >= 1000):
                answer += "M" * (num // 1000)
                num = num % 1000
            if (num // 100 == 4 or num // 100 == 9):
                if (num // 100 == 4):
                    answer += "CD"
                    num = num % 100
                else:
                    answer += "CM"
                    num = num % 100
            if (num >= 100):
                if (num < 400):
                    answer += "C" * (num // 100)
                    num = num % 100
                else:
                    answer += "D"
                    num -= 500
                    answer += "C" * (num // 100)
                    num = num % 100
            if (num // 10 == 4 or num // 10 == 9):
                if (num // 10 == 4):
                    answer += "XL"
                    num = num % 10
                else:
                    answer += "XC"
                    num = num % 10
            if (num >= 10):
                if (num < 40):
                    answer += "X" * (num // 10)
                    num = num % 10
                else:
                    answer += "L"
                    num -= 50
                    answer += "X" * (num // 10)
                    num = num % 10
            if (num % 10 == 4 or num % 10 == 9):
                if (num % 10 == 4):
                    answer += "IV"
                    num = 0
                else:
                    answer += "IX"
                    num = 0
            if (num % 10 > 0):
                if (num % 10 < 4):
                    answer += "I" * (num)
                    num = 0
                else:
                    answer += "V"
                    num -= 5
                    answer += "I" * (num)
                    num = 0
        return answer
solution = Solution()
print(solution.intToRoman(1994))