# 2022 ABPS fNIRS Demo
Demonstrate fNIRS processing with NIRSport2 device at the Australasian Brain & Psychological Sciences Meeting 2022.


## Usage

The project has several components:
* `montage`: Contains the NIRSport2/Aurora files for the montage used in this demo.
* `experiment`: Contains a python script to run the example experiment,
   including sending triggers via the cedrus usb to parallel converter.
* `analysis`: Contains a script to start the analysis conversation.


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