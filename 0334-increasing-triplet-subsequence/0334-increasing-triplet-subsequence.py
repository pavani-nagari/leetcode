class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        no_one, no_two = inf, inf
        
        for third in nums:
            
            if no_two < third: 
                return True
            if third <= no_one: 
                no_one= third    
            else:  
                no_two = third 
                
        return  False
    
            
                    
        