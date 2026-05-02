import osmnx as ox
import networkx as nx
import folium
from shapely.geometry import Point

# Download the street network
place = "Guwahati, Assam, India"
graph = ox.graph_from_place(place, network_type="walk")

# Add walking time to every street edge
graph = ox.add_edge_speeds(graph)
graph = ox.add_edge_travel_times(graph)

# Pick a starting point (Paltan Bazaar, Guwahati)
start_lat = 26.1833
start_lon = 91.7458

# Find the nearest node
start_node = ox.nearest_nodes(graph, start_lon, start_lat)

# Find all nodes reachable within 15 minutes (900 seconds)
reachable_nodes = nx.ego_graph(graph, start_node, radius=900, distance="travel_time")

# Fetch amenities
hospitals = ox.features_from_place(place, tags={"amenity": "hospital"})
schools = ox.features_from_place(place, tags={"amenity": "school"})

# Create interactive folium map centered on starting point
m = folium.Map(location=[start_lat, start_lon], zoom_start=14)

# Add starting point marker
folium.Marker(
    location=[start_lat, start_lon],
    popup="Starting Point - Paltan Bazaar",
    icon=folium.Icon(color="red", icon="home")
).add_to(m)

# Plot reachable streets
for u, v, data in reachable_nodes.edges(data=True):
    if "geometry" in data:
        coords = [(lat, lon) for lon, lat in data["geometry"].coords]
        folium.PolyLine(coords, color="red", weight=2, opacity=0.7).add_to(m)

# Add hospital markers
for _, row in hospitals.iterrows():
    if row.geometry.geom_type == "Point":
        folium.Marker(
            location=[row.geometry.y, row.geometry.x],
            popup=row.get("name", "Hospital"),
            icon=folium.Icon(color="blue", icon="plus-sign")
        ).add_to(m)

# Add school markers
for _, row in schools.iterrows():
    if row.geometry.geom_type == "Point":
        folium.Marker(
            location=[row.geometry.y, row.geometry.x],
            popup=row.get("name", "School"),
            icon=folium.Icon(color="green", icon="book")
        ).add_to(m)

# Save as an HTML file you can open in any browser
m.save("15min_city_map.html")
print("Map saved! Open 15min_city_map.html in your browser")