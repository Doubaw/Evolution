#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pulp
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
import random
import time

def main():
    
#     Erdos-Renyi
#     n = 25  # 點的數量
#     np = 0.2  # 邊的概率
#     # 建立一個 Erdos-Renyi 圖
#     G = nx.erdos_renyi_graph(n, np)
#     G = nx.relabel_nodes(G, {node: str(node + 1) for node in G.nodes})
    
#     barabasi_albert_graph
#     G = nx.barabasi_albert_graph(n=28, m=2)
#     G = nx.relabel_nodes(G, {node: str(node + 1) for node in G.nodes})

#     all_nodes = set()
#     adj = defaultdict(list)
#     for edge in edges:
#         all_nodes.update(edge)
#         adj[edge[0]].append(edge[1])
    
#     G = nx.barabasi_albert_graph(n=29, m=2)

# Brightkite_edges_2720_2870


#     edges = []
#     with open('Brightkite_edges_591_678.txt', 'r') as file:
        
#         for line in file:
#             edges.append(tuple(map(str, line.strip().split("\t")))) 

#     # 使用文件中的邊來創建一個圖
#     G = nx.Graph(edges)
#         # 找出最大的連通組件
#     connected_components = sorted(nx.connected_components(G), key=len, reverse=True)

#     # 創建一個新的只包含最大連通組件的圖
#     G = G.subgraph(connected_components[0]).copy()
    
#     # 創建鄰接表
#     adj = defaultdict(list)
#     for edge in edges:
#         adj[edge[0]].append(edge[1])
#         adj[edge[1]].append(edge[0])
        

    G = nx.barabasi_albert_graph(n=25, m=7)
    G = nx.relabel_nodes(G, {node: str(node + 1) for node in G.nodes})


    all_nodes = list(G.nodes)
    edges = list(G.edges)

    # 建立節點的鄰接字典
    adj = defaultdict(list)
    for edge in edges:
        adj[edge[0]].append(edge[1])  # 為每個節點建立鄰接列表
        adj[edge[1]].append(edge[0])  # 因為這是無向圖，所以每個邊的兩個節點都是對方的鄰接節點

    p = 2

#     all_nodes = set()
#     adj = defaultdict(list)
#     for edge in edges:
#         all_nodes.update(edge)
#         adj[edge[0]].append(edge[1])

#     for node in list(adj.keys()):
#         if len(adj[node]) < p:
#             del adj[node]

#     new_edges = [(i, j) for i in adj for j in adj[i]]

#     G = nx.Graph()
#     G.add_edges_from(new_edges)
#     G.remove_nodes_from([node for node, degree in dict(G.degree()).items() if degree < p])

#     all_nodes = list(G.nodes())
#     adj = {node: list(G.neighbors(node)) for node in all_nodes}

    while True:
        degrees = dict(G.degree())
        nodes_to_remove = [node for node, degree in degrees.items() if degree < p]
        if not nodes_to_remove:  # 沒有節點需要刪除，可以退出迴圈
            break
        G.remove_nodes_from(nodes_to_remove)

    
    # 更新節點列表和鄰接表
    all_nodes = list(G.nodes())
    adj = {node: list(G.neighbors(node)) for node in all_nodes}
    

    n = len(all_nodes)

    # Set K to the total number of nodes in the pruned network
    K = len(all_nodes)
    print("K: ",K)

    prob = pulp.LpProblem("problem", pulp.LpMinimize)
    x = pulp.LpVariable.dicts("x", [(i, t) for i in all_nodes for t in range(n)], cat=pulp.LpBinary)

    prob += pulp.lpSum([x[(i, 0)] for i in all_nodes])

    for i in all_nodes:
        prob += pulp.lpSum([x[(j, 0)] for j in adj[i]]) >= p * x[(i, 0)]
        for t in range(1, n):
            prob += pulp.lpSum([x[(j, t-1)] for j in adj[i]]) >= p * x[(i, t)]
            prob += x[(i, t-1)] <= x[(i, t)]

    prob += pulp.lpSum([x[(i, n-1)] for i in all_nodes]) >= K

    start_time = time.time()
    prob.solve()
    end_time = time.time()
    solve_time = end_time - start_time  # 計算求解時間

    print("Integer")
    print("Status:", pulp.LpStatus[prob.status])  # 輸出求解的狀態
    print("Solving time: ", solve_time, "seconds")  # 輸出求解時間

    initial_nodes = [i for i in all_nodes if pulp.value(x[(i, 0)]) == 1]
    affected_nodes = [i for i in all_nodes if any(pulp.value(x[(i, t)]) == 1 for t in range(n))]

    print("Initial nodes: ", initial_nodes)
    print("Affected nodes: ", affected_nodes)

    # 計算並輸出初始節點和受影響節點的數量
    initial_nodes_count = len(initial_nodes)
    affected_nodes_count = len(affected_nodes)

    print("Number of initial nodes: ", initial_nodes_count)
    print("Number of affected nodes: ", affected_nodes_count)

#     G = nx.Graph()
#     G.add_edges_from(new_edges)
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 10))
    nx.draw_networkx_nodes(G, pos, node_size=300, nodelist=all_nodes, node_color='blue')
    nx.draw_networkx_nodes(G, pos, node_size=300, nodelist=affected_nodes, node_color='green')
    nx.draw_networkx_nodes(G, pos, node_size=300, nodelist=initial_nodes, node_color='red')
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, labels={node: node for node in all_nodes}, font_color='white')

    plt.title('Network Graph')
    plt.show()


    print("========================================================================")


    # 設定K為修剪網絡中的節點總數
    K = len(all_nodes)
    print("K: ",K)

    # 建立線性規劃問題
    prob = pulp.LpProblem("problem", pulp.LpMinimize)

    # 定義決策變數x，表示在時間t時，節點i是否被選中
    x = pulp.LpVariable.dicts("x", [(i, t) for i in all_nodes for t in range(n)], cat=pulp.LpContinuous, lowBound=0, upBound=1)

    # 設定目標函數，最小化在時間0時被選中的節點數量
    prob += pulp.lpSum([x[(i, 0)] for i in all_nodes])

    # 設定約束條件
    for i in all_nodes:
        prob += pulp.lpSum([x[(j, 0)] for j in adj[i]]) >= p * x[(i, 0)]
        for t in range(1, n):
            prob += pulp.lpSum([x[(j, t-1)] for j in adj[i]]) >= p * x[(i, t)]
            prob += x[(i, t-1)] <= x[(i, t)]

    # 設定在最後的時間點，被選中的節點數量應該大於等於K
    prob += pulp.lpSum([x[(i, n-1)] for i in all_nodes]) >= K

    # 求解問題並計算求解時間
    start_time = time.time()
    prob.solve()
    end_time = time.time()
    solve_time = end_time - start_time

    print("Linear")
    print("Status:", pulp.LpStatus[prob.status])  # 輸出求解的狀態
    print("Solving time: ", solve_time, "seconds")  # 輸出求解時間

    # 找出在第一個時間點被選取的節點，並保存其 x 值
    initial_nodes = [(i, pulp.value(x[(i, 0)])) for i in all_nodes if pulp.value(x[(i, 0)]) > 0]
    
    print(initial_nodes)
    
    # 根據 x 值進行降序排序
    initial_nodes.sort(key=lambda node: -node[1])
    
    # 從tuple中只取節點
    initial_nodes = [node[0] for node in initial_nodes]

#     def spread_p_core(G, initial_nodes, K, p):
#         # 建立一個 set 保存選擇的節點
#         selected_nodes = set()
#         # 建立一個 set 保存已影響的節點
#         influenced_nodes = set()

#         # 初始節點列表已經依照 x 值降序排序
#         for node in initial_nodes:
#             selected_nodes.add(node)
#             # 更新受影響節點
#             influenced_nodes.update(nx.single_source_shortest_path_length(G, node).keys())

#             # 檢查是否達到 p-core
#             sub_graph = G.subgraph(selected_nodes)
#             core = nx.k_core(sub_graph, p)
#             # 如果子圖形成 p-core 且影響節點大於等於 K 則停止
#             if core.number_of_nodes() > 0 and len(influenced_nodes) >= K:
#                 break

#         return selected_nodes, influenced_nodes

#     # 執行演算法
#     selected_nodes, influenced_nodes = spread_p_core(G, initial_nodes, K, p)
    def spread_p_core(G, initial_nodes, K, p):
        selected_nodes = set()
        selected_nodes_list = []  # 這個列表用來保存根據貪婪算法選擇的節點
        influenced_nodes = set()

        for node in initial_nodes:
            selected_nodes.add(node)
            selected_nodes_list.append(node)  # 將選擇的節點添加到列表中
            influenced_nodes.update(nx.single_source_shortest_path_length(G, node).keys())

            sub_graph = G.subgraph(selected_nodes)
            core = nx.k_core(sub_graph, p)
            if core.number_of_nodes() > 0 and len(influenced_nodes) >= K:
                break

        return selected_nodes, influenced_nodes, selected_nodes_list

    # 執行演算法
    selected_nodes, influenced_nodes, selected_nodes_list = spread_p_core(G, initial_nodes, K, p)

    # 打印根據貪婪算法選擇的節點的列表
    print("Nodes selected by the greedy algorithm:", selected_nodes_list)

    print("Selected nodes: ", selected_nodes)
    print("Selected nodes_len: ", len(selected_nodes))
    print("Affected nodes: ", influenced_nodes)
    print("Affected nodes_len: ", len(influenced_nodes))


        # If you have a graph G, uncomment the lines below:
        
        # 使用spring_layout方法為圖G的每個節點生成位置
    pos = nx.spring_layout(G)

    # 繪製圖G
    plt.figure(figsize=(10, 10))
    nx.draw_networkx_nodes(G, pos, node_size=300, nodelist=all_nodes, node_color='blue')
    nx.draw_networkx_nodes(G, pos, node_size=300, nodelist=influenced_nodes, node_color='green')
    nx.draw_networkx_nodes(G, pos, node_size=300, nodelist=selected_nodes, node_color='red')
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, labels={node: node for node in all_nodes}, font_color='white')

    plt.title('Network Graph')
    plt.show()

#         return selected_nodes, affected_nodes

#     select_influential_nodes(initial_nodes, adj, p, K)

for i in range(1):  
    print(i)
    main()
    print("--------------------")


# In[ ]:




