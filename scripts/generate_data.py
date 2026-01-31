import random
import pandas as pd
from datetime import datetime, timedelta
import os

from song_data import songs_list


# These dates define the overall window for the simulation.
# All listening activity will be generated between these boundaries.
START_DATE = datetime(2025,11,1)
END_DATE = datetime(2026,2,3)

# This period represents a personal low point where listening behavior changes noticeably.
# During this window, song selection is biased toward slower and sadder tracks.
HEARTBREAK_START = datetime(2026,1,19)
HEARTBREAK_END = datetime(2026,1,31)


def generate_history():
    # This list will store every simulated listening event as a row
    data_rows = []
    
    # Start the simulation clock at the beginning of the timeline
    current_time = START_DATE

    print(f"Starting simulation from {START_DATE.date()}.....")

    # Keep generating listening activity until we hit the end date
    while current_time < END_DATE:
        
        # I don’t listen to music while I’m asleep.
        # If the time is between 3 AM and 12 PM, fast-forward to noon.
        if 3 <= current_time.hour < 12:

            hours_to_add = 12 - current_time.hour
            current_time += timedelta(hours=hours_to_add)

            # Even after waking up, there are days where I just don’t listen to music at all.
            # This simulates busy days, low-energy days, or days with no interest.
            if random.random() < 0.30:
                current_time += timedelta(hours=24)
                continue

            # If I do listen, I usually start sometime between 12:00 and 1:00 PM.
            current_time += timedelta(minutes=random.randint(0,60))
            continue

        # If I’m awake and listening, a song usually lasts 3–5 minutes.
        # Time moves forward as the song plays.
        song_duration = random.randint(3,5)
        current_time += timedelta(minutes=song_duration)

        # I don’t listen nonstop.
        # Sometimes I get distracted by work, gaming, or watching something.
        # These breaks can last anywhere from 1 to 4 hours.
        if random.random() < 0.25:
            break_duration = random.randint(60, 240)
            current_time += timedelta(minutes=break_duration)
            continue

        # Safety check in case we crossed the end date while adding time
        if current_time >= END_DATE:
            break

        # Capture the current hour so time-of-day preferences can be applied
        hour = current_time.hour

        # Check whether the current time falls inside the emotional disruption period
        is_heartbreak_era = (HEARTBREAK_START <= current_time <= HEARTBREAK_END)

        # Occasionally, even late at night, I play high-energy music.
        # This simulates rare “concert mode” or hype moments.
        is_concert_mode = False
        if not is_heartbreak_era:
            if (1 <= hour <= 3) and (random.random() < 0.10):
                is_concert_mode = True

        # Each song is assigned a weight that determines how likely it is to be played.
        # Higher weight means higher chance of selection.
        weights = []
        
        for song in songs_list:
            valence = song['valence']
            energy = song['energy']

            # Start with a neutral baseline
            weight = 1.0

            # During the emotional disruption period, happier songs are strongly avoided
            if is_heartbreak_era:
                if valence > 0.5:
                    weight = 0
                elif energy > 0.6:
                    weight = 0.02
                else:
                    weight = 20.0

            # In rare late-night hype moments, high-energy tracks dominate
            elif is_concert_mode:
                if energy > 0.7:
                    weight += 6.0
                else:
                    weight = 0

            # Late-night listening usually leans toward sadder music
            elif 0 <= hour <= 3:
                if valence < 0.4:
                    weight += 5.0
                else:
                    weight -= 0.5

            # During the afternoon, I slightly prefer happier songs
            elif 12 <= hour <= 17:
                if valence > 0.5:
                    weight += 1.5

            # Make sure weights never go negative
            weight = max(weight, 0)
            weights.append(weight)
        
        # If everything somehow gets zero weight, fall back to a random pick
        if sum(weights) == 0:
            selected_song = random.choice(songs_list)
        else:
            selected_song = random.choices(songs_list, weights=weights, k=1)[0]

        # Store the listening event as a structured row
        data_rows.append({
            "timestamp": current_time,
            "song_name": selected_song['name'],
            "artist": selected_song['artist'],
            "valence": selected_song['valence'],
            "energy": selected_song['energy'],
            "hour": hour
        })

    # Once the simulation ends, convert everything into a DataFrame
    print(f"Generated {len(data_rows)} listening events.")

    df = pd.DataFrame(data_rows)

    # Save the output CSV into the data folder relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, '..', 'data', 'my_spotify_data.csv')

    df.to_csv(output_path, index=False)
    print(f"Saved data to {output_path}")


if __name__ == "__main__":
    generate_history()
