import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

# sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

# Keras
from keras.models import Sequential
from keras.optimizers import Adam
from keras import layers


class Iris:
    # base, sklearn
    data, features, target, X, Y = None, None, None, None, None
    x_train, x_test, y_train, y_test = None, None, None, None
    y_train_oh, y_test_oh = None, None
    le = None
    scaler = None
    t_size = None  # target levels
    # Keras
    model = None
    history = None

    def __init__(self, path, target='class'):
        self.data = pd.read_csv(path)
        self.X, self.Y = self.data[self.data.columns.drop(target)], self.data[target]
        self.t_size = pd.unique(self.Y).size

    def split(self, test_size=0.2, random_state=42):
        self.x_train, self.x_test, self.y_train, self.y_test = \
            train_test_split(self.X, self.Y, test_size=test_size, random_state=random_state)
        le = LabelEncoder()  # class instance
        le.fit(self.y_train)
        self.y_train = le.transform(self.y_train)
        self.y_test = le.transform(self.y_test)
        scaler = StandardScaler()
        scaler.fit(self.x_train)
        self.x_train = scaler.transform(self.x_train)
        self.x_test = scaler.transform(self.x_test)
        return self.x_train, self.x_test, self.y_train, self.y_test


class Profile:
    history = None

    def __init__(self, history=None):
        self.history = history

    def plot0(self):

        hst = pd.DataFrame(
            {'epoch': np.arange(len(self.history.history['loss'])) + 1,
             'loss': self.history.history['loss'],
             'val_loss': self.history.history['val_loss'],
             'accuracy': self.history.history['accuracy'],
             'val_accuracy': self.history.history['val_accuracy']})
        loss, acc = hst.loc[:, ['epoch', 'loss', 'val_loss']], hst.loc[:, ['epoch', 'accuracy', 'val_accuracy']]
        loss_long = pd.melt(frame=loss, id_vars='epoch', value_vars=loss.columns[1:], var_name='measure',
                            value_name='value')
        acc_long = pd.melt(frame=acc, id_vars='epoch', value_vars=acc.columns[1:], var_name='measure',
                           value_name='value')
        fig, axes = plt.subplots(1, 2, figsize=(10, 4))
        fig.suptitle("NN")
        axes[0].set_title("Loss")
        axes[1].set_title("Accuracy")
        f1 = sb.lineplot(loss_long, x='epoch', y='value', hue='measure', ax=axes[0])
        f2 = sb.lineplot(acc_long, x='epoch', y='value', hue='measure', ax=axes[1])


    @staticmethod
    def softmax(x):
        return None

    @staticmethod
    def activations():

        def lc(x, L=1, k=1, x0=0):
            """
            logistic curve
            :param x: (-Inf, Inf)
            :param L: supremum
            :param k: logistic growth
            :param x0: midpoint
            :return:
            """
            return L/(1+np.exp(-k*(x-x0)))

        rng = pd.Series(np.arange(-8,8,.1))
        df = pd.DataFrame({'x':rng,
                           'lc': rng.apply(lambda x: lc(x, L=1, k=1, x0=0)),
                           'relu': rng.apply(lambda x: np.max((0,x))),
                           'tanh': rng.apply(lambda x: np.tanh(x)),
                           'bin': rng.apply(lambda x: 0 if x<0 else 1)
                           })
        fig, axes = plt.subplots(2,2)  # figsize=(10,8)
        fig.tight_layout(pad=3.0)
        fig.suptitle("Activation functions")
        lc_ = sb.lineplot(df, x='x', y='lc',ax=axes[0, 0],)
        lc_.set(title='Sigmoid')
        tanh_ = sb.lineplot(df, x='x', y='tanh', ax=axes[0, 1])
        tanh_.set(title='Hyperbolic tangent')
        relu_ = sb.lineplot(df, x='x', y='relu', ax=axes[1, 0])
        relu_.set(title='Rectified linear unit (ReLU)')
        bin_ = sb.lineplot(df, x='x', y='bin', ax=axes[1, 1])
        bin_.set(title='Binary step')


class KerasProfiling:
    # base, sklearn
    data, features, target, X, Y = None, None, None, None, None
    x_train, x_test, y_train, y_test = None, None, None, None
    y_train_oh, y_test_oh = None, None
    le = None
    scaler = None
    t_size = None  # target levels
    # Keras
    model = None
    history = None

    def __init__(self, path, test_size=0.2):
        iris = Iris(path)
        self.x_train, self.x_test, self.y_train, self.y_test = iris.split(test_size=test_size)
        self.standardise()
        self.onehot()

    def onehot(self):
        self.y_train_oh = np.eye(self.t_size)[self.y_train]
        self.y_test_oh = np.eye(self.t_size)[self.y_test]

    def nn(self, h_units=512, o_units=3):
        self.model = Sequential()
        self.model.add(layers.Dense(h_units, activation='relu', input_shape=(len(self.features),)))
        self.model.add(layers.Dense(o_units, activation='softmax'))
        self.model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

    def fit(self, epochs=100, batch_size=10, verbose=0):
        self.history = self.model.fit(self.x_train, self.y_train_oh,
                                      validation_data=(self.x_test, self.y_test_oh),
                                      epochs=epochs, batch_size=batch_size, verbose=verbose)
    def evaluate(self, verbose=0):
        return self.model.evaluate(self.x_test, self.y_test_oh, verbose=verbose)

