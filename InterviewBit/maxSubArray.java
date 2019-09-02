public class Solution {
    // DO NOT MODIFY THE LIST. IT IS READ ONLY
    public int maxSubArray(final List<Integer> A) {
        int max=-Integer.MAX_VALUE;
        int temp=0;
        for (int i=0;i<A.size();i++){
            temp=temp+A.get(i);
            if (temp>max){
                max=temp;
            }
            if (temp<0){
                temp=0;
            }
        }
        return max;
    }
}
