#!/bin/bash

rm -rf gallery-dl images posts 2>/dev/null
rm -rf images 2>/dev/null
mkdir -p images
gallery-dl https://twitter.com/1500tasvir_list
cp -r gallery-dl/twitter/1500tasvir_list/* images/ 2>/dev/null
find images/ -type f ! -name '*.jpg' -delete
mkdir -p posts
python3 main.py