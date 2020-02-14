# This script is part of BEAR pipeline
# This script will help the user to modify the paython interpreter locations.
for f in *sh;do sed -i - e"s#/usr/local/bin/python3.7#$1#g" $f;done
rm *e
