from collections import defaultdict


MOD = 998244353


def extgcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x, y = extgcd(b, a % b)
    return (g, y, x - a // b * y)


def modinv(a, mod):
    return extgcd(a, mod)[1]


# 1 / M
M = 10
minv = modinv(M, MOD)
ans = 2 ** 30
ans = (ans * minv) % MOD


class UnionFind():
    '''
    Union Find
    n : int, the number of nodes
    root : list, list of parents.
        If value is negative, the index is a root node number of a tree/group, and
        the absolute value is the number of nodes in the tree.
    rank : list, height of the tree
    '''

    def __init__(self, n):
        self.n = n
        self.root = [-1] * (n + 1)
        self.rank = [0] * (n + 1)

    def find(self, x):
        '''
        Find root of node x.
        x : int, node number
        '''
        if (self.root[x] < 0):
            return x

        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def unite(self, x, y):
        '''
        Unite trees.
        x : int, node number in one tree
        y : int, node number in another tree
        '''
        x = self.find(x)
        y = self.find(y)

        if (x == y):
            return
        elif (self.rank[x] > self.rank[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if (self.rank[x] == self.rank[y]):
                self.rank[y] += 1

    def is_same(self, x, y):
        '''
        Check if it's in the same tree.
        x : int, one node number
        y : int, another node number
        '''
        return self.find(x) == self.find(y)

    def get_tree_size(self, x):
        '''
        Get the tree size.
        x : int, node number
        '''
        return -self.root[self.find(x)]

    def get_roots(self):
        '''
        Get a list of the roots.
        '''
        return [i for i, x in enumerate(self.root) if x < 0]

    def get_number_of_group(self):
        '''
        Get the number of trees/groups.
        '''
        return len(self.get_roots())

    def get_all_group_members(self):
        '''
        Get all lists of nodes for all trees/groups.
        '''
        # K: root, V: list of nodes
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
