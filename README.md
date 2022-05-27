# Normalise-drums-kits

This repository has been created to rename and clasify easily samples in the drums kits directory from the website
'https://www.thekitplug.com'.

## Program Files

- renames.py takes folders path as arguments and recursively renames every file .wav in the folders from "\<compilation_name> - \<instrument> - \<id>.wav" into "\<id> - \<instrument> - \<compilation_name>.wav"
  
- classify.py takes folders path as arguments, creates missing folders to classify samples and move samples in the folder corresponding

## Usage example
  we want to normalise the folder "The Kit Plug - Overdose (Drill Drum Kit) unormalised" on Windows.
  For that, we run the program by entering these commands in the windows shell.
  
  ```bash
  python3 rename.py "The Kit Plug - Overdose (Drill Drum Kit) unormalised"
  python3 classify.py "The Kit Plug - Overdose (Drill Drum Kit) unormalised"
  ```

  "The Kit Plug - Overdose (Drill Drum Kit) unormalised" is now normalised and is became like the folder "The Kit Plug - Overdose (Drill Drum Kit) normalised"
  
