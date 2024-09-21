class Solution(object):
    def minCostToMoveChips(self, position):
        cnt1 = cnt2 = 0
        
        for i in range(len(position)):
            if position[i] % 2 == 0:
                cnt1 += 1
            else:
                cnt2 += 1
                
        if cnt1 > cnt2:
            return cnt2
        else:
            return cnt1