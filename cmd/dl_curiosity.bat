call C:\ProgramData\Anaconda3\condabin\activate.bat exts-tf2-gpu
python.exe ..\dl.py --rover_name curiosity --cache_location "..\cache" --incremental
call C:\ProgramData\Anaconda3\condabin\deactivate.bat
pause
