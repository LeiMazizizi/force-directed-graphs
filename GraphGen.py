import json
import numpy as np
import random
import os

# Styles
#  - "k" : complete
#  - "t" : tree
#  - "p" : planar
#  - "c" : components

def GenerateGraph(numVerts, density, maxWeight, style, numGroups=5):
    nodes = [] ; links = []

    # Generate Nodes
    for x in range(numVerts):
        nodes.append({'group': np.random.randint(numGroups), 'name': x})

    if style == "k":  # Generate Complete
        print("Generating Complete...")
        for x in nodes:
            for y in nodes[x['name']+1:]:
                if np.random.binomial(1, density) == 1:
                    w = np.random.randint(maxWeight)
                    links.append({'source': x['name'], 'target': y['name'], 'value': w})

    elif style == "t":  # Generate Tree
        print("Generating Tree...")
        N = nodes
        C = int(len(N)*density*.33)
        if C == 0: C == 1
        r = N[0]
        N = N[1:] ; N.reverse()
        while N != []:
            c = np.random.randint(C)+1
            if len(N) <= c:
                for n in N:
                    w = np.random.randint(maxWeight)
                    links.append({'source': n['name'], 'target': r['name'], 'value': w})
                N=[]
            else:
                children = N[:c]; N = N[c:]
                pIndex = np.random.randint(len(N))
                P = N[pIndex]
                for child in children:
                    w = np.random.randint(maxWeight)
                    links.append({'source':child['name'], 'target': P['name'], 'value': w})

    elif style == "p": # Generate planar graph
        A = nodes.copy()
        B = nodes.copy()
        random.shuffle(A)
        random.shuffle(B)
        for u in nodes:
            leg = A.pop()
            root = B.pop()
            print(leg, root)
            if np.random.binomial(1, density) == 1:
                links.append({'source': root['name'], 'target': leg['name'], 'value': np.random.randint(maxWeight)})
            if np.random.binomial(1, density) == 1:
                links.append({'source': u['name'], 'target': root['name'], 'value': np.random.randint(maxWeight)})
            elif np.random.binomial(1, density) == 1:
                links.append({'source': u['name'], 'target': leg['name'], 'value': np.random.randint(maxWeight)})

    elif style == "c": # Generate Connected Components
        print("Generating Connected Components...")
        N = nodes ; A = []
        C = int(len(N)*density*.33)
        if C == 0: C==1
        # Initial blob
        c = np.random.randint(1,C)
        if c >= len(N):
            blob = N ; N = []
        else:
            blob = N[:c] ; N = N[c:]
        for x in blob:
            for y in blob[x['name']+1:]:
                if np.random.binomial(1, density) == 1:
                    w = np.random.randint(maxWeight)
                    links.append({'source': x['name'], 'target': y['name'], 'value': w})
        A.extend(blob)

        while N != []:
            c = np.random.randint(1,C)
            if c >= len(N):
                blob = N; N = []
            else:
                blob = N[:c]; N = N[c:]
            for i in blob:
                for j in blob[blob.index(i) + 1:]:
                    if np.random.binomial(1, density) == 1:
                        w = np.random.randint(maxWeight)
                        links.append({'source': i['name'], 'target': j['name'], 'value': w})
            c = np.random.randint(len(A))
            k = A[c] ; r = blob[0]
            w = np.random.randint(maxWeight)
            links.append({'source': r['name'], 'target': k['name'], 'value': w})
            A.extend(blob)

    return {'links': links,'nodes': nodes}



def FindCliques(graph_data):
    print("Finding Cliques -> Returns list list of nodes in each clique -> store in DB")
    nodes = graph_data['nodes']
    links = graph_data['links']





def ExtractCliques(clique_array):
    print("Recoloring Cliques")




def GraphToJSON(data):
    os.remove('static/graph.json')
    with open('static/graph.json','w') as f: json.dump(data,f)


GenerateGraph(21,1,10,"c")