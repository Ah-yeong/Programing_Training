import heapq  # 우선순위 큐 구현

def dijkstra(graph, start): # graph에는 각 정점과 인접한 정점, 가중치가 저장됨
  distances = {node: float('inf') for node in graph}  # start로 부터의 거리 값을 저장
  distances[start] = 0  # 시작 값은 0
  queue = []
  heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작

  while queue:  # queue에 남아 있는 노드가 없으면 끝
    current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리

    if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 긴 경우
      continue
    
    for new_destination, new_distance in graph[current_destination].items():
      distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
      if distance < distances[new_destination]:  # 알고 있는 거리 보다 작은 경우
        distances[new_destination] = distance    # 거리 저장
        heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
  return distances

graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

print(dijkstra(graph, 'A'))
