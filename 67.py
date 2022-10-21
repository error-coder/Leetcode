class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''

        a = int(a, 2)
        b = int(b, 2)

        # 접두어 제외하기 -> 'b'
        return format(a + b, 'b')

# ex ) a = "11", b = "1" - 2진수
# a = 11은 1과 0, 1은 0이므로 이어 붙이면 100이 나옴
# 2진수 변환은 bin, 10진수 변환은 int