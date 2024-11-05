import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices 
        self.graph = {}   

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  

    def prim_mst(self):
        min_heap = []
        in_mst = [False] * self.V
        
        if 0 not in self.graph:
            print("Vertex 0 has no edges. Please ensure valid input.")
            return [], 0
        
     
        in_mst[0] = True
        
        for v, weight in self.graph[0]:
            heapq.heappush(min_heap, (weight, 0, v))  

        mst_weight = 0
        mst_edges = []

        while min_heap:
            weight, u, v = heapq.heappop(min_heap)

            if in_mst[v]:
                continue  

           
            in_mst[v] = True
            mst_weight += weight
            mst_edges.append((u, v, weight))

           
            for next_v, next_weight in self.graph[v]:
                if not in_mst[next_v]:
                    heapq.heappush(min_heap, (next_weight, v, next_v))

        return mst_edges, mst_weight

def main():
    
    num_vertices = int(input("Enter the number of vertices: "))
    g = Graph(num_vertices)

   
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        u, v, weight = map(int, input("Enter edge (u, v, weight): ").split())
        g.add_edge(u, v, weight)

    
    mst_edges, total_weight = g.prim_mst()

    if mst_edges:
        print("\nEdges in the Minimum Spanning Tree:")
        for u, v, weight in mst_edges:
            print(f"{u} -- {v} (weight: {weight})")
        print("Total weight of MST:", total_weight)
    else:
        print("No MST found due to invalid input.")

if __name__ == "__main__":
    main()
