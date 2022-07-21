import math

class UnionFind:
    '''UnionFind
    
    Attributes
    ----------
    par_: list of int
        ノードの根
        parent of node
    rank_: list of int
        ノードのランク、長さ
        rank of node
    '''
    par_ = None
    rank_ = None

    def __init__(self, n=6*10**5+3):
        '''
        Parameters
        ----------
        n: int, default 6*10**5+3
            number of nodes
        '''
        self.par_ = list(range(n))
        self.rank_ = [0] * n

    def root(self, x):
        if x == self.par_[x]:
            return x
        return self.root(self.par_[x])

    def rank(self, x):
        return self.rank_[x]

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)
        rank_x = self.rank(x)
        rank_y = self.rank(y)
        if x != y:
            if rank_x == rank_y:
                self.rank_[x] += 1
                self.par_[y] = x
            elif rank_x > rank_y:
                self.par_[y] = x
            else:
                self.par_[x] = y

class SegTree:
    from operator import add
    '''SegmentTree
    
    Attributes
    ----------
    nodes: list of int or float
    monoid: int or float
        単位元, Monoid
    nodes_length: int
        objectの長さ以上の最小の2^k-1
        The smallest 2^k-1 over the length of object
    seg_func: function
    '''
    nodes = None
    monoid = None
    nodes_length = None
    seg_func = None

    def __init__(self, object, *, monoid=0, seg_func=add):
        '''
        Parameters
        ----------
        object: array_like
            
        monoid: int or float default 0
            単位元, Monoid
        seg_func: function default operator.add
            セグ木にて用いる関数
            Function used in SegTree
        '''
        bin_n = bin(len(object))[2:]
        sum_bin_n = sum(int(i) for i in bin_n)
        if sum_bin_n == 1:
            cnt_nodes = 2**(len(bin_n) - 1)
        else:
            cnt_nodes = 2**len(bin_n)

        self.monoid = monoid
        self.nodes_length = 2*cnt_nodes - 1
        self.seg_func = seg_func
        self.nodes = [monoid] * (2*cnt_nodes - 1)
        
        for i, v in enumerate(object):
            self.update(i, v)
            self.eval(i)

    def get_node_idx(self, node):
        '''get node_idx in SegTree
        Parameters
        ----------
        node: int
            objectにおけるnodeのインデックス
            Index of node in object
        Returns
        -------
        node_idx: int
            node_idx in SegTree
        '''
        node_idx = self.nodes_length//2 + node
        return node_idx
    
    def update(self, node, val):
        '''
        Parameters
        ----------
        node: int
            objectにおけるnodeのインデックス
            Index of node in object
        val: int or float
            変えたい値
            Value to replace
        '''
        node_idx = self.get_node_idx(node)
        self.nodes[node_idx] = val

    def eval(self, node):
        '''
        Parameters
        ----------
        node: int
            objectにおけるnodeのインデックス
            Index of node in object
        '''
        node_idx = self.get_node_idx(node)
        while node_idx > 0:
            node_idx = math.ceil(node_idx/2) - 1
            self.nodes[node_idx] = self.seg_func(
                self.nodes[node_idx*2 + 1],
                self.nodes[node_idx*2 + 2]
            )

    def _get(self, query_left, query_right, _node_idx=0, _layer_left=0, _depth=1):
        '''
        Notes
        -----
        Don't change _node_idx, _layer_left, _depth
        '''
        cnt_layer_nodes = (self.nodes_length + 1) // (2**_depth)
        layer_right = _layer_left + cnt_layer_nodes - 1

        if _layer_left > query_right or layer_right < query_left:
            return self.monoid
        
        elif _layer_left >= query_left and layer_right <= query_right:
            return self.nodes[_node_idx]
        
        else:
            val_left = self._get(query_left, query_right, _node_idx*2+1, _layer_left, _depth+1)
            val_right = self._get(query_left, query_right, _node_idx*2+2, _layer_left + cnt_layer_nodes//2, _depth+1)
            return self.seg_func(val_right, val_left)
    
    def get(self, query_left, query_right):
        '''
        Returns
        -------
        self._get(query_left, query_right): int or float
            閉区間[query_left, query_right]の値
            Value of closed section[query_left, query_right]
        '''
        if query_right == -1:
            query_right = (self.nodes_length + 1) // 2
        return self._get(query_left, query_right)








