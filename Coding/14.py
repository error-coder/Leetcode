class Solution:
    def longestCommonPrefix(self, strs):
        string = ''

        # *연산자는 자바스크립트 스프레드 연산자와 역할이 같음
        # 스프레드 연산자는 배열, 객체를 펼칠 수 있음
        # 기존의 것을 건들이지 않고 새로운 객체를 만드는 것 -> spread(...)
        for elem in zip(*strs):
            if len(set(elem)) > 1:
                return string
            
            string += elem[0]

        return string
