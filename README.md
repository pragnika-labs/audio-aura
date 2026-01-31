# Audio Aura

Audio Aura is a personal data analytics project that explores my music listening behavior over time using a synthetic dataset inspired by Spotify listening history.

The goal of this project is not recommendation or prediction, but behavioral analysis to understand how mood, time of day, and emotional periods show up in listening patterns.

## Project Overview

Since access to the Spotify API was unavailable, I engineered my own dataset to realistically simulate my listening behavior.

Starting from a small, hand-curated list of songs with emotional attributes, I used Python to generate a time-series dataset that reflects:
- Daily routines and listening habits
- Time-of-day preferences
- Periods of emotional disruption
- Repetition and flow-state listening

This synthetic dataset is then analyzed using exploratory data analysis, clustering, and basic machine learning techniques.

## Dataset Generation

The listening data is generated using a custom Python script that simulates behavior rather than random activity.

Key aspects of the simulation include:
- A fixed timeline with realistic timestamps
- Personal sleep and activity routines
- Music-free days to reflect real-life breaks
- Probabilistic song selection based on mood and time
- An emotional disruption period that influences listening choices

The result is a Spotify-style listening history designed to resemble real user behavior.

## Analysis Highlights

The analysis notebook focuses on uncovering patterns rather than building production models.

Key insights include:
- A measurable drop in average song happiness during an emotional disruption period
- Time-of-day effects on listening mood
- Repetition and concentration around specific songs during low periods
- Identification of recurring mood-based listening personas using clustering
- Validation of cluster structure using a simple classification model

All analysis steps are documented directly inside the notebook with markdown explanations.

## Project Structure

audio-aura/
│
├── data/
│ ├── my_spotify_data.csv
│ └── spotify_data_clustered.csv
│
├── notebooks/
│ └── analysis.ipynb
│
├── scripts/
│ ├── generate_data.py
│ └── song_data.py
│
└── README.md

## Tools & Technologies

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Jupyter Notebook

## Notes

This project is intentionally personal and exploratory.  
The behaviors modeled here are based on my own routines and are not meant to generalize to other users.

## Contact

**Pragnika Mancholaa**  
Bachelor of Science in Computer Science  

Email: pragnikamancholaa@gmail.com  
LinkedIn: https://www.linkedin.com/in/pragnika-mancholaa  
Hashnode: https://pragnika.hashnode.dev
GitHub: https://github.com/pragnika-labs

