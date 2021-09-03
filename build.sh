#!/bin/bash

# build jinja templates and sass
staticjinja build --srcpath=templates --outpath=. && sass sass/style.scss:style.css --no-source-map
