class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(' : ')', '[' : ']', '{' : '}'}
        
        for elem in s:
            if elem in brackets:
                stack.append(elem)
            else:
                # 스택이 비었을 경우
                if not stack:
                    return False
                else:
                    # 스택의 마지막 들어가는 값이 짝이 맞을 경우
                    if elem == brackets[stack[-1]]:
                        stack.pop()
                    # 나머지 경우는 다 맞지 않기 때문에 False 반환
                    else:
                        return False

        # 남아 있는 연산자가 있고 짝이 맞는것이 없기 때문에 False
        if stack:
            return False
        else:
            return True


        
# 스택에 ([{이 먼저 쌓인뒤 )]}이 스택에 쌓여야 True
# 스택은 후입선출
# 짝이 맞을경우 pop 해주고 True 값을 반환