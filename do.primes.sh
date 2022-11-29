#!/bin/bash
#SBATCH -N 1
#SBATCH -t 48:00:00
#SBATCH --mem 1GB

./primes.py > $STORE/primes.txt