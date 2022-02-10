heap = []

def push_heap(heap, newValue):
    heap.append(newValue)

    childidx = len(heap) - 1
    parentidx = (childidx - 1) // 2

    while childidx != 0 and newValue > heap[parentidx]:
        heap[childidx] = heap[parentidx]

        childidx = parentidx
        parentidx = (childidx -1) // 2
    
    heap[childidx] = newValue
    return heap

def pop_heap(heap):

    ret_val = heap[0]

    heap[0] = heap[-1]

    del heap[-1]

    here = 0

    while True:
        left = here * 2 + 1
        right = here * 2 + 2

        if left >= len(heap): break
        
        next = here
        
        if heap[left] > heap[next]:
            next = left
        
        if right < len(heap) and heap[right] > heap[next]:
            next = right

        if next == here: break
        tmp = heap[here]
        heap[here] = heap[next]
        heap[next] = tmp

        here = next

    return ret_val

if __name__ == '__main__':
    while True:
        n = int(input())
        if n == -1: break

        heap = push_heap(heap, n)
    print(heap)
    while len(heap) > 0:
        print(pop_heap(heap))