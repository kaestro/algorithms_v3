# https://leetcode.com/problems/number-of-days-between-two-dates/description/

from datetime import datetime

# date의 format은 "YYYY-MM-DD"이다.
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date_format = "%Y-%m-%d"
        a = datetime.strptime(date1, date_format)
        b = datetime.strptime(date2, date_format)
        return abs((a-b).days)