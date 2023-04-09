class Solution:
    def countAndSay(self, n: int) -> str:
        num = "1"
        for _ in range(1, n):
            num = self.say(num)
        return str(num)

    def say(self, n: str) -> str:
        output_str = ""
        current_char = n[0]
        current_num = 0
        for char in n:
            if char == current_char:
                current_num += 1
            else:
                output_str += str(current_num) + current_char
                current_char = char
                current_num = 1
        output_str += str(current_num) + current_char
        return output_str
