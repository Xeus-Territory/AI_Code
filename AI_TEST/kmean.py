import numpy as np

class Kmean(object):
    def __init__(self, k, data, max_iter = 10):
        self.cluster = k
        self.iter = max_iter
        self.data = np.array(data)
        self.centroids, self.idx = self.find_k_means(self.data, self.cluster, self.iter)

    def initialize_K_centroid(self, X, K):
        m, n = X.shape
        k_rand = np.ones((K, n))
        k_rand = X[np.random.choice(range(len(X)), K, replace=False),:]
        return k_rand
    
    def find_closest_centroid(self, X, centroids):
        m = len(X)
        c = np.zeros(m)
        for i in range(m):
            distances = np.linalg.norm(X[i] - centroids, axis=1)
            c[i] = np.argmin(distances)
        return c
    
    def compute_means(self, X, idx, K):
        m, n = X.shape
        centroids = np.zeros((K, n))
        for k in range(K):
            points_belong_k = X[np.where(idx == k)]
            centroids[k] = np.mean(points_belong_k, axis=0,)
        return centroids
    
    def find_k_means(self, X, K, max_iters=10):
        _, n = X.shape
        centroids = self.initialize_K_centroid(X, K) 
        centroid_history = np.zeros((max_iters, K, n))
        for i in range(max_iters):
            idx = self.find_closest_centroid(X, centroids)
            centroids = self.compute_means(X, idx, K)
        
        return centroids, idx 
    
kmean = Kmean(2, [[0, 3], [1, 4], [2, 0], [3, 0]])
print("Tam cac cum: ", kmean.centroids)
print("Cac diem phan cum theo nhom: ", kmean.idx)