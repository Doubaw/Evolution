#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pulp
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
import time
from itertools import combinations
import itertools
from networkx.algorithms.cycles import simple_cycles


def main():
#     G = nx.barabasi_albert_graph(n=35, m=3)
#     k = 4 
#     p = 3 



#     G = nx.barabasi_albert_graph(n=35, m=3)
#     k = 5 
#     p = 3


#     G = nx.barabasi_albert_graph(n=26, m=6)
#     G = nx.barabasi_albert_graph(n=28, m=5)
    G = nx.barabasi_albert_graph(n=28, m=5)
#     k = 5 
#     p = 4

    G = nx.relabel_nodes(G, {node: str(node + 1) for node in G.nodes})

    
    
#     n = 25  # 點的數量
#     np = 0.4  # 邊的概率
#     # 建立一個 Erdos-Renyi 圖
#     G = nx.erdos_renyi_graph(n, np)
#     G = nx.relabel_nodes(G, {node: str(node + 1) for node in G.nodes})
    
    
    all_nodes = list(G.nodes)
    edges = list(G.edges)

    adj = defaultdict(list)
    for edge in edges:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])

    k = 5 
    p = 4 

    all_nodes = set()
    adj = defaultdict(list)
    for edge in edges:
        all_nodes.update(edge)
        adj[edge[0]].append(edge[1])

    for node in list(adj.keys()):
        if len(adj[node]) < p:
            del adj[node]

    new_edges = [(i, j) for i in adj for j in adj[i]]

    G = nx.Graph()
    G.add_edges_from(new_edges)

    G.remove_nodes_from([node for node, degree in dict(G.degree()).items() if degree < p])

    all_nodes = list(G.nodes())
    adj = {node: list(G.neighbors(node)) for node in all_nodes}      
    
    n = len(all_nodes)
    print("n: ", n)

    prob = pulp.LpProblem("Integer", pulp.LpMaximize)

    x = pulp.LpVariable.dicts("x", [(i, t) for i in all_nodes for t in range(n)], cat=pulp.LpBinary)

    prob += pulp.lpSum([x[(i, n-1)] for i in all_nodes])

    prob += pulp.lpSum([x[(i, 0)] for i in all_nodes]) == k

    for i in adj:
        prob += pulp.lpSum([x[(j, 0)] for j in adj[i]]) >= p * x[(i, 0)]
        for t in range(1, n):
            prob += pulp.lpSum([x[(j, t-1)] for j in adj[i]]) >= p * x[(i, t)]
            prob += x[(i, t-1)] <= x[(i, t)]

    start_time = time.time()
    prob.solve()
    end_time = time.time()
    solve_time = end_time - start_time

    print("Integer")
    print("Status:", pulp.LpStatus[prob.status])
    print("Solving time: ", solve_time, "seconds")

    initial_nodes = [i for i in all_nodes if pulp.value(x[(i, 0)]) == 1]
    affected_nodes = [i for i in all_nodes if any(pulp.value(x[(i, t)]) == 1 for t in range(n))]
    last_affected_nodes = [i for i in all_nodes if pulp.value(x[(i, n-1)]) == 1]

    print("Initial_nodes: ", initial_nodes)
    print("Affected_nodes: ", affected_nodes)
    print("Last_affected_nodes: ",last_affected_nodes)

    initial_nodes_count = len(initial_nodes)
    affected_nodes_count = len(affected_nodes)

    print("Number of initial nodes: ", initial_nodes_count)
    print("Number of affected nodes: ", affected_nodes_count)

    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 10))
    nx.draw_networkx_nodes(G, pos, node_size=300, nodelist=all_nodes, node_color='blue')
    nx.draw_networkx_nodes(G, pos, node_size=300, nodelist=affected_nodes, node_color='green')
    nx.draw_networkx_nodes(G, pos, node_size=300, nodelist=initial_nodes, node_color='red')
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, labels={node: node for node in all_nodes}, font_color='white')

    plt.title('Integer Graph')
    plt.show()

    print("===============================================================================")

    n = len(all_nodes)
    print("n: ", n)

    prob = pulp.LpProblem("Linear", pulp.LpMaximize)

    x = pulp.LpVariable.dicts("x", [(i, t) for i in all_nodes for t in range(n)], cat=pulp.LpContinuous, lowBound=0, upBound=1)

    prob += pulp.lpSum([x[(i, n-1)] for i in all_nodes])

    prob += pulp.lpSum([x[(i, 0)] for i in all_nodes]) == k 

    for i in adj:
        prob += pulp.lpSum([x[(j, 0)] for j in adj[i]]) >= p * x[(i, 0)] 
        for t in range(1, n):
            prob += pulp.lpSum([x[(j, t-1)] for j in adj[i]]) >= p * x[(i, t)]
            prob += x[(i, t-1)] <= x[(i, t)] 

    start_time = time.time()   
    prob.solve()
    end_time = time.time()
    solve_time = end_time - start_time 


    print("Linear")
    print("Status:", pulp.LpStatus[prob.status]) 
    print("Solving time: ", solve_time, "seconds")

    initial_nodes = sorted([(i, pulp.value(x[(i, 0)])) for i in all_nodes if pulp.value(x[(i, 0)]) > 0], key=lambda x: x[1], reverse=True)
    initial_nodes = [node[0] for node in initial_nodes]
    print("Initial_nodes: ", initial_nodes)

    def find_k_cycle_dfs(G, k, initial_nodes):
        initial_nodes_set = set(initial_nodes)
        cycles_set = set()

        def dfs(node, visited, path):
            visited.add(node)
            path.append(node)
            if len(path) == k:
                if path[0] in G.neighbors(node):
                    cycle = tuple(sorted(path))  # 排序並轉為元組
                    cycles_set.add(cycle)  # 將 cycle 加入到集合中
            else:
                for neighbor in initial_nodes_set.difference(visited):
                    if neighbor in G.neighbors(node):
                        dfs(neighbor, visited, path)
            path.pop()
            visited.remove(node)

        for node in initial_nodes:
            dfs(node, set(), [])

        # 將每個元組轉換回列表
        return [list(cycle) for cycle in cycles_set]

    # 使用上述函數
    k_clique = find_k_cycle_dfs(G, k, initial_nodes)
#     if k_clique:
#         print("Found k-cycle: ", k_clique)
#     else:
#         print("No k-cycle found.")

#     print("The k-cycle with maximum spread is: ", max_k_cycle)
    def p_core_spread(G, k_clique, p):
        # 從k-clique開始進行擴散
        initial_nodes = k_clique

        # 初始化受影響的節點
        affected_nodes = set(initial_nodes)
        new_affected = set(initial_nodes)

        while new_affected:
            current_affected = set(new_affected)
            new_affected = set()
            for node in current_affected:
                # 找出所有節點的鄰居
                neighbors = set(G.neighbors(node))
                # 如果鄰居的數量大於等於p，則將它們添加到新受影響的節點集合
                for neighbor in neighbors:
                    if len(set(G.neighbors(neighbor)).intersection(affected_nodes)) >= p and neighbor not in affected_nodes:
                        new_affected.add(neighbor)
            # 當新的受影響節點數量為0時，停止迴圈
            if len(new_affected) == 0:
                break
            affected_nodes.update(new_affected)

        return affected_nodes

    k_cycles = find_k_cycle_dfs(G, k, initial_nodes)

    
    if not k_cycles:
        print("No k-cycle found.")
    else:
        # 保存每個 k-cycle 擴散的影響節點數量
        k_cycle_spreads = {}

        for k_cycle in k_cycles:
            affected_nodes = p_core_spread(G, k_cycle, p)
            print(affected_nodes)
            k_cycle_spreads[tuple(k_cycle)] = len(affected_nodes)
        max_spread_k_cycle = max(k_cycle_spreads, key=k_cycle_spreads.get)
        max_spread_nodes = p_core_spread(G, list(max_spread_k_cycle), p)
    
        print(k_cycle_spreads)

        print(max_spread_k_cycle)
        print(max_spread_nodes)
    #     print("Affected nodes:", affected_nodes)
    #     print("Number of affected nodes:",len(affected_nodes))
        initial_nodes = max_spread_k_cycle
        affected_nodes = max_spread_nodes

        # 繪製圖表
        pos = nx.spring_layout(G)
        plt.figure(figsize=(10, 10))
        nx.draw_networkx_nodes(G, pos, node_size=300, nodelist=all_nodes, node_color='blue')
        nx.draw_networkx_nodes(G, pos, node_size=300, nodelist=affected_nodes, node_color='green')
        nx.draw_networkx_nodes(G, pos, node_size=300, nodelist=initial_nodes, node_color='red')
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos, labels={node: node for node in G.nodes}, font_color='white')
        plt.show()

for i in range(1):
    print(i)
    main()
    print("-----------------------------")


# In[ ]:




