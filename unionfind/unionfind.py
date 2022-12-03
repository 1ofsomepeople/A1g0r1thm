class UnionFind():
  def __init__(self, ):
    self.father = {}

  # 寻找根结点
  def find(self, x):
    root = x
    while self.father[root] != root:
      root = self.father[root]
    while x != root: # 路经压缩
      x_father = self.father[x]
      self.father[x] = root
      x = x_father
    return root

  # 合并两个节点
  def merge(self, p, q):
    root_p, root_q = self.find(p), self.find(q)
    if root_p != root_q:
      self.father[root_p] = root_q

  # 判断连通性
  def is_connected(self, p, q):
    return self.find(p) == self.find(q)

  # 增加节点
  def add(self, x):
    if x not in self.father:
      self.father[x] = x
