class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # rstrip은 오른쪽 공백을 지우는 메소드
        # 오른쪽 단어만 공백으로 구분한 다음 오른쪽에 있는 공백을 지워줌
        words = s.rstrip().split(' ')

        # 오른쪽의 단어 길이만 반환하면 되니 오른쪽 단어 길이가 0이면 0
        if len(words) == 0:
            return 0
        else:
            return len(words[-1])
