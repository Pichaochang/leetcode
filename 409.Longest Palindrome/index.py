class Solution:
  def expandCenter(self, str, left, right):
    while left >=0 and right < len(str) and str[left] == str[right]:
      left-=1
      right+=1
    return left + 1, right - 1
      
  def longestPalindrome(self, s: str) -> str:
    start, end = 0, 0
    for i in range(len(s)):
      # 首先 要考虑2种情况 1.中心字母没超过1/2  2.中心字母超过1/2 
      # 定义left right
      left1, right1 = self.expandCenter(s, i, i)
      left2, right2 = self.expandCenter(s, i, i + 1)
      if right1 - left1 > end - start:
        start, end = left1, right1
      if right2 - left2  > end - start:
        start, end = left2, right2
    print(start, end)
    return s[start:end + 1]
        
    
          
s = Solution()
count = s.longestPalindrome("babad")
print(count)