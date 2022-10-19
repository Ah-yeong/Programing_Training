# 2020-1-2
# 배낭의 가치를 최대화 하기와 비슷한 백준 병범한 배낭 문제

# 알고리즘
# ① 현재 배낭의 허용 무게보다 넣을 물건의 무게가 더 크다면 넣지 않는다.
# ② 그렇지 않다면, 다음 중 더 나은 가치를 선택하여 넣는다
#    2-1) 현재 넣을 물건의 무게만큼 배낭에서 뺀다. 그리고 현재 물건을 넣는다.
#    2-2) 현재 물건을 넣지않고 이전 배낭 그대로 가지고 간다.
'''
n, k = map(int, input().split())

thing = [[0,0]]
d = [[0]*(k+1) for _ in range(n+1)]

# 줄 마다 (무게, 가치)가 입력됨
for i in range(n):
    thing.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = thing[i][0]
        v = thing[i][1]

        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

print(d[n][k])
'''
# 특정 문자의 개수 세기 2020-1-1
# 재귀함수로 풀기
'''
def count_0(idx, arr, cnt):
    if idx == len(arr)-1:
        if arr[idx] == '0':
            return 1
        else:
            return 0
    else:
        if arr[idx] == '0':
            return 1 + count_0(idx+1, arr, cnt+1)
        else:
            return count_0(idx+1, arr, cnt)

arr = '10101010'

print(count_0(0, arr, 0))
'''


# 최대값 찾기
'''
#include<stdio.h>



int Max(int *arr, int n){

	if (n == 1){

		return *arr;

	}

	else{

		if (*(arr + n - 1) > Max(arr, n - 1)){

			return *(arr + n - 1);

		}

		else{

			return Max(arr, n - 1);

		}

	}

}



void main(){

	int n, arr[20] = { 0 };

	scanf("%d", &n);

	for (int i = 0; i < n; i++){

		scanf("%d", &arr[i]);

	}

	printf("%d\n", Max(arr, n));

}
'''