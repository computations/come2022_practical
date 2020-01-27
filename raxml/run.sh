#!/bin/bash

raxml-ng --msa ../data/027.fas --model gtr+g+i --seed 1997727857 --tree rand{1} --prefix seed1 --all --bs-trees 10
raxml-ng --msa ../data/027.fas --model gtr+g+i --seed 287019283 --tree rand{1} --prefix seed2 --all --bs-trees 10
