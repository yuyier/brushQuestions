from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_index = 0
        # nums_set = set()
        nums_list = []
        except_list = []
        nums.sort()
        while nums_index < len(nums) - 2:
            while nums[nums_index] in except_list:
                nums_index += 1
            except_list.append(nums[nums_index])
            second_num_index = nums_index + 1
            except_second_list = []
            while second_num_index < len(nums) - 1:
                while nums[second_num_index] in except_second_list:
                    second_num_index += 1
                the_third_num = 0 - nums[nums_index] - nums[second_num_index]
                if the_third_num in nums[second_num_index + 1:]:
                    # tuple_num = (nums[nums_index], nums[second_num_index], the_third_num)
                    # nums_set.add(tuple_num)
                    list_add = [nums[nums_index], nums[second_num_index], the_third_num]
                    nums_list.append(list_add)
                    except_second_list.append(nums[second_num_index])
                    except_second_list.append(the_third_num)

                second_num_index += 1

            nums_index += 1
        print(len(nums_list))
        return nums_list
