# Search methods

import search


ab = search.GPSProblem('A', 'B'
                       , search.romania)


print(search.branch_and_bounch_search(ab, search.Order()).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
