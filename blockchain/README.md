# helpers
Collection of mostly useful scripts to share


## block_hash.py

  Implementation of a SHA256 for hashing and verification in 1 Kb blocks.
  This enables possible launch of verified blocks before  the whole file is verified - basis for streaming for example.
  
  #### Installation:
  1. Copy the 'block_hash.py' to your computer
  2. launch it with 'python3 block_hash.py' (you must have python 3.x installed)
  3. Follow instructions  

  #### Disclaimer:
  - this program was never meant for serious use, I wanted a MVP for my own training, use therefore with caution
  - provides only resistance against random data loss by design, does not protect against existential forgery
