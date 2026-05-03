# 15-Minute City Map — Guwahati

A Python tool that visualizes whether essential services like hospitals 
and schools are reachable within a 15-minute walk from any starting 
point in Guwahati, India, using real street network data.

## What It Does

- Downloads live street network data from OpenStreetMap
- Calculates all streets reachable within 15 minutes on foot
- Overlays real hospitals and schools on the map
- Outputs an interactive map you can open in any browser

## Libraries Used

- OSMnx — downloads and models street networks
- NetworkX — runs the graph and pathfinding calculations
- GeoPandas — manages spatial data
- Folium — renders the interactive map
- Matplotlib — handles static plotting

## How to Run

1. Clone this repository
   git clone https://github.com/AVIEN0p/Urban_planning.git

2. Create a virtual environment
   python -m venv venv

3. Activate it
   venv\Scripts\activate

4. Install all libraries
   pip install -r requirements.txt

5. Run the project
   python map_test.py