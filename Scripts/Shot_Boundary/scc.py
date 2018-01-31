
def strongly_connected_components_tree(vertices, edges):
    """
    Find the strongly connected components of a directed graph.

    Uses a recursive linear-time algorithm described by Tarjan [2]_ to find all
    strongly connected components of a directed graph.

    Parameters
    ----------
    vertices : iterable
        A sequence or other iterable of vertices.  Each vertex should be
        hashable.

    edges : mapping
        Dictionary (or mapping) that maps each vertex v to an iterable of the
        vertices w that are linked to v by a directed edge (v, w).

    Returns
    -------
    components : iterator
        An iterator that yields sets of vertices.  Each set produced gives the
        vertices of one strongly connected component.

    Raises
    ------
    RuntimeError
        If the graph is deep enough that the algorithm exceeds Python's
        recursion limit.

    Notes
    -----
    The algorithm has running time proportional to the total number of vertices
    and edges.  It's practical to use this algorithm on graphs with hundreds of
    thousands of vertices and edges.

    The algorithm is recursive.  Deep graphs may cause Python to exceed its
    recursion limit.

    `vertices` will be iterated over exactly once, and `edges[v]` will be
    iterated over exactly once for each vertex `v`.  `edges[v]` is permitted to
    specify the same vertex multiple times, and it's permissible for `edges[v]`
    to include `v` itself.  (In graph-theoretic terms, loops and multiple edges
    are permitted.)

    References
    ----------
    .. [1] Harold N. Gabow, "Path-based depth-first search for strong and
       biconnected components," Inf. Process. Lett. 74 (2000) 107--114.

    .. [2] Robert E. Tarjan, "Depth-first search and linear graph algorithms,"
       SIAM J.Comput. 1 (2) (1972) 146--160.

    Examples
    --------
    Example from Gabow's paper [1]_.

    >>> vertices = [1, 2, 3, 4, 5, 6]
    >>> edges = {1: [2, 3], 2: [3, 4], 3: [], 4: [3, 5], 5: [2, 6], 6: [3, 4]}
    >>> for scc in strongly_connected_components_tree(vertices, edges):
    ...     print(scc)
    ...
    set([3])
    set([2, 4, 5, 6])
    set([1])

    Example from Tarjan's paper [2]_.

    >>> vertices = [1, 2, 3, 4, 5, 6, 7, 8]
    >>> edges = {1: [2], 2: [3, 8], 3: [4, 7], 4: [5],
    ...          5: [3, 6], 6: [], 7: [4, 6], 8: [1, 7]}
    >>> for scc in  strongly_connected_components_tree(vertices, edges):
    ...     print(scc)
    ...
    set([6])
    set([3, 4, 5, 7])
    set([8, 1, 2])

    """
    identified = set()
    stack = []
    index = {}
    lowlink = {}

    def dfs(v):
        index[v] = len(stack)
        stack.append(v)
        lowlink[v] = index[v]

        for w in edges[v]:
            if w not in index:
                # For Python >= 3.3, replace with "yield from dfs(w)"
                for scc in dfs(w):
                    yield scc
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif w not in identified:
                lowlink[v] = min(lowlink[v], lowlink[w])

        if lowlink[v] == index[v]:
            scc = set(stack[index[v]:])
            del stack[index[v]:]
            identified.update(scc)
            yield scc

    for v in vertices:
        if v not in index:
            # For Python >= 3.3, replace with "yield from dfs(v)"
            for scc in dfs(v):
                yield scc