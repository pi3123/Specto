
# Spectogram engine
Converts WAV files to spectograms (.png) and the other way.
Inspired by the [ARSS ](http://arss.sourceforge.net/) 
## Features
* Has color and brightness to depict the amplitude. (ARSS has only brightness)
* Can convert from spectogram to WAV with minimum loss in quality. (ARSS loses a lot of data)

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies.
```bash
pip install Specto
```
## Usage
### WAV to Spectogrm
```python
# Loading the worker
turtle = Turtle(minMagnitude=0.004416916563059203,     # Minimum frequency
		maxMagnitude=2026134.8514368106,       # Maximum Frequency
		minPhase=-math.pi,
		maxPhase=math.pi)
				
rate, audData  =  scipy.io.wavfile.read(WAV_FILE_NAME) # Reading the Audio file
audData  =  audData.sum(axis=1) /  2                   # combining 2 channels to one
img = turtle.genGramForWav(audData)                    # Generating the img
img.save(OUTPUT_FILE_NAME, "PNG")                      # saving the img
```


### Spectogram to WAV
```python
# Loading the worker
turtle = Turtle(minMagnitude=0.004416916563059203,     # Minimum frequency
		maxMagnitude=2026134.8514368106,       # Maximum Frequency
		minPhase=-math.pi,
		maxPhase=math.pi)
				
rec  =  turtle.genWavForGram(WAV_FILE_NAME)            # Generating the WAV
scipy.io.wavfile.write(OUTPUT_FILE_NAME, 44100, rec)   # Saving the WAV file 
```


## Roadmap
*  A simple UI
* Use Numba to make it faster
* Auto conversion from other audio formats to WAV.
