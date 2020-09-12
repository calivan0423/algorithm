import sys
sys.stdin = open("ucpc2020.txt","rt")
import time

'''

if __name__ == "__main__":
    n = int(input())
    list = []
    D=0
    G=0
    for i in range(n+1):
        list.append([])
    for i in range(n - 1):
        a, b = map(int, input().split())
        list[a].append(b)
        list[b].append(a)



class Graph:
    def __init__(self):
        self.graph = {}
        self.marked = []
        self.edge = {}

    def add(self,v,w):
        if v not in self.graph:
            self.graph[v]={w}
        else:
            self.graph[v].add(w)

        if w not in self.graph:
            self.graph[w]={v}
        else:
            self.graph[w].add(v)

    def bfs_path(self,start,finish):
        queue =[start]
        self.marked.append(start)
        while queue:
            v = queue.pop(0)
            if v == finish: #도착노드
                return
            for w in self.graph[v]:
                if w not in self.marked:
                    self.edge[w]=v
                    queue.append(w)
                    self.marked.append(w)

    def path_to(self,start,finish):
        path = []
        i = finish
        while i!=start:
            path.append(i)
            i=self.edge[i]
        path.append(start)
        return path

    def shortest_path(self,start,finish):
        #self.edge.clear()
        self.marked.clear()
        self.bfs_path(start,finish)
        if finish not in self.marked:
            return (False)
        path = self.path_to(start,finish)
        path.reverse()
        return len(path)

if __name__ == "__main__":
    n = int(input())
    list=[]
    for i in range(0,n+1):
        list.append([])
    g = Graph()
    g.nodes = set(range(1, n+1))
    D=0
    G=0
    for i in range(n-1):
        a, b = map(int, input().split())
        g.add(a,b)
        list[a].append(b)
        list[b].append(a)

    for i in range(n+1):
        k=len(list[i])
        if k==3:
            G+=1
    for i in range(1, n+1):
        for j in range(i,n+1):
            k=g.shortest_path(i,j)
            if k == 4:
                D += 1
    if D==0:
        print('G')
    elif G==0:
        print('D')
    else:
        result = D/G
        if result >3 :
            print('D')
        elif result<3:
            print('G')
        else :
            print('DUDUDUNGA')




INF = sys.maxsize

def F(n,a):
    dist = [[INF]*(n) for i in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j]=a[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j]>dist[i][k]+dist[k][j]:
                    dist[i][j]=dist[i][k]+dist[k][j]
    return dist

if __name__ == "__main__":

    n = int(input())
    list = [[INF for col in range(n)] for row in range(n)]
    list2 = []
    for i in range(0, n + 1):
        list2.append([])
    D = 0
    G = 0
    for i in range(n-1):
        a, b = map(int, input().split())
        list[a-1][b-1] = 1
        list[b-1][a-1] = 1
        list2[a].append(b)
        list2[b].append(a)

    dist = F(n,list)

    for i in range(n):
        for j in range(n):
            if dist[i][j]==3:
                D+=1
    D/=2

    for i in range(n + 1):
        k = len(list2[i])
        if k == 3:
            G += 1

    if D == 0:
        print('G')
    elif G == 0:
        print('D')
    else:
        result = D / G
        if result > 3:
            print('D')
        elif result < 3:
            print('G')
        else:
            print('DUDUDUNGA')


from heapq import heappop, heappush

def dijkstra(s):
	result=[float('inf') for _ in range(n)]
	result[s]=0
	que=list()
	heappush(que,(result[s],s))
	while que:
		result_v,v=heappop(que)
		for fu,fw in graph[v]:
			if result[fu]>result_v+fw:
				result[fu]=result_v+fw
				heappush(que,(result[fu],fu))
	return result


if __name__ == "__main__":
    n = int(input())
    e=n-1
    D = 0
    G = 0
    graph=[[] for _ in range(n)]
    for _ in range(e):
        a,b=map(int,input().split())
        graph[a-1].append((b-1,1))
        graph[b-1].append((a-1,1))
    for i in range(n):
        k = len(graph[i])
        if (k==3):
            G+=1

    for i in range(1,n+1):
        D += dijkstra(i-1).count(3)
    D/=2

    if D == 0:
        print('G')
    elif G == 0:
        print('D')
    else:
        result = D / G
        if result > 3:
            print('D')
        elif result < 3:
            print('G')
        else:
            print('DUDUDUNGA')
'''
import queue

list = []
D = 0
G = 0



if __name__ == "__main__":
    n = int(input())
    for i in range(n + 1):
        list.append([])
    for i in range(n - 1):
        a, b = map(int, input().split())
        list[a].append(b)

    for j in range(1,n+1):
        le=len(list[j])
        if le ==2:
            G+=1
        h=1
        q=[]
        for i in (list[j]):
            q.append(i)
            while q:
                k= q.pop(0)
                for i in (list[k]):
                    q.append(i)
                    h+=1
                if h==4:
                    D+=1


    if D == 0:
        print('G')
    elif G == 0:
        print('D')
    else:
        result = D / G
        if result > 3:
            print('D')
        elif result < 3:
            print('G')
        else:
            print('DUDUDUNGA')





