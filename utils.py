import math
import numpy as np
from numba import njit, prange


@njit(fastmath=True)
def amplifyMagByLog(d):
    return 188.301 * math.log10(d + 1)


@njit(fastmath=True)
def weakenAmplifiedMag(d):
    return math.pow(10, d / 188.301) - 1


@njit(parallel=True, nogil=True)
def genLinearScale(magnitudePixels, phasePixels,
                   magnitudeMin, magnitudeMax, phaseMin, phaseMax):
    height = magnitudePixels.shape[0]
    width = magnitudePixels.shape[1]
    magnitudeRange = magnitudeMax - magnitudeMin
    phaseRange = phaseMax - phaseMin
    rgbArray = np.zeros((height, width, 3), 'uint8')

    for w in prange(width):
        for h in range(height):
            magnitudePixels[h, w] = (magnitudePixels[h, w] - magnitudeMin) / magnitudeRange * 255 * 2
            magnitudePixels[h, w] = amplifyMagByLog(magnitudePixels[h, w])
            phasePixels[h, w] = (phasePixels[h, w] - phaseMin) / phaseRange * 255
            red = 255 if magnitudePixels[h, w] > 255 else magnitudePixels[h, w]
            green = (magnitudePixels[h, w] - 255) if magnitudePixels[h, w] > 255 else 0
            blue = phasePixels[h, w]
            rgbArray[h, w, 0] = int(red)
            rgbArray[h, w, 1] = int(green)
            rgbArray[h, w, 2] = int(blue)
    return rgbArray


@njit(parallel=True, nogil=True)
def recoverLinearScale(rgbArray, magnitudeMin, magnitudeMax,
                       phaseMin, phaseMax):
    width = rgbArray.shape[1]
    height = rgbArray.shape[0]
    magnitudeVals = rgbArray[:, :, 0].astype(np.float64) + rgbArray[:, :, 1].astype(np.float64)
    phaseVals = rgbArray[:, :, 2].astype(np.float64)
    phaseRange = phaseMax - phaseMin
    magnitudeRange = magnitudeMax - magnitudeMin
    for w in prange(width):
        for h in range(height):
            phaseVals[h, w] = (phaseVals[h, w] / 255 * phaseRange) + phaseMin
            magnitudeVals[h, w] = weakenAmplifiedMag(magnitudeVals[h, w])
            magnitudeVals[h, w] = (magnitudeVals[h, w] / (255 * 2) * magnitudeRange) + magnitudeMin
    return magnitudeVals, phaseVals
