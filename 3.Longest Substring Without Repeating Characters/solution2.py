class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        string_set = set()
        string_len = len(s)
        result, rightIndex  = 0, -1
        for i in range(string_len):
            # i = -1 情况下
            if i != 0:
                print(s[i - 1])
                string_set.remove(s[i - 1])
            #         执行正常逻辑
            while rightIndex + 1 < string_len and s[rightIndex + 1] not in string_set:
                string_set.add(s[rightIndex + 1])
                rightIndex += 1
                # 第 i 到 rk 个字符是一个极长的无重复字符子串
                result = max(result, rightIndex - i + 1)
        return result

s = Solution();
print(s.lengthOfLongestSubstring("abcb"))

