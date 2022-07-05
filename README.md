# 2022-ABPS-fNIRS-Demo
Demonstrate fNIRS processing with NIRSport2 device


## Installation

Due to psychopy not supporting M1 (due to PyQt5 not supporting M1)
this requires more steps than usual.

0. Ensure env variables arent set
   ```console
   unset CONDA_PREFIX
   ```
1. Install poetry
2. Initialise poetry
   ```console
   poetry install
   ```
3. Download psychopy repo
   ```console
   cd ..
   git clone xxxxxxx
   ```
3. Start up poetry shell and install remaining 
   ```console
   poetry shell
   pip install ../psychopy
   ```
   
