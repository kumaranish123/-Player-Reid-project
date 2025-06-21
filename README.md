# Single-Feed Player Re-Identification (Assignment)

## How to run
1. Open a terminal (Command Prompt).
2. `cd` to the project folder  
   `cd C:\Users\ANISH KUMAR\Downloads\player-reid-project`
3. Activate the virtual env  
   `venv\Scripts\activate`
4. Run  
   `python run_track.py`
   A result video appears at `runs\track\predict.mp4`.

## Requirements
* Python 3.12
* Packages: ultralytics, opencv-python, gdown, lap

Install with  
`pip install -r requirements.txt`  
(see the file we provide).

## Approach
We use a fine-tuned YOLOv11 model (best.pt) for player detection and the
built-in BYTE tracker of Ultralytics to keep IDs consistent in real time.