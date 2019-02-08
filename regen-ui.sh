#!/bin/bash
for f in gui/*.ui; do echo $f; pyside2-uic -d $f -o FediBooks/uic/${f:4:-2}py; done
