# Map Visualization with Folium

This project provides a Python script (`mapping.py`) that generates an interactive map using the Folium library. The map highlights horchaterías (specialty Spanish cafes) in a specific location and includes features for visualizing population density across countries.

## Features

1. **Horchaterías Markers**:
    - Displays markers for horchaterías using data from a CSV file (`horchaterias.txt`).
    - Markers include popups with the name of the horchatería (linked to a Google search) and its phone number.
    - Circle marker colors are determined by the last digit of the phone number:
        - Red for even numbers.
        - Green for odd numbers.

2. **Population Zones**:
    - Adds a GeoJSON layer (`world.json`) to represent population density by country:
        - Cyan for countries with a population under 10 million.
        - Blue for countries with 10–20 million.
        - Yellow for countries with over 20 million.

3. **Layer Control**:
    - Allows toggling visibility of markers and population zones on the map.

## Requirements

### Libraries
- `folium`
- `pandas`

Install the required libraries using pip:
```bash
pip install folium pandas
```

### Files
Ensure the following files are present in the working directory:
1. `horchaterias.txt` - A CSV file containing columns:
    - `Nombre`: Name of the horchatería.
    - `Latitud`: Latitude coordinates.
    - `Longitud`: Longitude coordinates.
    - `Teléfono`: Phone number.
2. `world.json` - A GeoJSON file with population data by country.

## Usage

1. Run the script:
    ```bash
    python mapping.py
    ```

2. Open the generated `Map1.html` file in a browser to interact with the map.

## Customization

### Adjusting Marker Colors
Modify the `decidir_color` function to change the logic for assigning colors based on phone numbers or other criteria.

### Adding More Layers
Add new layers using `folium.FeatureGroup` and attach them to the map with `map.add_child`.

### Data Source
Update the CSV file (`horchaterias.txt`) with new entries to include additional horchaterías.

## Example Map
The map centers on latitude 39.474416 and longitude -0.375389, with a default zoom level of 15. Markers and population zones can be toggled independently.

---

Feel free to adapt this script for other datasets or regions!

