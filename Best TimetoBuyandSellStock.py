class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0  # Initialize the left and right pointers
        maxP = 0  # Initialize the maximum profit
        
        while r < len(prices):
            if prices[r] > prices[l]:
                # If the price at the right pointer is higher than the price at the left pointer,
                # calculate the profit and update maxP with the maximum profit encountered so far.
                maxP = max(prices[r] - prices[l], maxP)
            else:
                l = r  # If the price at the right pointer is not higher, set the left pointer to the right pointer.
            
            r += 1  # Move the right pointer to the next day
            
        return maxP  # Return the maximum profit
