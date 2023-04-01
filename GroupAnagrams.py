class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer_dict = {}
        for string in strs:
            if ''.join(sorted(list(string))) in answer_dict:
                answer_dict[''.join(sorted(list(string)))].append(string)
            else:
                answer_dict[''.join(sorted(list(string)))] = [string]
        answer = [answer_dict[key] for key in answer_dict]
        return answer
