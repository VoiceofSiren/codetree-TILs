'''
큐가 가지는 의미: 탐색 가능한 정점의 모음

큐가 비어 있지 않으면 계속 탐색
큐가 비어 있으면 탐색 종료
'''


from collections import deque

n, m = map(int, input().split())

# 지도 입력
a = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 각 지점을 방문했는지 여부
visited = [
    [ 0 for _ in range(m) ]
    for _ in range(n)
]

# dist[i][j]: (i, j)에 도달하는 데 필요한 거리
# 거리에 대한 가중치는 모두 동일할 때만 사용 가능한 로직임.
dist = [
    [ -1 for _ in range(m) ]
    for _ in range(n)
]

def bfs():
    # q를 통해 너비 우선 탐색
    while q:
        # 현재 위치가 r행 c열을 탐색 중이다.
        r, c = q.popleft()

        # (r, c)와 인접한 칸인 (nr, nc)를 찾기
        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nr = r + dr
            nc = c + dc

            # 격자를 벗어나지 않는지 확인       / 뱀이 없는지       / 방문한 적이 없는지
            if 0 <= nr < n and 0 <= nc < m and a[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = 1
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))

# bfs를 위한 새로운 queue를 생성
q = deque()
# (0, 0)은 탐색 성공
visited[0][0] = 1
# (0, 0)까지의 거리는 0이다.
dist[0][0] = 1
q.append((0, 0))

# 탐색 수행
bfs()

print(visited[n - 1][m - 1])