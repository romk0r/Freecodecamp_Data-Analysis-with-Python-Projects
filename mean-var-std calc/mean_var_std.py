import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError('List must contain nine numbers.')
  
  arr = np.array(list).reshape(3,3)
  d = {}

  mean_ = []
  var_  = []
  std_ = []
  max_ = []
  min_ = []
  sum_ = []

  mean_.append(np.mean(arr, axis=0).tolist())
  mean_.append(np.mean(arr, axis=1).tolist())
  mean_.append(np.mean(arr).tolist())

  var_.append(np.var(arr, axis=0).tolist())
  var_.append(np.var(arr, axis=1).tolist())
  var_.append(np.var(arr).tolist())

  std_.append(np.std(arr, axis=0).tolist())
  std_.append(np.std(arr, axis=1).tolist())
  std_.append(np.std(arr).tolist())

  max_.append(np.max(arr, axis=0).tolist())
  max_.append(np.max(arr, axis=1).tolist())
  max_.append(np.max(arr).tolist())

  min_.append(np.min(arr, axis=0).tolist())
  min_.append(np.min(arr, axis=1).tolist())
  min_.append(np.min(arr).tolist())

  sum_.append(np.sum(arr, axis=0).tolist())
  sum_.append(np.sum(arr, axis=1).tolist())
  sum_.append(np.sum(arr).tolist())

  d['mean'] = mean_
  d['variance'] = var_
  d['standard deviation'] = std_
  d['max'] = max_
  d['min'] = min_
  d['sum'] = sum_



  return d