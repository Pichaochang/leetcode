class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		length = 1
		if len(s) == 0 or not s:
			return 0
		if len(s) == 1:
			return 1
		# xzaxog
		for i in range(len(s)):
			j = i
			while j < len(s):
				temps = self.isRepeatString(s[i:j + 1])
				temple = j - i + 1
				if temps == 1 and length < temple:
					length = temple
				print(i, j, s[i:j + 1], temps)
				j += length
				if j >= len(s):
					temps = self.isRepeatString(s[i:len(s)])
					temple = len(s) - i
					if temps == 1 and length < temple:
						length = temple
					break;

		return length

	def isRepeatString(self, s: str) -> bool:
		hash = {}
		for i in range(len(s)):
			if s[i] in hash:
				return False
			else:
				hash[s[i]] = True
		return True
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         # 哈希集合，记录每个字符是否出现过
#         occ = set()
#         n = len(s)
#         # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
#         rk, ans = -1, 0
#         for i in range(n):
#             if i != 0:
#                 # 左指针向右移动一格，移除一个字符
#                 occ.remove(s[i - 1])
#             while rk + 1 < n and s[rk + 1] not in occ:
#                 # 不断地移动右指针
#                 occ.add(s[rk + 1])
#                 rk += 1
#             # 第 i 到 rk 个字符是一个极长的无重复字符子串
#             ans = max(ans, rk - i + 1)
#         return ans

s = Solution();
print(s.lengthOfLongestSubstring("abcb"))
