# Normalise-drums-kits
Enables to rename and classify samples in a drums kit to normalise it

This repository has been created to rename and clasify easily samples in the drums kits directory from the website
'https://www.thekitplug.com'.

- renames.py takes folders path as arguments and recursively renames every file .wav in the folders from "<compilation_name> - <instrument> - <id>.wav" into "<id> - <instrument> - <compilation_name>.wav"
  
- classify.py takes folders path as arguments, creates missing folders to classify samples and move samples in the folder corresponding

Usage example : 
  we want to normalise the folder "The Kit Plug - Overdose (Drill Drum Kit) unormalised"
  run rename.py with "The Kit Plug - Overdose (Drill Drum Kit) unormalised" as argument
  then, run classify.py with "The Kit Plug - Overdose (Drill Drum Kit) unormalise" as arguement
  "The Kit Plug - Overdose (Drill Drum Kit) unormalised" has been normalised and is became like the folder "The Kit Plug - Overdose (Drill Drum Kit) normalised"
  
