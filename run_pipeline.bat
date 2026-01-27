@echo off
setlocal

:: Set the project directory
set PROJECT_DIR=%~dp0
set AI_ENGINE_DIR=%PROJECT_DIR%ai_engine

:: --- Step 1: Set up virtual environment ---
echo [STEP 1] Setting up virtual environment...
if not exist "%AI_ENGINE_DIR%\.venv" (
    echo Creating virtual environment...
    python -m venv "%AI_ENGINE_DIR%\.venv"
) else (
    echo Virtual environment already exists.
)

:: --- Step 2: Install dependencies ---
echo [STEP 2] Installing dependencies...
call "%AI_ENGINE_DIR%\.venv\Scripts\pip.exe" install -r "%AI_ENGINE_DIR%\requirements.txt"

:: --- Step 3: Download dataset ---
echo [STEP 3] Downloading dataset...
call "%AI_ENGINE_DIR%\.venv\Scripts\python.exe" "%AI_ENGINE_DIR%\download_dataset.py"

:: --- Step 4: Run training ---
echo [STEP 4] Running training...
call "%AI_ENGINE_DIR%\.venv\Scripts\python.exe" "%AI_ENGINE_DIR%\train.py" --data "%AI_ENGINE_DIR%\data\datasets\coco128.yaml" --epochs 1 --imgsz 320

:: --- Step 5: Run inference ---
echo [STEP 5] Running inference...
set MODEL_PATH=%AI_ENGINE_DIR%\runs\detect\latest_run\weights\best.pt
set IMAGE_PATH=%AI_ENGINE_DIR%\data\datasets\coco128\coco128\images\train2017\000000000009.jpg
call "%AI_ENGINE_DIR%\.venv\Scripts\python.exe" "%AI_ENGINE_DIR%\inference.py" --model "%MODEL_PATH%" --source "%IMAGE_PATH%"

echo [SUCCESS] Pipeline finished.
endlocal
