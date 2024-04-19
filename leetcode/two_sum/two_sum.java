class Solution {
        public int[] twoSum(int[] nums, int target) {
                HashMap<Integer, Integer> restAndValIndex = new HashMap<Integer, Integer>();
                
                for( int i = 0; i < nums.length; i++) {
                        int val = nums[i];
                        if (restAndValIndex.containsKey(val))
                                return new int[] {i, restAndValIndex.get(val)};
                        restAndValIndex.put(target - val, i);
                }
                return new int[] {};
        }
}
