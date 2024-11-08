import cv2
import os
import pandas as pd
from datetime import datetime, timedelta

########################################################################

def extract_frames_from_video(video_path, interval=30):
    """Extract frames from video at a specified interval."""
    cap = cv2.VideoCapture(video_path)
    frames = []
    frame_data = []
    count = 0
    fps = cap.get(cv2.CAP_PROP_FPS)  # Get frames per second
    video_start_time = datetime.strptime('12:00:00', '%H:%M:%S')  # Set start time if needed

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if count % interval == 0:  # Extract frame at every 'interval' count
            timestamp = video_start_time + timedelta(seconds=count / fps)
            frames.append(frame)
            frame_data.append({'frame_id': f'frame_{count // interval}', 'timestamp': timestamp})
        count += 1
    cap.release()
    return frames, frame_data

############################################################################################

def load_reference_images(reference_dir):
    """Load SIFT descriptors from reference images."""
    sift = cv2.SIFT_create()
    descriptors_list = []

    for filename in os.listdir(reference_dir):
        img_path = os.path.join(reference_dir, filename)
        img = cv2.imread(img_path)
        if img is None:
            continue
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        kp, des = sift.detectAndCompute(gray, None)
        if des is not None:
            descriptors_list.append(des)

    return descriptors_list

############################################################################################

def classify_frame(frame, good_descriptors, bad_descriptors, ratio_threshold=1.35):
    """Classify a frame as 'good' or 'bad' based on SIFT feature matching."""
    sift = cv2.SIFT_create()
    kp_frame, des_frame = sift.detectAndCompute(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), None)
    if des_frame is None:
        return 'bad'
    
    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
    good_matches = sum(len(bf.match(des_frame, good_des)) for good_des in good_descriptors)
    bad_matches = sum(len(bf.match(des_frame, bad_des)) for bad_des in bad_descriptors)
    
    match_ratio = good_matches / (bad_matches + 1)
    return 'good' if match_ratio > ratio_threshold else 'bad'

#############################################################################################

def classify_and_save_frames(frames, frame_metadata, good_ref_dir, bad_ref_dir):
    """Classify and save frames as 'good' or 'bad'."""
    good_descriptors = load_reference_images(good_ref_dir)
    bad_descriptors = load_reference_images(bad_ref_dir)
    
    os.makedirs('outputs/good', exist_ok=True)
    os.makedirs('outputs/bad', exist_ok=True)

    for i, frame in enumerate(frames):
        classification = classify_frame(frame, good_descriptors, bad_descriptors)
        frame_id = frame_metadata[i]['frame_id']
        if classification == 'good':
            cv2.imwrite(f'outputs/good/{frame_id}.jpg', frame)
        else:
            cv2.imwrite(f'outputs/bad/{frame_id}.jpg', frame)

###############################################################################################5

# Paths to video and reference directories
video_path = r'C:\Users\spw20ydj\megadetector_project\CameraTraps\videos\124038_Lobster_1.mp4'
good_ref_dir = r'C:\Users\spw20ydj\megadetector_project\CameraTraps\good'
bad_ref_dir = r'C:\Users\spw20ydj\megadetector_project\CameraTraps\bad'

# Step 1: Extract frames from the video
frames, frame_data = extract_frames_from_video(video_path)

# Step 2: Classify frames based on reference images
classify_and_save_frames(frames, frame_data, good_ref_dir, bad_ref_dir)

