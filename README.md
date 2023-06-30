# Protein folding algorithm

Course: Algorithms and Heuristics  
Case: Protein Pow(d)er  
Team: The Folding Brigade  

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Input](#input)
- [Running the code](#running-the-code)
- [Output](#output)
- [Experiments](#experiments)


## Introduction
This repository contains code for the course Algoritmen en Heuristieken at the University of Amsterdam (2022-2023).
The case we worked out is Protein Pow(d)er which concerns the optimal manner of folding a Protein.

## Prerequisites
The modules and packages needed to run the program can be found in `requirements.txt`.
You can install these packages with the following command:
```
pip3 install -r requirements.txt
```

## Input
The input for the function `main.py` will be determined by a numeric value that corresponds to a protein that is stored under `data/proteins.csv`.

## Running the code
The best way to run the code is by simply using the following command:
```
python3 main.py
```
This will ask the user if they want to analyse a new protein (n) or analyse existing data(e).

After choosing to evaluate **existing data (e)**, the files `scores_random.csv`, `scores_FRESS.csv` and `scores_Greedy.csv` from the data map, will be used to generate a graph. 

After choosing to analyse a **new protein (n)**, the user can see the possible proteins that you can select. If you already know which protein you wish to select beforehand, you can use the command:
```
python3 main.py [number]
```
Where [number] is any integer representing a protein.

The user can choose an algorithm in the next menu that pops up, choosing **Random (1), FRESS (2), Depth first (3)** or **Greedy (4)**

In case the user chooses **random**, the program needs to be provided with the number of times the algorithm should be ran.

In case the user chooses **FRESS**, the user will be asked to provide the number of times the algorithm should be run, and the amount of folds that need to be made per elongation. 

In case the user chooses **Depth_first** or **Greedy**, the user needs to clarify if a new run should be initiated, or the last run should be continued. In case of Greedy, the number of times the algorithm should run is also asked. 

## Output
The output is generated in the form of the aminoacid type and the direction in which the next aminoacid is placed. This output can be found in the file `output.csv`. 

The scores found by the algorithm can be found in the file `[name_algorithm].csv`. The csv files created can be used for further analysis when the user chooses **analyse existing data (e)**, and all `score_*.csv` files are given as input (with the same protein and parameters). 

## Experiments 
To evaluate our algorithms, we conducted experiments using different protein sequences.

For the second protein provided for this case (HHPHHHPHPHHHPH) we ran the random algorithm (10000 runs), the greedy algorithm (10000 runs), the FRESS algorithm (10000 runs and 1000 folds per elongation) and the depth_first algortihm (1 run).

For protein 5 provided by the case (HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH) we ran the random (10000 runs) and the FRESS algorithm (10000 runs and 1000 folds per elongation). Greedy took much longer to run and thus could not be run for this protein, nor number 8.

For protein 8 provided for this case (HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH) we ran the random (1000 runs) and FRESS algorithm (1000 runs and 1000 folds per elongation). Because of time constraints we could not run the 10000 runs we wanted, but 1000 runs gives an indication of the distribution. 
