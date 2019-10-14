from chainer import Chain
import chainer.functions as F
import chainer.links as L


class MLP(Chain):
    def __init__(self):
        super(MLP, self).__init__()
        with self.init_scope():
            self.l1 = L.Linear(784, 100)
            self.l2 = L.Linear(100, 100)
            self.l3 = L.Linear(100, 10)

    def forward(self, x):
        h1 = F.relu(self.l1(x))
        h2 = F.relu(self.l2(h1))
        y = self.l3(h2)
        return y
