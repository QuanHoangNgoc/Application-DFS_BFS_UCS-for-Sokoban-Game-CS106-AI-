# Introduction
- Quan Hoang Ngoc
- Assignment 1 of _TTNT_  
- _HK2_, 2024
  
### about 
- In this project, we install search algorithms such as DFS, BFS, UCS to apply them to solve the sokoban game by modeling them as a search problem. We also conduct experiments and statistics to compare algorithms as well as evaluate the difficulty of the game.
- We can model Sokoban World by a search problem and apply algorithms such as DFS, BFS, UCS to search for a solution (a path) that can win the game. In these cases, UCS appears to be the better algorithm.
- In the source code of this project, we use Python Programming Language to implement the algorithms, but the run time of programs is too long and slow (up hours). Instead of, you can use C++ as the backend of algorithms, it will significantly improve speed of algorithms based on data structure and  control structure, thus reducing the time and resources needed to experiment.

### show-off 
- [Application DFS BFS UCS for Sokoban Game - Modeling Search Problem - [AI course - CS106 - UIT]](https://youtu.be/s27dXLyyjzo?feature=shared)

# Repo Structure:  
- RESOURCES: some resources, guidelines, documents and reports of this project.
- SOURCE CODE: source code of this project.
- [Application_DFS_BFS_UCS_for_Sokoban_Game.ttnt](https://uithcm-my.sharepoint.com/:f:/g/personal/22521178_ms_uit_edu_vn/EuXhV_mF0uxJn75qkuz-FdUBuNKOyAOXv53GolTUMTuhNg?e=O6DMoV)
  - Backup this project
  - Contain submit files   

# Pipeline: 
-DFS, BFS, UCS implementation with comment lines. Installing pygame and pyautogui libraries.
- Customize and configure the source code to suitable for performing experiment. 
- Take a long time to experiment and study statistics. Experiment resources: Kaggle Colab P100 - 29GB RAM.
- Present report and pack project process. 

# How to install this project: 
- Download all source code and run file Sokoban.py to play a game. 
- If people want to change some attributes of this project to config, please change at constant.py. 
- The source code is organized as a MVC model with View is Sokoban.py and Controller is Game.py. 
- Thus, to change the algorithm that you want to use, please change at game.py >> auto_move(). 
- Customize algorithms at solver.py.
### requirements
- python >= 3.0
- pygame
- pyautogui

# Donate: 
- If this project is useful, please like (star) to add motivation for me. 
- I am happy to share my knowledge and projects to people. I am willing to spend more time, enthusiasm and a well-groomed appearance for these projects. Thank you for your help. 
