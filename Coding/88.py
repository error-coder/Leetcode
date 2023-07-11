class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # del : 인덱스를 삭제함
        # m: -> nums1의 길이가 m이므로 nums1의 인덱스 길이 m 이상부터 삭제함
        del nums1[m:]

        # nums2의 0부터 num2의 길이 n까지 나열한 걸 병합함
        nums1 += nums2[0:n]

        # 정렬시켜줌
        nums1.sort()