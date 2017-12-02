import numpy as np
import networkx as nx
import sys

def dijkstra_2_src(G, s1, s2):
    pass

                # T = nx.Graph()      # tree
                #
                # l = [np.inf for v in G.nodes()]   # lambda vector
                # p = np.array([-1 for v in G.nodes()])       # pred. vector
                #
                # l[int(s1)] = 0
                # l[int(s2)] = 0
                #
                # p[int(s1)] = 0
                # p[int(s2)] = 0
                #
                # # Q = np.array(G.nodes())
                # Q = G.nodes()
                #
                # while(len(Q) != 0):
                #     #print(len(Q))
                #     # extract min
                #     menor = l[0]
                #     u = Q[0]
                #     for i in l:
                #         if(i < menor) and (i in Q):
                #             menor = i
                #             u = i
                #
                #     uIndex = Q.index(u)
                #     del Q[uIndex]
                #     #print(Q.size)
                #     # T = T union {u}
                #     T.add_node(u)
                #     T.add_edge(u, p[uIndex], weight=(G[u][p[u]]['weight']))
                #
                #     for v in G.neighbors(u):
                #         # relax
                #         if ((v in Q) and (l[Q.index(v)] > l[uIndex] + G[u][v]['weight'])):
                #             l[Q.index(v)] = l[uIndex] + G[u][v]['weight']
                #             p[Q.index(v)] = u

                # T = nx.Graph()
                #
                # n = np.array([-1 for i in range(G.number_of_nodes())])
                # sp = np.array([float('Inf') for i in range(G.number_of_nodes())])
                #
                # sp[int(s1)] = 0
                # sp[int(s2)] = 0
                #
                # Q = np.array(G.nodes())
                #
                # while(Q.size != 0):
                #     u = np.argmin(sp)
                #     print(u)
                #     sp = np.delete(sp, u)
                #     Q = np.delete(Q, u+1)
                #     T.add_node(u+1)
                #     if(u+1 != s1 and u+1 != s2):
                #         T.add_edge(n[u], u, weight=G.get_edge_data(n[u], u+1)['weight'])
                #     for v in G.neighbors(u+1):
                #         aux = np.array(relax(u+1, v-1, G, sp, n))
                #         if(aux.size != 0):
                #             sp = np.array(aux[0])
                #             n = np.array(aux[1])