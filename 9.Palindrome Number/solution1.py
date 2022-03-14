class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x > pow(2, 31) - 1 or x < 0 or (x != 0 and x % 10 == 0 ):
            return False
        right, left = 0, x
        while right <= left:
            right = right * 10 + left % 10
            left = int(left / 10)
            if left == right or (right * 10 + left % 10 ) == left :
                return True
        return False
s = Solution();
print(s.isPalindrome(0))