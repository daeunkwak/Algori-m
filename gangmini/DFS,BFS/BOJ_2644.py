
class Kinship:
    count = 0

    def __init__(self, graph,people,find_node):
        self.graph = graph
        self.visited = [0 for _ in range(people)]
        self.find_node = find_node


    def find_kinship(self,start_node): #dfs로 구현
        if(start_node == self.find_node):
            print(self.count)
            exit(0)

        self.visited[start_node - 1] = 1

        for i in self.graph[start_node - 1]:
            if (self.visited[i - 1] == 0):  # 방문 안 한 노드
                self.count += 1
                self.find_kinship(i)
        self.count -= 1


def main():
    people = int(input())
    x, y = map(int, input().split())
    relation = int(input())

    ## 인접리스트로 그래프 구현
    graph = [[] for _ in range(people)]
    for i in range(relation):
        parent, child = map(int, input().split())
        graph[(parent)-1].append(child)
        graph[(child)-1].append(parent)

    kinship_instance = Kinship(graph,people,y)
    kinship_instance.find_kinship(x)
    print(kinship_instance.count)

if __name__ == '__main__':
    main()