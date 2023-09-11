class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        size_groups = {}
        for person, value in enumerate(groupSizes):
            if value in size_groups:
                size_groups[value].append(person)
            else:
                size_groups[value] = [person]
        groups = []
        for size in size_groups:
            while size_groups[size] != []:
                groups.append(size_groups[size][:size])
                size_groups[size] = size_groups[size][size:]
        return groups
