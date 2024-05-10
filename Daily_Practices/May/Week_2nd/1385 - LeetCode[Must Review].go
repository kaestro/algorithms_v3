// https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/
package Week_2nd

import "math"

func FindTheDistanceValue(arr1 []int, arr2 []int, distance int) int {
	pairExists := make(map[int]bool)
	numCount := make(map[int]int)
	for _, num := range arr1 {
		pairExists[num] = false
		numCount[num]++
	}

	for _, num := range arr2 {
		for key := range pairExists {
			if int(math.Abs(float64(num-key))) <= distance {
				pairExists[key] = true
			}
		}
	}

	count := 0
	for key, value := range pairExists {
		if !value {
			count += numCount[key]
		}
	}

	return count
}

func BetterSolution(arr1 []int, arr2 []int, distance int) int {
	count := 0
	for _, num1 := range arr1 {
		for _, num2 := range arr2 {
			if int(math.Abs(float64(num1-num2))) <= distance {
				count++
				break
			}
		}
	}

	return len(arr1) - count
}
