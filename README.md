# IND-Enzymes

Link to the database: https://indenzymes.srmist.edu.in/Home
Link to Article: https://link.springer.com/article/10.1007/s00792-021-01231-2

# PubMed Data Extraction and Network Generation for Thermophilic and Psychrophilic Organisms
This Python script automates the process of extracting PubMed IDs related to specific species, parsing the resulting JSON files to identify whether the organisms have thermophilic or psychrophilic characteristics, and generating a network visualization of the data.

# Prerequisites
Ensure you have the following Python libraries installed:
Biopython
xmltodict
pandas
json
networkx
matplotlib
You can install them using pip:
pip install biopython xmltodict pandas matplotlib networkx

# Usage
# Part 1: Extract PubMed IDs
Email Setup: Make sure to set your email in the script for using Entrez services:
python
Entrez.email = "your_email@example.com"
Input File: The script reads species names from ex.csv. Make sure this file contains a column named "species".
Run the script: The script will search for each species name in PubMed, extract the search results, and write them to trail1.txt.
# Part 2: Parse JSON Files
Input JSON File: The script reads from a JSON file (trail.json or psychroCGCB.json). Make sure this file contains the required structure as expected from PubMed's E-utilities.
Parsing Process: The script extracts specific fields such as "IdList", "TranslationSet", and "TranslationStack" to identify and categorize organisms based on the search results.
Output: Results are written to psychroCGCBresult.txt.
# Part 3: Network Generation
Input Files: The script reads two CSV files:
nodes.csv: Contains information about nodes such as species names, groups (thermophilic or psychrophilic), and node sizes (species count).
edges.csv: Contains information about edges including the source species, target category, and edge weight.
Network Visualization: The script generates a network graph using NetworkX, where:

Nodes represent species.
Edges connect species to thermophilic or psychrophilic categories.
Node colors and sizes represent groups and species count.
Customization:

Node colors are set using a predefined color_map.
The graph layout and appearance can be adjusted using various parameters in options.

# Outputs
Text Files:
trail1.txt: Contains PubMed search results for each species.
psychroCGCBresult.txt: Contains parsed data from JSON files.

# Network Visualization:
A network graph is displayed, showing the relationships between species and their thermophilic/psychrophilic nature.
Notes
Entrez API Usage: Make sure your email is set correctly and that you comply with NCBI’s usage policy.
Input Files: Ensure that input files (ex.csv, nodes.csv, and edges.csv) are formatted correctly to match the script’s expectations.
Network Graph: You may adjust the color_map dictionary and other network parameters to fit your visualization needs.
# Troubleshooting
Missing Modules: Install any missing modules using pip install.
File Not Found Errors: Verify that all input files are in the correct directory or provide full paths to the files.
API Limits: NCBI imposes rate limits on API requests. Ensure compliance with these limits to avoid temporary bans.
