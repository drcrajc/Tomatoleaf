import os
import cv2

def convert_videos_to_frames(source_folder, destination_folder):
    # Get a list of all video files in the source folder
    video_files = [file for file in os.listdir(source_folder) if file.endswith(".mp4")]

    # Process each video file
    for video_file in video_files:
        # Construct the paths for the video file and the destination folder
        video_path = os.path.join(source_folder, video_file)
        video_folder = os.path.splitext(video_file)[0]
        output_folder = os.path.join(destination_folder, video_folder)

        # Create the output folder for this video if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        # Open the video file
        video = cv2.VideoCapture(video_path)

        # Check if the video file was successfully opened
        if not video.isOpened():
            print(f"Error opening video file: {video_path}")
            continue

        # Initialize variables
        frame_count = 0
        success = True

        # Read video frames and save them as images
        while success:
            # Read the next frame
            success, frame = video.read()

            if success:
                # Generate the new filename
                frame_name = f"{video_folder}_{video_file}_frame_{frame_count:05d}.jpg"

                # Save the frame as a JPEG image with the new filename
                output_path = os.path.join(output_folder, frame_name)
                cv2.imwrite(output_path, frame)

                # Increment frame count
                frame_count += 1

        # Release the video file
        video.release()

        print(f"Conversion complete. Saved {frame_count} frames to {output_folder}")

# Example usage
source_folder = "path/to/source/folder"
destination_folder = "path/to/destination/folder"
convert_videos_to_frames(source_folder, destination_folder)
