class Solution {
    public String convertToTitle(int columnNumber) {
        String ans="";
        int quo = columnNumber;
        while(quo >26){
            int rem = quo%26 ==0 ? 26 : quo%26;
            if(quo%26==0){
                quo = quo/26 -1;
            }
            else{
                quo/=26;
            }
            ans = Character.toString((char)(64+rem)) + ans;
            System.out.println(rem);
        }
        System.out.println(quo);
        ans = Character.toString((char)(64+quo))+ans;
        return ans;
        
    }
}