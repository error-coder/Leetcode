class Solution:
    # nums -> List[int], target -> int return -> List[int]
    def twoSum(self, nums, target):
        elem = []

        # target의 값과 배열에 있는 인덱스 위치의 값이 같음, 인덱스 위치를 반환시켜야함
        # target - nums[i]를 해주면 인덱스 값이 나옴
        # ex) target - nums[0] = 9 - 2 = 7
        for i in range(len(nums)):
            if nums[i] in elem:
                return [elem.index(nums[i]), i]

            elem.append(target-nums[i])

    
 
        
