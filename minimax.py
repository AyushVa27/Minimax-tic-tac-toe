class Solution:
   def PredictTheWinner(self, nums):
       # minMax -- recursion with memoization
       n = len(nums)
       if n == 1 or n % 2 == 0:
           return True
   
       self.dp = [0 for _ in range(n * n)]
       return self.checkWin(nums, 0, n-1) >= 0
  
   def checkWin(self, nums, left, right):
       if left >= right:
           return nums[left]
      
       k = left * len(nums) + right
       if self.dp[k] > 0:
           return self.dp[k]
      
       self.dp[k] = max(nums[left] - self.checkWin(nums, left + 1, right), nums[right] - self.checkWin(nums, left, right - 1))
       return self.dp[k]

a = Solution()
print(a.PredictTheWinner([1,5,2,3,7,223,8,9,12,100]))
#prints true if player 1 is the winner