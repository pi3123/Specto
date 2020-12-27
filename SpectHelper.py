from PIL import Image
from utils import *


class Turtle:
    def __init__(self,
                 minMagnitude,
                 maxMagnitude,
                 minPhase,
                 maxPhase,
                 FFT_LENGTH=1024,
                 WINDOW_LENGTH=512):
        self.FFT_LENGTH = FFT_LENGTH
        self.WINDOW_LENGTH = WINDOW_LENGTH
        self.WINDOW_STEP = int(self.WINDOW_LENGTH / 2)
        self.magnitudeMin = minMagnitude
        self.magnitudeMax = maxMagnitude
        self.phaseMin = minPhase
        self.phaseMax = maxPhase

    def genGramForWav(self, signal):
        buffer = np.zeros(int(signal.size + self.WINDOW_STEP - (signal.size % self.WINDOW_STEP)))
        buffer[0:len(signal)] = signal

        height = int(self.FFT_LENGTH / 2)
        width = int(len(buffer) / self.WINDOW_STEP - 1)

        magnitudePixels = np.zeros((height, width))
        phasePixels = np.zeros((height, width))

        for w in range(width):
            buff = np.zeros(self.FFT_LENGTH)
            stepBuff = buffer[w * self.WINDOW_STEP:w * self.WINDOW_STEP + self.WINDOW_LENGTH]

            # Hanning window
            stepBuff = stepBuff * np.hanning(self.WINDOW_LENGTH)
            buff[0:len(stepBuff)] = stepBuff

            # buff now has windowed signal with step length and padded with zeroes to the end
            fft = np.fft.rfft(buff)
            for h in range(len(fft)):
                magnitude = math.sqrt(fft[h].real ** 2 + fft[h].imag ** 2)
                if magnitude > self.magnitudeMax:
                    self.magnitudeMax = magnitude
                if magnitude < self.magnitudeMin:
                    self.magnitudeMin = magnitude

                phase = math.atan2(fft[h].imag, fft[h].real)
                if phase > self.phaseMax:
                    self.phaseMax = phase
                if phase < self.phaseMin:
                    self.phaseMin = phase
                magnitudePixels[height - h - 1, w] = magnitude
                phasePixels[height - h - 1, w] = phase
        rgbArray = genLinearScale(magnitudePixels, phasePixels,
                                  self.magnitudeMin, self.magnitudeMax, self.phaseMin, self.phaseMax)
        img = Image.fromarray(rgbArray, 'RGB')
        return img

    def genWavForGram(self, filePath):
        img = Image.open(filePath)
        data = np.array(img, dtype='uint8')
        width = data.shape[1]
        height = data.shape[0]

        magnitudeVals, phaseVals \
            = recoverLinearScale(data, self.magnitudeMin, self.magnitudeMax, self.phaseMin, self.phaseMax)
        recovered = np.zeros(self.WINDOW_LENGTH * width // 2 + self.WINDOW_STEP, dtype=np.int16)
        for w in range(width):
            toInverse = np.zeros(height, dtype=np.complex_)
            for h in range(height):
                magnitude = magnitudeVals[height - h - 1, w]
                phase = phaseVals[height - h - 1, w]
                toInverse[h] = magnitude * math.cos(phase) + (1j * magnitude * math.sin(phase))
            signal = np.fft.irfft(toInverse)
            recovered[w * self.WINDOW_STEP:w * self.WINDOW_STEP + self.WINDOW_LENGTH] += signal[
                                                                                         :self.WINDOW_LENGTH].astype(
                np.int16)
        return recovered