import csv
import base64
import pandas as pd

def extract_base64_to_mp4(csv_file):
    df = pd.read_csv(csv_file)
    
    html_video_responses = df[df['trial_type'] == 'html-video-response']
    
    for index, row in html_video_responses.iterrows():
        base64_data = row['response']
        if pd.isna(base64_data):  # Check if response is NaN
            continue    
        #subject = row['PROLIFIC_PID']
        subject=row['run_id']
        task_number = row['task']
        output_file = f"{subject}_task{task_number}.mp4"
        decoded_data = base64.b64decode(base64_data)
        
        with open(output_file, 'wb') as mp4_file:
            mp4_file.write(decoded_data)

# loop trhough all the csv files in the folder called "miming_watching_movies"
# and extract the base64 to mp4
import os
for file in os.listdir('/Users/sophie/Downloads/testing/'):
    if file.endswith(".csv"):
        #file path 
        file = os.path.join('/Users/sophie/Downloads/testing/', file)
        extract_base64_to_mp4(file)
        