from dataclasses import dataclass

@dataclass
class ModelConfig:
  # data parameters
  blockSize: int = None # context size or the num of chars for each input
  vocabSize: int = None # the domain of input ints, i.e. [0, ..., vocabSize -1]

  # model parameters
  n_layers: int = 4 # number of hidden layers in model
  embed_dim: int = 64 # the embed dimension

