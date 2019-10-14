import chainer
import numpy as np

from model import MLP


class PredictionService:
    model = MLP()
    chainer.serializers.load_npz("model.npz", model)

    @staticmethod
    def predict(x: np.ndarray):
        with chainer.using_config("train", False):
            p = PredictionService.model(x[np.newaxis, ...])[0].array.argmax()
        return p
