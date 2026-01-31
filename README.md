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
