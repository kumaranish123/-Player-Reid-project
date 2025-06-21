──────────  README.md  ──────────
```
# Single-Feed Player Re-Identification



## How to run
```bash
git clone https://github.com/kumaranish123/-Player-Reid-project.git
cd -Player-Reid-project
python -m venv venv
venv\Scripts\activate          # Linux/Mac: source venv/bin/activate
pip install -r requirements.txt
python run_track.py
```
Output video: `runs/track/predict.mp4`.

## Dependencies
Python ≥ 3.10, Ultralytics, OpenCV, lap, Torch (full list in `requirements.txt`).  
Large model handled with **Git LFS**.

## Approach
1. YOLOv11 (`best.pt`) detects players each frame.  
2. Ultralytics **BYTE** tracker (`model.track`) keeps the same `id` when a player re-enters.  
3. API saves a new video with coloured boxes and IDs.

## Techniques tried
| Change | Result |
| ------ | ------ |
| conf 0.25 → 0.30 | fewer false ball detections |
| DeepSORT | similar accuracy, slower → kept BYTE |

## Challenges
* Drive quota blocked `gdown` → manual download.  
* PowerShell policy blocked `activate` → used `cmd`.  
* Missing C++ tools for `lap` → installed pre-built wheel.

## Next work
* Train ReID embeddings for cross-camera task.  
* Convert model to ONNX/TensorRT for real-time speed.
```
────────  END README  ────────


──────────  REPORT.md  ──────────
```
# Brief Report – Player Re-ID

**Goal** Maintain the same player ID inside one video feed.  
**Solution** YOLOv11 + BYTE tracker (8-line script).

## Results
• 13 players tracked with stable IDs through the 15-s clip.  
• ~25 s total on laptop CPU (≈15 FPS).

## What worked
* conf 0.30 removed ball false-positives.  
* BYTE tracker gave fewer ID switches than DeepSORT.

## Remaining work
* Cross-camera ID: needs appearance embeddings.  
* Optimise speed with ONNX/TensorRT.

## Key files
| File | Purpose |
| ---- | ------- |
| run_track.py | main script |
| data/best.pt | fine-tuned weights |
| runs/track/predict.mp4 | sample result
```
────────  END REPORT  ─────────


