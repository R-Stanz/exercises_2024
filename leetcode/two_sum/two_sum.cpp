class Solution {
public:
        vector<int> twoSum(vector<int>& nums, int target) {
                unordered_map<int,int> rest_and_val_index;    
                
                for (int i = 0; i < nums.size(); i++) {
                        int val = nums.at(i);
                        if (rest_and_val_index.contains(val))
                                return vector<int> {i, rest_and_val_index[val]};       
                        rest_and_val_index[target - val] = i;
                }       
                return vector<int>();
        }
};
