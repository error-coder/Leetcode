class Solution:
    def plusOne(self, digits):
        result = []
        arr = digits[::-1]
        st = ''
        
        # digits 리스트 요소를 문자로 변환
        for i in digits:
            st += str(i)

        # 1을 더해줌
        st = int(st) + 1

        # 결과 목록에 더해진 숫자를 추가
        for i in str(st):
            result.append(i)

        return result
            
# 숫자를 문자로 변환
# 더한 후 다시 숫자로 변환해서 집어넣음