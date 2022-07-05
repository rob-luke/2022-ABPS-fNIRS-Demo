# 2022 ABPS fNIRS Demo
Demonstrate fNIRS processing with NIRSport2 device at the Australasian Brain & Psychological Sciences Meeting 2022.

## Aim

We will take a measurement and go from raw data to average waveforms and topographic GLM results.

<img width="222" alt="image" src="https://user-images.githubusercontent.com/748691/177321932-56e5104e-e08e-4dc3-bc2c-90010fa08a85.png"> <img width="222" alt="image" src="https://user-images.githubusercontent.com/748691/177322014-e988c1c9-d8e3-4e5a-be8e-bd0023178872.png"> <img width="222" alt="image" src="https://user-images.githubusercontent.com/748691/177322079-baa98760-6813-467f-b700-880a1ac15574.png">


## Usage

The project has three components:
* `montage`: Contains the NIRSport2/Aurora files for the montage used in this demo.
* `experiment`: Contains a python script to run the example experiment,
   including sending triggers via the cedrus usb to parallel converter.
* `analysis`: Contains analysis scripts for both waveform and GLM style analysis. We will use these to kick start the conversation.


## Installation

### Running The Experiment

1. Install poetry
2. Move to the directory
   ```console
   cd /path/to/2022-ABPS-fNIRS-Demo
   ```
3. Install requirements
   ```console
   poetry install
   ```
3. Run the experiment and specify the required parameters 
   ```console
   poetry run python experiment/experiment.py  --subject Rob --session test --run 1
   ```
   
### Running The Analysis

1. Install MNE using the method recommended at https://mne.tools/stable/install/index.html
2. Run Jupyter Lab
   ```console
   jupyter lab
   ```
3. Move to the analysis directory and launch the relevant notebook
4. Change the path to your data
