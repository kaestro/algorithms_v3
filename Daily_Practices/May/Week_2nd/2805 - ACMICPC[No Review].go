// https://www.acmicpc.net/problem/2805
package Week_2nd

import (
	"bufio"
	"os"
	"sort"
	"strconv"
	"strings"
)

func Main2805() int {
	numTrees, targetTreeLength, treeHeights, maxHeight := GetInputTrees()

	ans := CalculateMaxCuttingLength(numTrees, targetTreeLength, maxHeight, treeHeights)
	return ans
}

func GetInputTrees() (int, int, []int, int) {
	scanner := bufio.NewScanner(os.Stdin)

	numTrees, neededTreeLength := readInitialParams(scanner)
	treeHeights, maxHeight := readTreeHeights(scanner, numTrees)

	return numTrees, neededTreeLength, treeHeights, maxHeight
}

func readInitialParams(scanner *bufio.Scanner) (int, int) {
	scanner.Scan()
	params := strings.Split(scanner.Text(), " ")
	numTrees, _ := strconv.Atoi(params[0])
	neededTreeLength, _ := strconv.Atoi(params[1])
	return numTrees, neededTreeLength
}

func readTreeHeights(scanner *bufio.Scanner, numTrees int) ([]int, int) {
	treeHeights := make([]int, numTrees)
	maxHeight := 0

	scanner.Scan()
	treeHeightsStr := strings.Split(scanner.Text(), " ")
	for i := 0; i < numTrees; i++ {
		if i >= len(treeHeightsStr) {
			treeHeights = append(treeHeights, 0)
		} else {
			treeHeights[i], _ = strconv.Atoi(treeHeightsStr[i])
			if treeHeights[i] > maxHeight {
				maxHeight = treeHeights[i]
			}
		}
	}
	return treeHeights, maxHeight
}

func CalculateMaxCuttingLength(numTrees, targetTreeLength, maxHeight int, treeHeights []int) int {
	left, right := 0, maxHeight

	if isDefaultCase(treeHeights, targetTreeLength) {
		return 0
	}

	sort.Slice(treeHeights, func(i, j int) bool {
		return treeHeights[i] > treeHeights[j]
	})

	for left < right {
		mid := (left + right + 1) / 2
		sum := calculateSum(mid, treeHeights)
		left, right = updateBounds(sum, targetTreeLength, mid, left, right)
	}

	return left
}

func calculateSum(mid int, treeHeights []int) int {
	sum := 0
	for _, height := range treeHeights {
		if height <= mid {
			break
		}
		sum += height - mid
	}
	return sum
}

func updateBounds(sum, targetTreeLength, mid, left, right int) (int, int) {
	if sum >= targetTreeLength {
		return mid, right
	}
	return left, mid - 1
}
func isDefaultCase(treeHeights []int, targetTreeLength int) bool {
	sum := 0
	for _, height := range treeHeights {
		sum += height
	}

	return sum == targetTreeLength
}
