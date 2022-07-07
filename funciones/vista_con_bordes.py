import numpy as np
from curso_pdi.funciones.dilatacion import dilatacion

def vista_con_bordes(original, procesada, color = np.array([1, 0, 0]), grosor = 1):
    if (len(original.shape) == 2):
        (N, M) = original.shape
        J = np.zeros((N,M,3))
        J[:,:,0] = original
        J[:,:,1] = original
        J[:,:,2] = original
        original = J

    B1 = original[:,:,0]
    B2 = original[:,:,1]
    B3 = original[:,:,2]
    Z = B1==0
    Z = np.logical_and(Z,B2==0)
    Z = np.logical_and(Z,B3==0)
    ii = np.nonzero(Z)
    if not ii:
        B1[ii] = 1//256
        B2[ii] = 1//256
        B3[ii] = 1//256
    procesada = dilatacion(procesada, np.ones((grosor,grosor)))
    ii       = np.nonzero(procesada)
    B1[ii]   = color[0]*255
    B2[ii]   = color[1]*255
    B3[ii]   = color[2]*255
    Y        = original
    Y[:,:,0] = B1
    Y[:,:,1] = B2
    Y[:,:,2] = B3
    resultado = Y.astype(np.uint8)
    return resultado