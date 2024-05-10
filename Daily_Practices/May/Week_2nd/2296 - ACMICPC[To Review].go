package Week_2nd

import (
	"fmt"
	"sort"
)

type Building struct {
	x     int
	y     int
	price int
}

func Main2296() {
	n, buildings := GetBuildingInput()

	ans := CalculateMaxProfit(n, buildings)

	fmt.Println(ans)
}

func GetBuildingInput() (int, []Building) {
	var n int
	fmt.Scan(&n)

	buildings := make([]Building, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&buildings[i].x, &buildings[i].y, &buildings[i].price)
	}

	return n, buildings
}

func CalculateMaxProfit(n int, buildings []Building) int {
	buildings = reorderBuildings(buildings)

	dp := initializeDp(n, buildings)
	ans := 0
	for i := 0; i < n; i++ {
		for j := 0; j < i; j++ {
			if buildings[j].y < buildings[i].y {
				dp[i][0] = max(dp[i][0], dp[j][0]+buildings[i].price)
			} else if buildings[j].y > buildings[i].y {
				dp[i][1] = max(dp[i][1], dp[j][1]+buildings[i].price)
			}
		}
		ans = max(ans, dp[i][0], dp[i][1])
	}

	return ans
}

func initializeDp(n int, buildings []Building) [][]int {
	dp := getNby2Slice(n)
	for i := 0; i < n; i++ {
		dp[i][0] = buildings[i].price
		dp[i][1] = buildings[i].price
	}

	return dp
}

func reorderBuildings(buildings []Building) []Building {
	sort.Slice(buildings, func(i, j int) bool {
		return buildings[i].x < buildings[j].x
	})

	return buildings
}

func getNby2Slice(n int) [][]int {
	dp := make([][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]int, 2)
	}

	return dp
}

func max(nums ...int) int {
	maxVal := nums[0]
	for _, num := range nums {
		if num > maxVal {
			maxVal = num
		}
	}

	return maxVal
}
