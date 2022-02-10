C = int(input())


def convert(_char):
    if _char == 'a': return 0
    if _char == 'b': return 1
    if _char == 'c': return 2
    if _char == 'd': return 3
    if _char == 'e': return 4
    if _char == 'f': return 5
    if _char == 'g': return 6
    if _char == 'h': return 7
    if _char == 'i': return 8
    if _char == 'j': return 9
    if _char == 'k': return 10
    if _char == 'l': return 11
    if _char == 'm': return 12
    if _char == 'n': return 13
    if _char == 'o': return 14
    if _char == 'p': return 15
    if _char == 'q': return 16
    if _char == 'r': return 17
    if _char == 's': return 18
    if _char == 't': return 19
    if _char == 'u': return 20
    if _char == 'v': return 21
    if _char == 'w': return 22
    if _char == 'x': return 23
    if _char == 'y': return 24
    if _char == 'z': return 25

for _ in range(C):
    n = int(input())

    words = []
    for _ in range(n):
        words.append(str(input()))
    
    #인접 행렬 스타일
    adj = [[0]*26 for _ in range(26)]

    #i 로 시작해서 j로 끝나는 단어
    graphs = [] 
    for _ in range(26):
        graphs.append([[] for _ in range(26)])
    
    #i 로 끝나는 단어 수
    indegree = [0 for _ in range(26)]

    #i 로 시작하는 단어 수
    outdegree = [0 for _ in range(26)]

    def makeGraph(_words):

        for word in words:
            f_word = convert(word[0])
            l_word = convert(word[-1])

            adj[f_word][l_word] += 1
            graphs[f_word][l_word].append(word)
            indegree[l_word] += 1
            outdegree[f_word] += 1
    
    def getEulerCircuit(here, circuit):
        for there in range(26):
            while adj[here][there] > 0:
                adj[here][there] -= 1
                getEulerCircuit(there, circuit)
        
        circuit.append(here)

    def getEulerTrailOrCircuit():
        circuit = []

        for i in range(26):
            if outdegree[i] == (indegree[i] + 1):
                getEulerCircuit(i, circuit)
                return circuit
            
        for i in range(26):
            if outdegree[i]:
                getEulerCircuit(i, circuit)
                return circuit
        return circuit

    def checkEuler():
        plus1 = minus1 = 0

        for ind, outd in zip(indegree, outdegree):
            delta = outd - ind

            if delta < -1 or delta > 1: return False
            if delta == -1: minus1 += 1
            if delta == 1: plus1 += 1

        if (plus1 == 1 and minus1 == 1) or (plus1 ==0 and minus1 == 0): return True
    

    def solve(words):
        makeGraph(words)

        if not checkEuler(): return 'IMPOSSIBLE'

        circuit = getEulerTrailOrCircuit()

        if len(circuit) != len(words) + 1: return 'IMPOSSIBLE'

        circuit = circuit[::-1]

        ret = ""
        for i in range(1,len(circuit),1):
            a = circuit[i-1]
            b = circuit[i]

            ret += graphs[a][b][-1]
            ret += " "
            del graphs[a][b][-1]
        return ret

    print(solve(words))