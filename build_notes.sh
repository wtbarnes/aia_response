#!/bin/bash
pandoc -V geometry:a4paper -f rst --toc --smart -o README.pdf README.rst
