#!/bin/bash
for f in gui/*.ui; do
out=FediBooks/uic/ui_${f:4:-2}py
if [ ! -f "$out" ] || [ "$f" -nt "$out" ]; then
	echo $f ($out)
	pyside2-uic -i 0 -d $f -o $out
fi
done
