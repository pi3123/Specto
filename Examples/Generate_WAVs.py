import os
import math
import scipy.io.wavfile

from tqdm import tqdm
from SpectHelper import Turtle

inputFolder = "X:/Projects/Specto/Spectograms/"
outputFolder = "X:/Projects/Specto/WAVFiles/recovered/"

# Getting file names from the input folder
array = []
for file in os.listdir(inputFolder):
    if file.endswith(".png"):
        array.append(file)

# Loading the worker
turtle = Turtle(minMagnitude=0.004416916563059203,
                maxMagnitude=2026134.8514368106,
                minPhase=-math.pi,
                maxPhase=math.pi)

# Generating spectograms
for file in tqdm(array, desc="Generating WAV files"):
    inputName = inputFolder + file
    outputName = outputFolder + file.replace('.png', '.wav')  # Making fname
    rec = turtle.genWavForGram(inputName)
    scipy.io.wavfile.write(outputName, 44100, rec)
