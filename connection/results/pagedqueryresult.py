from typing import List


class PagedQueryResult:
    offset: int
    limit: int
    count: int
    total: int
    results: List
    # facets - Object containing FacetResults - Optional

    def __init__(self, offset: int, limit: int, count: int, total: int, results: List, facets=None):
        self.offset = offset
        self.limit = limit
        self.count = count
        self.total = total
        self.results = results
        self.facets = facets

    def __str__(self):
        return vars(self).__str__()
