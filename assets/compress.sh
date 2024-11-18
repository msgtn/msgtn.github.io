#!/bin/sh
find . -type f -name "*.jpg" |  xargs -I {} -n1  convert {} -define jpeg:extent=1000kb {}
