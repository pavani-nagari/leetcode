class Solution {
    public int removeDuplicates(int[] nums) {
        int i = 1;
        int j=0;
        int no_rep = 1;
        boolean printed = false;
        boolean visited = false;
        if(nums.length<=1)
            return 1;
        if(nums[0]!=nums[1]){
            nums[j] = nums[0];
            j++;
        }
        while(i<nums.length ){
            if(nums[i] == nums[i-1]){
                no_rep ++;
            }
            else{
                no_rep = 1;
                visited = false;
                printed = true;
                nums[j] = nums[i];
                j++;
            }
            if(no_rep>=2 && !visited){
                visited = true;
                if(printed){
                    nums[j] = nums[i];
                    j++;
                }
                else{
                    nums[j] = nums[i];
                    nums[j+1] = nums[i];
                    j = j+2;
                }
            }
            i++;
        }
        return j;
        
    }
}