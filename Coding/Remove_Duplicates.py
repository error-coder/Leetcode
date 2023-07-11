class Solution:
    def searchInsert(self, nums, target):
        # target이 주어진 수열 중 어디에 들어가는지 찾는 문제
        # left : 배열의 첫번째 인덱스, right : 배열의 마지막 인덱스
        # mid : 배열의 중간 인덱스, target : 찾고자 하는 값
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            # target이 배열의 중간 인덱스보다 크다면 오른쪽 배열을 대상으로 탐색
            # 가운데 기준 오른쪽 배열 구간으로 이동
            if nums[mid] < target:
                left = mid + 1
            # target이 배열의 중간 인덱스보다 작다면 왼쪽 배열을 대상으로 탐색
            # 가운데 기준 왼쪽 배열 구간으로 이동
            if nums[mid] > target:
                right = mid - 1

        return left
            
# bisect라는 python 라이브러리를 이용해 간단하게 풀이 가능함