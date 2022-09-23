class Solution:
	def concatenatedBinary(self, n: int) -> int:
		ans = 0
		curr = 0
		val = 1
		for i in range(1,n+1):
			if i == val:
				mul = 2<<curr
				curr+=1
				val<<=1

			ans = (ans*mul + i)%(10**9 + 7)
		return ans