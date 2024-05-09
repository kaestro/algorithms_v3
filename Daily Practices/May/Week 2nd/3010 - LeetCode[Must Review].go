package main

import (
	"math"
)

func minimumCost(nums []int) int {
	n := len(nums)
	if n < 3 {
		return 0
	}

	minCost := math.MaxInt32
	for i := 1; i < n-1; i++ {
		for j := i + 1; j < n; j++ {
			cost := nums[0] + nums[i] + nums[j]
			if cost < minCost {
				minCost = cost
			}
		}
	}
	return minCost
}
