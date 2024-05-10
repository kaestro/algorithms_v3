// https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/description/
package Week_2nd

import "math"

func minStartValue(nums []int) int {
	minValue := math.MaxInt32
	sum := 0

	for _, num := range nums {
		sum += num
		if sum < minValue {
			minValue = sum
		}
	}

	ans := -minValue + 1
	if ans <= 0 {
		return 1
	}

	return ans
}
