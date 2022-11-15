'''
이진 문자열 배열이 주어짐
bank[i] : 0,1로 구성된 i번째 행
0 : 비어있음 / 1 : 보안 장치가 있음

두 보안장치 사이의 레이저 빔이 존재할 조건
1. 두 보안 장치는 서로 다른 두 행(r1, r2)에 존재 (r1 < r2)
2. r1 < i < r2를 만족하는 i행에는 보안장치가 없음

총 레이저 빔 수 반환
'''

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result = temp = 0
        for i in range(len(bank)):
            cnt = bank[i].count('1')
            if cnt != 0:
                result += cnt * temp
                temp = cnt
        return result