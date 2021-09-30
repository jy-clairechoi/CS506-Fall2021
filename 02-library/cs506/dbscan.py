from .sim import euclidean_dist

class DBC():

    def __init__(self, dataset, min_pts, epsilon):
        self.dataset = dataset
        self.min_pts = min_pts
        self.epsilon = epsilon

    def _get_epsilon_neighborhood(self, idx):
        neighborhood = []
        for i, y in enumerate(self.dataset):
            if i == idx:
                continue
            if euclidean_dist(self.dataset[idx], y) <= self.epsilon:
                neighborhood.append(i)
        return neighborhood

    def _make_bfs_assignments(self, queue, assignment, assignments):
        while queue:
            nextP = queue.pop(0)
            if assignments[nextP] != 0:
                continue
            assignments[nextP] = assignment

        return assignments


    def dbscan(self):
        """
            returns a list of assignments. The index of the
            assignment should match the index of the data point
            in the dataset.
        """
        assignments = [0 for _ in range(len(self.dataset()))]
        assignment = 1
        for i, x in enumerate(self.dataset):
            # if 
            neighborhood = self._get_epsilon_neighborhood(x)
            if len(neighborhood) >= self.min_pts:
                # explore x neighborhood for core points and give them the same assignment
                assignments[i] = assignment
                assignments = self._make_bfs_assignments(neighborhood, assignment, assignments)

        return assignments
