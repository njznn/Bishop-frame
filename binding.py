import numpy as np
import ctypes as C

def tomat(vec):
  mat = np.zeros((3, int(len(vec)/3)))
  for k in range(len(vec)):
    j = k // 3
    i = k % 3
    mat[i, j] = vec[k]
  return mat

def tovec(mat):
 return mat.reshape((mat.shape[0] * mat.shape[1]), order='F')

def calcincpp(mat, initvec):
    mat = mat.transpose()
    st_tock = mat.shape[1]
    a = tovec(mat).astype('float64')
    initvec = np.array(initvec).astype('float64')
    # Load the shared object file
    lib = C.CDLL('bishoplib/build/libbishoplib.so.1.0.1')


    f_run = lib.run
    f_run.argtypes = [np.ctypeslib.ndpointer(dtype = np.float64), np.ctypeslib.ndpointer(dtype = np.float64),C.c_int]
    f_run.restype = np.ctypeslib.ndpointer(dtype = np.float64, shape=(4*len(a)-9,))
    y = f_run(a, initvec, st_tock)
    
    return(tomat(y))
    
