#!/bin/bash

# Create a new release of Mumble-Django.

set -e
set -u

export HGPLAIN=t

BASEDIR=`hg root`
LASTTAG=`hg tags | grep -v tip | head -n1 | cut -d' ' -f1`

VERSIONSTR=`python -c 'from djextdirect import VERSIONSTR; print VERSIONSTR'`

echo
echo "Current version is ${VERSIONSTR}."

if hg tags | grep "${VERSIONSTR}" > /dev/null; then
    echo "Warning: Version string in djExtDirect module has not been updated."
    echo "         Running vi so you can fix it in three, two, one."
    sleep 3
    MODFILE="${BASEDIR}/djextdirect/__init__.py"
    vi "$MODFILE" -c '/VERSION ='
    hg commit "$MODFILE" -m 'Bump module version'
fi

VERSIONSTR=`python -c 'from djextdirect import VERSIONSTR; print VERSIONSTR'`

HISTFILE=`tempfile`
hg log -r "${LASTTAG}:tip" > "${HISTFILE}"
vi -p "${HISTFILE}" "${BASEDIR}/CHANGELOG"
rm "${HISTFILE}"

echo "New version will be tagged ${VERSIONSTR}. If this is correct, hit enter to continue."
read

hg commit "${BASEDIR}/CHANGELOG" -m "Releasing ${VERSIONSTR}."
hg tag "${VERSIONSTR}"
hg push

echo "You successfully released ${VERSIONSTR}!"

python setup.py register
