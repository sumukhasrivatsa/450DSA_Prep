class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy=0
        sell=1
        profit=0
        maxprof=0
        while(buy<sell) and sell<=len(prices)-1:
            prof=prices[sell]-prices[buy]
            if prof>maxprof:
                maxprof=prof
                sell+=1
            elif prof<=0:
                buy=sell
                sell=buy+1
            else:
                sell+=1
        if maxprof==0:
            return 0
        else: return maxprof
            
            
            
        
