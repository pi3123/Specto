import os
import math
import scipy.io.wavfile

from tqdm import tqdm
from SpectHelper import Turtle

inputFolder = "../Specto/WAVFiles/"
outputFolder = "../Specto/Spectograms/"

# Getting file names from the input folder
array = []
for file in os.listdir(inputFolder):
    if file.endswith(".wav"):
        array.append(file)

# Loading the worker
turtle = Turtle(minMagnitude=0.004416916563059203,
                maxMagnitude=2026134.8514368106,
                minPhase=-math.pi,
                maxPhase=math.pi)

# Generating spectograms
for file in tqdm(array, desc="Generating spectograms"):
    inputName = inputFolder + file
    outputName = outputFolder + file.replace(inputFolder, '').replace('.wav', '.png')  # Making fname
    rate, audData = scipy.io.wavfile.read(inputName)  # Reading the Audio file
    audData = audData.sum(axis=1) / 2  # combining 2 channels to one
    img = turtle.genGramForWav(audData)  # Generating the img
    img.save(outputName, "PNG")  # saving the img
