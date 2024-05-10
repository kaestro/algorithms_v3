// https://leetcode.com/problems/minimum-number-game/description/
package Week_2nd

import "sort"

func numberGame(nums []int) []int {
	sort.Ints(nums)

	ans := make([]int, len(nums))
	for i := 0; i < len(nums); i += 2 {
		ans[i], ans[i+1] = nums[i+1], nums[i]
	}

	return ans
}
