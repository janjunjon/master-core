from Abstract.Abstract import Abstract
import pickle

class SKLearn(Abstract):
    def __init__(self) -> None:
        super().__init__()

    def saveModel(self, model, path):
        pickle.dump(model, open(path, 'wb'))

    def loadModel(self, path):
        model = pickle.load(open(path, 'rb'))
        self.model = model
        return model

class SKLearnOnlyMethod:
    @classmethod
    def saveModel(cls, model, path):
        pickle.dump(model, open(path, 'wb'))

    @classmethod
    def loadModel(cls, path):
        model = pickle.load(open(path, 'rb'))
        return model