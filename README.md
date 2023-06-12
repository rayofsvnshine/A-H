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
This will show you the possible proteins that you can select. If you already know which protein you wish to select beforehand, you can use the command:
```
python3 main.py [number]
```
Where [number] is any integer representing a protein.