'''Leetcode#1
I copy the rare answer below
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        can_solut = {}
        for i in range(0,len(nums)):
            if nums[i] in can_solut:
                j = can_solut.get(nums[i])
                return [j,i]
            else:            
                b = target - nums[i]
                can_solut.update({b:i})