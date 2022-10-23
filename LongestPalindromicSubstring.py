class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_dash = '|' + '|'.join(list(s)) + '|'
        palindrome_radii = []


        center = 0
        while center < len(s_dash):
            r = 0
            while center - (r + 1) >= 0 and center + (r + 1) < len(s_dash) and s_dash[center-(r + 1)] == s_dash[center+(r + 1)]:
                r += 1
            palindrome_radii.append(r)
            center += 1
        
        radius = max(palindrome_radii)
        center = palindrome_radii.index(radius)
        longest_in_s_dash = s_dash[center-radius + 1: center+radius]
        longest_in_s = longest_in_s_dash.replace("|", "")
        return longest_in_s

