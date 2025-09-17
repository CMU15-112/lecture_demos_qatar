def longestCommonSubstring(s1, s2):
    longest_seen = ""
    if s1 == s2:
        return s1
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    for i in range(len(s1)):
        for j in range(1, len(s1)):
            if s1[i:j] in s2:
                if len(longest_seen) < len(s1[i:j])  :
                    longest_seen = s1[i:j]
                elif len(longest_seen) == len(s1[i:j]) and s1[i:j] < longest_seen:
                    longest_seen = s1[i:j]
                else:
                    continue
    return longest_seen
                



assert(longestCommonSubstring('abcdef', 'abqrcdest')) == 'cde'
assert(longestCommonSubstring('abcdef', 'ghi')) == ''
assert(longestCommonSubstring('abcABC', 'zzabZZAB')) == 'AB'
assert(longestCommonSubstring('trkmqeadhKMQOghKMQyrtKM', 'sdvaddsrKMQadKMkmqKMQOa')) == 'KMQO'
