// https://www.acmicpc.net/problem/2805
package Week_2nd

import (
	"fmt"
	"sort"
)

func Main2805() int {
	numTrees, targetTreeLength, treeHeights, maxHeight := GetInputTrees()

	ans := CalculateMaxCuttingLength(numTrees, targetTreeLength, maxHeight, treeHeights)
	return ans
}

func GetInputTrees() (int, int, []int, int) {
	var numTrees, neededTreeLength int
	fmt.Scan(&numTrees, &neededTreeLength)

	treeHeights := make([]int, numTrees)
	maxHeight := 0

	for i := 0; i < numTrees; i++ {
		fmt.Scan(&treeHeights[i])
		if treeHeights[i] > maxHeight {
			maxHeight = treeHeights[i]
		}
	}

	return numTrees, neededTreeLength, treeHeights, maxHeight
}
func CalculateMaxCuttingLength(numTrees, targetTreeLength, maxHeight int, treeHeights []int) int {
	left, right := 0, maxHeight

	sort.Slice(treeHeights, func(i, j int) bool {
		return treeHeights[i] > treeHeights[j]
	})

	for left < right {
		mid := (left + right + 1) / 2
		sum := 0

		for _, height := range treeHeights {
			if height <= mid {
				break
			}
			sum += height - mid

			if sum >= targetTreeLength {
				break
			}
		}

		if sum >= targetTreeLength {
			left = mid
		} else {
			right = mid - 1
		}
	}

	return left
}
