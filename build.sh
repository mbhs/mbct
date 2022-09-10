#!/bin/bash

# build jinja templates and sass
#staticjinja build --srcpath=templates --outpath=. && sass sass/style.scss:output/style.css --no-source-map
python3 build.py && sass sass/style.scss:output/style.css --sourcemap=none
