from ultralytics import YOLO

# load the model you downloaded
model = YOLO("data/best.pt")          # change to player_ball_yolov11.pt if you renamed it

# track players and save a video with boxes + IDs
model.track(
    source="data/15sec_input_720p.mp4",
    save=True,        # writes the output video
    persist=True,     # keeps the same ID when a player re-appears
    conf=0.3          # detection confidence threshold
)

print("Finished!  Check the runs/track/predict.mp4 file.")