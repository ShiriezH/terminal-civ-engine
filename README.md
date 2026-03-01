🏛 Terminal Civilization Engine

A modular, turn-based civilization simulation engine built in Python.
The engine procedurally generates a world map, spawns AI-controlled factions, and simulates territorial expansion, resource accumulation, and combat until a single faction achieves total dominance.
Each simulation run produces a unique world and emergent faction behavior.

## 📌 Overview
Terminal Civilization Engine is a grid-based strategy simulation designed to demonstrate:

- Object-oriented architecture
- Procedural world generation
- AI-driven expansion logic
- Turn-based simulation systems
- Combat resolution mechanics
- Resource economy modeling
- CLI configuration handling
- Clean Git workflow and modular design

## 🎯 Goals

- Demonstrate system design
- Practice algorithms and data structures
- Implement a clean modular architecture
- Follow professional Git workflow

## ⚙️ Features

- Weighted procedural terrain generation
- Object-based Tile system
- AI-controlled factions
- Territory expansion algorithm
- Combat resolution system
- Resource accumulation per turn
- Turn-based simulation loop
- CLI map size configuration (--size)
- Victory detection & automatic termination
- Turn statistics dashboard

## 🧠 How It Works
## 🌍 World Generation

- A square grid map is generated.

- Terrain types use weighted probabilities:

 - `~` Water

 - `.` Plains

 - `F` Forest

 - `^` Mountain

- Each tile is represented by a Tile object for extensibility.

## 🏰 Faction System

- Two AI factions spawn on random non-water tiles.
- Each faction:

 - Tracks owned tiles

 - Collects resources based on terrain

 - Expands into adjacent territory each turn

## ⚔ Combat System
When factions attempt to claim the same territory:

- Combat strength = tile count + random factor

- The stronger faction claims the tile

- The weaker faction loses control

## 🏆 Victory Condition
The simulation ends automatically when one faction controls all non-water tiles.

## 🏗 Project Structure
```
terminal-civ-engine/
│
├── main.py              # Entry point + CLI handling
├── requirements.txt     # Project dependencies
│
├── world/
│   ├── map.py           # Core simulation engine
│   └── tile.py          # Tile data model
│
├── entities/
│   └── faction.py       # Faction logic
│
└── README.md  
```

## 🚀 How to Run
1️⃣ Clone the Repository

git clone https://github.com/ShiriezH/terminal-civ-engine.git
cd terminal-civ-engine

2️⃣ Create a Virtual Environment

python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run the Simulation
Default 10x10 map:

python main.py

Custom map size:

python main.py --size 15

## 📈 Future Improvements

- Smarter AI expansion strategy
- Resource-weighted combat scaling
- Multiple factions (3–5 factions)
- Save/load simulation state
- Interactive player mode
- GUI version of the engine

## 🏁 Project Purpose
This project was developed as a structured systems design exercise (20–40 hours) focused on:

- Building a non-trivial simulation from scratch
- Designing scalable, modular architecture
- Practicing professional Git workflows
- Creating recruiter-ready portfolio material
