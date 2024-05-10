// https://leetcode.com/problems/find-words-containing-character/description/
package Week_2nd

import "strings"

func findWordsContaining(words []string, x byte) []int {
	ans := []int{}
	for idx, word := range words {
		if strings.Contains(word, string(x)) {
			ans = append(ans, idx)
		}
	}
	return ans
}
