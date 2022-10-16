class Solution:
    # x는 int, return 값은 bool형
    # 앞뒤가 같은 숫자 -> True(음수형이면 뒤집었을때 -가 맨 뒤로 가서 false)
    def isPalindrome(self, x):
        Pail = str(x)

        if x < 0 :
            return False

        # 연속열을 슬라이스 할 때 시작, 끝을 생략하면 전체 범위를 선택하는데
        # 증감값을 -1로 해주면 뒤에서 앞으로 가져와 뒤집는것과 같음
        if Pail == Pail[::-1]:
            return True
        else:
            return False

        # 대칭수 판별 가장 빠른 방법 -> s[::-1] == s