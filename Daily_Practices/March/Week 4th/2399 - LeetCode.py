# https://leetcode.com/problems/check-distances-between-same-letters/description/

from typing import List

class Solution:
    def checkDistances(self, input_str: str, distance_list: List[int]) -> bool:

        char_distance_dict = {}
        char_last_idx_dict = {chr(i + ord('a')) : -1 for i in range(26)}
        for i, distance in enumerate(distance_list):
            char_distance_dict[chr(i + ord('a'))] = distance
        
        for i, char in enumerate(input_str):
            if char_last_idx_dict[char] == -1:
                char_last_idx_dict[char] = i
            else:
                distance = i - char_last_idx_dict[char] - 1
                if distance != char_distance_dict[char]:
                    return False

        return True


if __name__ == "__main__":
    sol = Solution()
    input_str = "abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzza"
    distance = [49,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    sol.checkDistances(input_str, distance)