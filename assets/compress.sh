#!/bin/sh
# Run from repo root: assets/compress.sh
# Backs up full-resolution originals to _assets/ (excluded from the Jekyll
# build), then downsizes + recompresses the served copies in assets/.
MAX_DIM=1600

for dir in assets/img assets/catbot; do
  find "$dir" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" \) | while read -r f; do
    backup="_${f}"
    mkdir -p "$(dirname "$backup")"
    [ -f "$backup" ] || cp -p "$f" "$backup"

    case "$f" in
      *.jpg|*.jpeg)
        convert "$f" -resize "${MAX_DIM}x${MAX_DIM}>" -strip -quality 82 "$f"
        ;;
      *.png)
        convert "$f" -resize "${MAX_DIM}x${MAX_DIM}>" -strip \
          -define png:compression-level=9 \
          -define png:compression-filter=5 \
          -define png:compression-strategy=1 "$f"
        ;;
    esac
  done
done
