# Protein folding algorithm

Course: Algorithms and Heuristics  
Case: Protein Pow(d)er  
Team: The Folding Brigade  

## Table of Contents
* [Introduction](#introduction)
* [Input](#input)
* [Prerequisites](#prerequisites)
* [Running the code](#running-the-code)

## Order of business (remove??)
1. main loads in csv
2. stores string of protein in Protein class
3. inputs Protein in Folder class
4. if a valid fold is made, store score and coordinates in Fold class
5. repeat until X number of valid folds is made
6. call Score to determine best Fold
7. save best fold to output

## Introduction
This repository contains code for the course Algoritmen en Heuristieken at the University of Amsterdam (2022-2023).
The case we worked out is Protein Pow(d)er which concerns the optimal manner of folding a Protein.

## Input
The input for the function `main.py` will be determined by a numeric value that corresponds to a protein that is stored under `data/proteins.csv`.

## Prerequisites
The modules and packages needed to run the program can be found in `requirements.txt`.
You can install these packages with the following command:
```
pip3 install -r requirements.txt
```

## Running the code
The best way to run the code is by simply using the following command:
```
python3 main.py
```
This will ask the user if he/she wants to analyse a new protein (n) or analyse existing data(e).

After choosing to evaluate existing data(e), the files scores_random.csv, scores_FRESS.csv and scores_Pruning.csv from the data map, will be used to generate a graph. 

After choosing to analyse a new protein (n), the user can see the possible proteins that you can select. If you already know which protein you wish to select beforehand, you can use the command:
```
python3 main.py [number]
```
Where [number] is any integer representing a protein.

The user can choose an algorithm in the next menu that pops up, choosing random (1), FRESS (2), Depth_first (3) or Pruning (4)

In case the user chooses random, the program needs to be provided with the number of times the algorithm should be ran.

In case the user chooses FRESS, the user will be asked to provide the number of times the algorithm should be run, and the amount of folds need to be made per elongation. 

In case the user choose Depth_first or Pruning, the user needs to clarify if a new run shouold be conducted, or the last run should be continued. Afterwards, in case of Pruning, the number of times the algorithm should run is asked. 

## Output
The output is generated in the form of the aminoacid type and the direction the next aminoacid is placed. This output can be found in the file output.csv. 

The scores found by the algorithm can be found in the file [name_algorithm].csv. 

## Experiments 
To evaluate our algorithms, we conducted experiments using different protein sequences.

For the second protein provided for this case (HHPHHHPHPHHHPH) we ran the random algorithm (10000 runs), the pruning algorithm (10000 runs), the FRESS algorithm (10000 runs and 1000 folds per elongation) the depth_first algortihm and the pruning algorithm (10000 runs).

For protein 5 and 8 provided by the case (HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH and HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH respectively) we ran the random (10000 runs), the FRESS algorithm (10000 runs and 1000 folds per elongation) and the pruning algorithm (10000 runs). 
