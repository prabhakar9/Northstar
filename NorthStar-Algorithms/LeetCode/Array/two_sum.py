def lengthOfLongestSubstring(s):
    char_set = [-1 for _ in range(128)]
    longest = 0
    l = 0
    ptr = -1
    for i in range(len(s)):
        ord_ch = ord(s[i])
        if char_set[ord_ch] == -1 or char_set[ord_ch] < ptr:
            l += 1
            char_set[ord_ch] = i
        else:
            longest = max(longest, l)
            l = i - char_set[ord_ch]
            ptr = char_set[ord_ch] + 1
            char_set[ord_ch] = i
    longest = max(longest, l)
    return longest


if __name__ == "__main__":
    s = " "
    out_s = lengthOfLongestSubstring(s)
    print(out_s)
