#!/usr/bin/env bash
# Rebuild everything: SFX -> silent renders -> final MP4s (16:9 + Instagram Reel 9:16)
set -euo pipefail
cd "$(dirname "$0")"; export PLAYWRIGHT_PATH="${PLAYWRIGHT_PATH:-playwright}"
python3 sfx.py
node render.js silent-16x9.mp4 &
node render.js --vertical silent-9x16.mp4 &
wait
# 16:9, 60 fps
ffmpeg -y -v error -i silent-16x9.mp4 -i sfx.wav -c:v copy -c:a aac -b:a 192k -ac 2 -shortest -movflags +faststart auradrop-promo-16x9.mp4
# Instagram Reel: 1080x1920, 30 fps, H.264 High, AAC 48 kHz stereo
ffmpeg -y -v error -i silent-9x16.mp4 -i sfx.wav -vf fps=30 -c:v libx264 -profile:v high -level 4.2 -preset slow -crf 17 -maxrate 12M -bufsize 24M -pix_fmt yuv420p \
  -c:a aac -b:a 192k -ar 48000 -ac 2 -shortest -movflags +faststart auradrop-reel-9x16.mp4
ffmpeg -y -v error -ss 6.4 -i silent-9x16.mp4 -frames:v 1 reel-cover.png
rm -f silent-16x9.mp4 silent-9x16.mp4 auradrop-promo-silent.mp4 auradrop-promo.mp4
