# ps-python
python Problem Solving

---
### baekjoon
#### graph
* 최단거리 가중치가 모두 같은 경우에는 dfs, bfs(더 좋음) , 다른 경우 dijkstra
>* 2606
>   * dfs나 bfs, 단방향일시 끊어졌을때 조회가 다 안됨, 양방향 필요
    
>* 1012
>   * dfs로 4방향 탐색. 재귀 깊이 sys.setrecursionlimit() 필요
>   * 좌표 x, y 입력시, 사용시 통일되게 해야함

>* 2468
>   * 높이정보 이하 변경하면서 dfs 4방향 탐색


