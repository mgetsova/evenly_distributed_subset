import numpy as np

N_SELECT = 4
data = [0.0, 1.0, 2.0, 3.0, 4.0, 100.0]

'''
program to compute the N most evenly distributed points from an ordered set of 
floats. For N = 2, we always pick the endpoints. 

The metric optimized for is
the minimum variance of the distance between each consecutive pair of the 
choosen points. 

By defining the weight of a pair of consecutive points as the
corresponding value in the numerator of the variance (eg. for 0 and 1 above,
the weight of the 'edge' from 0 to 1 would be ((1- 0) - mean) ^ 2) and the mean
as the difference between the endpoints divided by the number of intervals between
consecutive points in the chosen set (N -1), we can map the problem to finding
the minimum weight path from the left endpoint to the right endpoint having 
N - 1 edges in a graph representing all possible directed paths betweeen the 
endpoints.
'''

    
def getMin(dist, j, mean, arr):
    ''' 
    Given a set of path weights to points occuring prior to j,
    a point j (where j is the index of the point in the input data array, arr),
    and the mean value as described above, this function returns the minimum
    weight path to the point arr[j] and the index of the previously constructed
    path to which j was most optimally appended.
    '''
    deltas = np.power((arr[0:j] - arr[j]) - mean, 2)
    dists_to_j = dist[0:j] + deltas
    index = np.argmin(dists_to_j)
    return dists_to_j[index], index

def evenlyDistributed(N, arr):
    '''
    Given a sorted array of floats, arr of length M and an integer N <= M, 
    this function returns the set of N most evenly distributed points in arr. 
    The function uses a dynamic programming approach to solve the problem by 
    iteratively computing the weights of paths of length k to all reachable
    points from a current point j and storing the minimum weight and path in
    the N x M dist and path matricies, respectively. 
    '''

    points = np.asarray(arr)
    mean = (points[0] - points[-1]) / float(N - 1)
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
        return [points[0], points[-1]]
     
    if N > 2:
        ''' dist[k][j] = the minimum weight found for a path having k edges
        from the leftmost endpoint to the point at arr/points[j]'''
        dist = np.empty((N, len(points)), float)
        dist[0] = [0.0] + [float('inf')] * (len(points) - 1)
        
        ''' path[k][j] = the corresponding set of points along the path '''
        path = np.empty((N, len(points)), list)
        path[0] = points

        for k in range(1, N):
            dist[k] = [float('inf')] * len(points)      
            for j in range(0, len(points)):          
                if j >= k and j < len(points) + k - N + 1:
                    m, index = getMin(dist[k-1], j, mean, points)
                    dist[k][j] = m
                    if k == 1:
                        path[k][j] = [points[index], points[j]]
                    else:
                        path[k][j] = path[k-1][index] + [points[j]]
                    
          
        return path[N-1][len(points) - 1]
    
    
result = evenlyDistributed(N_SELECT, data)
print(result)

                    

                