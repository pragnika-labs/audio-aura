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

The synthetic listening data was generated using rules modeled directly from my own routines and habits. These behaviors are intentionally personal and are not meant to generalize or represent typical listening patterns.

**Core simulation logic:**

- **Fixed timeline**  
  Listening activity is generated within a defined window (November 2025 to January 2026) to keep the dataset bounded and analyzable.

- **Personal sleep routine**  
  Listening stops at **3:00 AM** and resumes at **12:00 PM**, reflecting my own sleep and wake patterns during this period rather than an assumed “normal” schedule.

- **Music-free days**  
  After waking up, there is a **30% chance of no listening for the entire day**, representing days where I am busy, unwell, or simply not interested in music.

- **Flow states and breaks**  
  When music plays, it often happens in short back-to-back sessions. After each song, there is a **25% chance of a long break** (1–4 hours), reflecting how I switch between activities like work, gaming, or watching content.

- **Emotion-driven listening period**  
  Between **January 19 and January 26**, listening behavior shifts toward lower-valence songs, reflecting a personal low period that temporarily influenced music choice.

- **Time-of-day preferences**  
  Late-night listening (12:00–3:00 AM) generally favors lower-valence music, but a **10% chance of high-energy tracks** is retained to reflect occasional mood shifts and avoid rigid correlations.

## Feature Engineering & Data Setup

Once the synthetic dataset was generated, additional features were created to support time-based and behavioral analysis.

Key transformations include:

- **Timestamp parsing**  
  Timestamps were converted into proper datetime objects to enable temporal analysis.

- **Time-of-day buckets**  
  Each listening event was mapped to a time period based on the hour of the day:
  - Late Night (00:00–03:00)
  - Morning (03:00–12:00)
  - Afternoon (12:00–17:00)
  - Evening (17:00–21:00)
  - Night (21:00–00:00)

- **Emotional disruption flag**  
  A boolean flag was introduced to isolate the defined emotional disruption period (January 19–26), allowing direct comparison between baseline and disrupted listening behavior.

These engineered features form the foundation for the exploratory analysis, clustering, and modeling performed later in the project.

