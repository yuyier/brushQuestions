class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]
        # pre_index, last_index = 0, len(s) - 1
        # result = True
        # while pre_index <= last_index:
        #     pre_str, last_str = s[pre_index].lower(), s[last_index].lower()
        #     if not pre_str.isdigit() and (pre_str < 'a' or pre_str > 'z'):
        #         pre_index += 1
        #         continue
        #
        #     if not last_str.isdigit() and (last_str < 'a' or last_str > 'z'):
        #         last_index -= 1
        #         continue
        #
        #     if pre_str != last_str:
        #         result = False
        #         break
        #     pre_index,last_index = pre_index+1,last_index-1
        # return result


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    # s = "race a car"
    print(Solution().isPalindrome(s))
