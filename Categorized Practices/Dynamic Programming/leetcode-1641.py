# https://leetcode.com/problems/count-sorted-vowel-strings/description/

class Solution:
    def countVowelStrings(self, n: int) -> int:
        # Initialize a 2D array to store the count of strings of length i ending with each vowel
        dp = [[0] * 5 for _ in range(n+1)]

        # Initialize base case
        for i in range(5):
            dp[1][i] = 1
        
        # Fill in the DP table
        for i in range(2, n + 1):
            for j in range(5):
                # The count of strings of length i ending with vowel j is the sum of counts of strings
                # of length i - 1 ending with vowel k for k <= j
                dp[i][j] = sum(dp[i - 1][k] for k in range(j + 1))
        
        # The answer is the sum of counts of strings of length n ending with each vowel
        return sum(dp[n])