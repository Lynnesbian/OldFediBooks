#!/bin/bash
for f in FediBooks/gui/*.ui; do
out=FediBooks/uic/ui_${f:14:-2}py
if [ ! -f "$out" ] || [ "$f" -nt "$out" ]; then
	echo $f \($out\)
	pyside2-uic -i 0 -d $f -o $out
fi
done
