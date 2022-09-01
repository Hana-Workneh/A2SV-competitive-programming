class Solution:
	def convert(self, s: str, numRows: int) -> str:
		if numRows<2:
			return s
		lst = ['']*numRows
		step = 1
		index = 0
		for i in s:
			if index == numRows:
				step = -1
				index -= 2
			if index == -1:
				step = 1
				index +=2
			lst[index] = lst[index] + i
			index += step
		return ''.join(lst)