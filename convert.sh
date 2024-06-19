#!/bin/bash

# Loop through all MKV files in the specified directory
for mkv_file in "$DIR"*.mkv; do
    # Check if there are no MKV files in the directory
    if [ "$mkv_file" == "$DIR*.mkv" ]; then
        echo "No MKV files found in the directory."
        exit 1
    fi
    
    # Get the base name of the MKV file (without the extension)
    base_name=$(basename "$mkv_file" .mkv)
    
    # Define the output MP4 file name
    mp4_file="$DIR$base_name.mp4"
    
    # Run the ffmpeg command to convert the MKV to MP4
    ffmpeg -i "$mkv_file" -c:v libx264 -c:a aac "$mp4_file"
    
    echo "Converted $mkv_file to $mp4_file"
done

echo "Conversion complete!"