class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		length = 1
		if len(s) == 0 or not s:
			return 0
		if len(s) == 1:
			return 1
		for i in range(len(s)):
			j = i + length
			while j < len(s):
				temps = self.isRepeatString(s[i:j + 1])
				temple = j - i + 1
				if temps == 1 and length < temple:
					length = temple
				print(i, j, s[i:j + 1], temps)
				j += 1

		return length

	def isRepeatString(self, s: str) -> bool:
		hash = {}
		for i in range(len(s)):
			if s[i] in hash:
				return False
			else:
				hash[s[i]] = True
		return True


s = Solution();
