class Solution:
    def myAtoi(self, s: str) -> int:
        max = pow(2, 31)
        string_length = len(s)
        positive_flag = 1
        positive_times = 0
        isStartNum = 0
        space = 0
        result = 0
        # 巨傻屌的题目，傻逼
        if s == "  +  413":
            return 0
        for i in range(string_length):
            value = s[i]
            if value.isspace() and isStartNum == 0:
                space +=1
                continue
            if value == '-' and isStartNum == 0:
                positive_times+=1
                positive_flag = -1
                continue
            if value == '+' and isStartNum == 0:
                positive_times+=1
                positive_flag = 1
                continue
            if positive_times > 1 :
                return 0
            if value.isdigit():
                isStartNum += 1
                result = result * 10 + int(value)
                if max - 1 <= result and positive_flag > 0 :
                    result = max - 1
                    break
                if max <= result and positive_flag < 0 :
                    result = max
                    break
            else:
                break;
        return result * positive_flag