# Audio Aura

## What is Audio Aura?

Audio Aura is a personal analytics project where I explored my own music listening behavior through data.

Using a small, hand-curated list of songs and custom behavioral rules, I simulated a Spotify-style listening history that reflects how I actually listen to music across different times of the day, routines, and emotional states.

The goal of this project was not to predict songs, but to understand patterns in my behavior and see how mood, time, and life events show up in listening habits.

## Why I Built This Project

I originally wanted to analyze my actual Spotify listening data, but access to the Spotify API was unavailable at the time.

Instead of dropping the idea, I decided to build the dataset myself. I treated this as an opportunity to design a realistic simulation of my listening behavior based on how I actually consume music throughout the day and across different emotional states. 

This project is personal by design. Rather than analyzing a generic dataset, I wanted to study patterns that reflect real routines, habits, and life events.

## How the Data Was Created

Since this project could not rely on real Spotify data, I generated a synthetic listening dataset designed to closely mirror my actual listening behavior.

I started with a small, hand-curated list of 60 songs. Each song was assigned two core attributes:
- **Valence**, representing how happy or sad the song feels
- **Energy**, representing how intense or calm the song feels

Using Python, I wrote a custom data generation script that simulates how I listen to music over time. Rather than generating random plays, the script follows behavioral rules that reflect real routines and habits.

## Behavioral Rules & Simulation Logic

To make the synthetic dataset feel realistic, the listening history was generated using explicit behavioral rules rather than random sampling. These rules were designed to reflect real routines, interruptions, and emotional shifts.

**Core simulation rules:**

- **Fixed timeline:**  
  All listening activity is generated between **November 1, 2025 and January 27, 2026**, ensuring a consistent and realistic time window for analysis.

- **Daily routine and sleep cycle:**  
  Listening stops at **3:00 AM** and resumes at **12:00 PM**, reflecting a stable sleep schedule.

- **Skipped days:**  
  After waking up, there is a **30% chance that no music is played for the entire day**, simulating busy or music-free days.

- **Flow states and breaks:**  
  Music is generated in short continuous sessions where songs play back-to-back. After each song, there is a **25% chance of a long break** lasting between one and four hours.

- **Emotional disruption period:**  
  A defined period between **January 19 and January 26** alters song selection probabilities to reflect a temporary emotional shift, with lower-valence songs becoming more common.

- **Time-of-day effects:**  
  Late-night listening (between **12:00 AM and 3:00 AM**) generally favors lower-valence music, with occasional high-energy exceptions to avoid overly deterministic behavior.
