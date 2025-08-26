import numpy as np
from PowerMethod import RayleighQuotientIteration
from typing import List


class PageRank:
    def __init__(self, page_num, damping_factor=0.85):
        self.page_num = page_num
        self.damping_factor = damping_factor
        self.damping_matrix = (1 - damping_factor) * np.full(
            (page_num, page_num), 1 / page_num
        )
        self.original_vec = np.full(page_num, 1 / page_num)
        self.connection_matrix = np.zeros((page_num, page_num))

    def add_connection_list(self, page_ind1: int, page_indlist: List[int]):
        if page_ind1 >= self.page_num or page_ind1 < 0:
            raise ValueError("Must be a page number between 0 and page_num-1")
        for node in page_indlist:
            if node >= self.page_num or node < 0:
                raise ValueError("Must be a page number between 0 and page_num-1")
            if self.connection_matrix[node, page_ind1] == 0:
                self.connection_matrix[node, page_ind1] = 1

    def add_connection(self, page_ind1: int, page_ind2: int):
        if (
            page_ind1 >= self.page_num
            or page_ind1 < 0
            or page_ind2 < 0
            or page_ind2 >= self.page_num
        ):
            raise ValueError("Must be a page number between 0 and page_num-1")
        if self.connection_matrix[page_ind2, page_ind1] == 0:
            self.connection_matrix[page_ind2, page_ind1] = 1
        else:
            print("Edge has already been found inside connecting the two nodes")

    def score(self):
        new_matr = (
            self.damping_factor
            * (self.connection_matrix / self.connection_matrix.sum(axis=0))
            + self.damping_matrix
        )
        vec = RayleighQuotientIteration(new_matr, self.original_vec, 100)[1]
        return vec / np.sum(vec)

# Quick Page Rank Tests

Google = PageRank(4)

Google.add_connection_list(0, [1, 2, 3])
Google.add_connection_list(1, [2, 3])
Google.add_connection_list(2, [0])
Google.add_connection_list(3, [0, 2])

print(Google.score())
