# Spectogram engine
Converts WAV files to spectograms (.png) and the other way.
Inspired by the [ARSS ](http://arss.sourceforge.net/) 
## Features
* Has color and brightness to depict the amplitude. (ARSS has only brightness)
* Can convert from spectogram to WAV with minimum loss in quality. (ARSS loses a lot of data)

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies.
```bash
pip install -r requirements.txt
```
## Usage
### WAV to Spectogrm
1. Drag and drop the WAV file into the **WAVFiles** folder.
2. Open the **Generate_Spectogram.py** in the **Examples** folder.
3. Set the values of **inputFolder** and **outputFolder** to their appropriate absolute paths.
4. Run it and you can find the spectogram in the output folder


### Spectogram to WAV
1.  Drag and drop the **png** file into the **Spectograms** folder.
2. Open the **Generate_WAVs.py** in the **Examples** folder
3. Set the values of **inputFolder** and **outputFolder** to their appropriate absolute paths.
4. Run it and you can find the spectogram in the output folder

## Roadmap
*  A simple UI
* Use Numba to make it faster
* Auto conversion from other audio formats to WAV.
