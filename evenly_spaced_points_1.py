

N_SELECT = 4
data = [0.0, 1.0, 2.0, 3.0, 4.0, 100.0]
mean = (data[-1] - data[0]) / float(N_SELECT-1)
def weightOfEdge(i, j):
    return (abs(data[i] - data[j]) - mean) ** 2
    
def getMin(dist, j):
    min_ = dist[0] + weightOfEdge(0, j)
    index = 0
    for i in range(j):
        if min_ > dist[i] + weightOfEdge(i, j):
            min_ = dist[i] + weightOfEdge(i, j)
            index = i
    return min_, index

def evenlyDistributed(N, points):
    if N > len(points):
        print('ERROR: number of points to select (N) exceeds number of data points')
        return 
    if N == 1:
        if len(points) == 0:
            print('ERROR: no input data')
            return
        elif len(points) == 1:
            return points
        else:
            print('ERROR: Must select >= 2 values')
            return 
    
    if N == 2:
        return [arr[0], arr[-1]]
     
    if N > 2:
        dist = [[]] * N
        dist[0] = [0.0] + [float('inf')] * (len(points) - 1)
        
        path = [[]] * N
        path[0] = points

        for k in range(1, N):
            dist[k] = [float('inf')] * len(points)
            path[k] = [[]] * len(points)
            
            for j in range(0, len(points)):          
                if j >= k and j < len(points) + k - N + 1:
                    m, index = getMin(dist[k-1], j)
                    dist[k][j] = m
                    if k == 1:
                        path[k][j] = [points[index], points[j]]
                    else:
                        path[k][j] = path[k-1][index] + [points[j]]
                    
          
        for line in dist:
            print(line)
        print('-----------')
        for line in path:
            print(line)
        print('---------------')
        return path[N-1][len(points) - 1]
    
    
result = evenlyDistributed(N_SELECT, data)
print(result)

                    

                
                        
            