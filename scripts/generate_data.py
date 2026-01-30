import random
import pandas as pd
from datetime import datetime, timedelta
import os

from song_data import songs_list

# --- STEP 1: SETTING THE BOUNDARIES ---
# I need to define the start and end of my simulation.
# The code will run from Nov 1st until the day I finished the data (Jan 27th).
START_DATE = datetime(2025,11,1)
END_DATE = datetime(2026,1,27)

# This is the "Heartbreak Week" I want to simulate.
# If the simulation hits these dates, the music taste needs to change drastically.
HEARTBREAK_START = datetime(2026,1,19)
HEARTBREAK_END = datetime(2026,1,26)

def generate_history():
    # This list is my bucket. I'll throw every song I "listen" to in here.
    data_rows = []
    
    # Set the clock to the very beginning.
    current_time = START_DATE

    print(f"Starting simulation from {START_DATE.date()}.....")

    # --- THE MAIN LOOP (The Engine) ---
    # Keep running this loop until the clock hits the End Date.
    while current_time < END_DATE:
        
        # --- LOGIC 1: THE SLEEP CYCLE ---
        # Reality Check: I sleep from 3 AM to 12 PM.
        # If the clock hits this range, I shouldn't be listening to music.
        if 3 <= current_time.hour < 12:

            # Calculate how many hours are left until noon...
            hours_to_add = 12 - current_time.hour
            # ...and fast-forward the clock instantly.
            current_time += timedelta(hours=hours_to_add)

            # Now that I'm "awake" at noon, do I even want to listen to music?
            # I'll flip a coin. 30% chance I'm too busy today.
            if random.random() < 0.30:
                current_time += timedelta(hours=24) # Skip the whole day
                continue # Go back to the start of the loop (don't play music)

            # If I didn't skip the day, I wake up with some variance (0-60 mins).
            # So I start listening between 12:00 and 1:00 PM.
            current_time += timedelta(minutes=random.randint(0,60))
            continue # Restart the loop to check the new time

        # --- LOGIC 2: PLAYLIST FLOW ---
        # If I'm awake, I'm listening. 
        # A song lasts 3-5 mins, plus a tiny gap between tracks.
        song_duration = random.randint(3,5)
        gap = random.randint(0,2)

        # Move the clock forward because time passes while I listen.
        current_time += timedelta(minutes=song_duration + gap)

        # --- LOGIC 3: GETTING DISTRACTED ---
        # I don't listen nonstop. 25% of the time, I take a break.
        # Maybe I'm gaming or watching YouTube for 1 to 4 hours.
        if random.random() < 0.25:
            break_duration = random.randint(60, 240) # 1-4 hours in minutes
            current_time += timedelta(minutes=break_duration)
            continue # Stop here, go back to start.

        # Emergency Stop: Did adding that song push me past the End Date?
        if current_time >= END_DATE:
            break

        # --- LOGIC 4: SETTING THE MOOD (CONTEXT) ---
        # Before picking a song, I need to know the context.
        hour = current_time.hour

        # Check: Am I currently in the "Heartbreak Window"? (True/False)
        is_heartbreak_era = (HEARTBREAK_START <= current_time <= HEARTBREAK_END)

        # Check: Is it a "Party Night"?
        # Default is False. But if it's late (1-3 AM) AND I get lucky (10%)...
        is_concert_mode = False
        if not is_heartbreak_era:
            if(1 <= hour <= 3) and (random.random() < 0.10):
                is_concert_mode = True

        # --- LOGIC 5: THE SCORING SYSTEM (WEIGHTS) ---
        # I need to look at every song in my list and give it a "Score" (Weight).
        # High Score = Likely to pick. Score 0 = Impossible to pick.
        weights = []
        
        for song in songs_list:
            valence = song['valence'] # How happy is it?
            energy = song['energy']   # How fast is it?

            weight = 1.0 # Start fair (everyone gets 1 ticket)

            # SCENARIO A: HEARTBREAK (Sadness Overload)
            if is_heartbreak_era:
                if valence > 0.5:
                    weight = 0      # Kill happy songs immediately
                elif energy > 0.6:
                    weight = 0.05   # Almost kill fast songs
                else:
                    weight = 20.0   # MASSIVE boost to sad/slow songs

            # SCENARIO B: CONCERT MODE (Party Time)
            elif is_concert_mode:
                if energy > 0.7:
                    weight += 10.0  # Boost the bangers
                else:
                    weight = 0      # Kill the slow stuff

            # SCENARIO C: LATE NIGHT (Sad Boi Hours)
            # If it's past midnight...
            elif 0 <= hour <= 3:
                if valence < 0.4:
                    weight += 5.0   # Prefer sad songs
                else:
                    weight -= 0.5   # Less likely to play happy songs

            # SCENARIO D: AFTERNOON (Chill/Happy)
            elif 12 <= hour <= 17:
                if valence > 0.5:
                    weight += 1.5   # Slightly prefer happy songs

            # Math Safety: Weight can't be negative.
            weight = max(weight, 0)

            weights.append(weight)
        
        # --- LOGIC 6: PICKING THE WINNER ---
        # If all weights are 0 (rare), just pick randomly.
        if sum(weights) == 0:
            selected_song = random.choice(songs_list)
        else:
            # Otherwise, run the "Raffle" using the weights I calculated above.
            selected_song = random.choices(songs_list, weights=weights, k=1)[0]

        # --- LOGIC 7: PACKING THE DATA ---
        # Create a dictionary row for this event and add it to my bucket.
        data_rows.append({
            "timestamp": current_time,
            "song_name": selected_song['name'],
            "artist": selected_song['artist'],
            "valence": selected_song['valence'],
            "energy": selected_song['energy'],
            "hour": hour
        })

    # --- FINAL STEP: SAVING THE FILE ---
    # I'm out of the loop now. Time to save.
    print(f"Generated {len(data_rows)} listening events.")

    # Convert my list of dictionaries into a neat table (DataFrame)
    df = pd.DataFrame(data_rows)

    # Find the right folder automatically so I don't have path errors
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, '..', 'data', 'my_spotify_data.csv')

    # Write the CSV file (index=False means don't number the rows 0,1,2...)
    df.to_csv(output_path, index=False)
    print(f"Saved data to {output_path}")

if __name__ == "__main__":
    generate_history()