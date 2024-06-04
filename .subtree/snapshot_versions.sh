#!/bin/bash
set -e

PYDO3SE_LOCAL_PATH="src/pyDO3SE"
THERMAL_TIME_LOCAL_PATH="src/thermal_time"
DO3SE_PHENOLOGY_LOCAL_PATH="src/do3se_phenology"
DO3SE_MET_LOCAL_PATH="src/do3se_met"

PYDO3SE_VERSION=`cat $PYDO3SE_LOCAL_PATH/VERSION.txt`
THERMAL_TIME_VERSION=`cat $THERMAL_TIME_LOCAL_PATH/VERSION.txt`
DO3SE_PHENOLOGY_VERSION=`cat $DO3SE_PHENOLOGY_LOCAL_PATH/VERSION.txt`
DO3SE_MET_VERSION=`cat $DO3SE_MET_LOCAL_PATH/VERSION.txt`


echo "pyDO3SE version: $PYDO3SE_VERSION"
echo "thermal_time version: $THERMAL_TIME_VERSION"
echo "do3se_phenology version: $DO3SE_PHENOLOGY_VERSION"
echo "do3se_met version: $DO3SE_MET_VERSION"

PREVIOUS_PYDO3SE_VERSION=`cat SUB_VERSIONS.txt | grep "pyDO3SE" | cut -d " " -f 3`
PREVIOUS_THERMAL_TIME_VERSION=`cat SUB_VERSIONS.txt | grep "thermal_time" | cut -d " " -f 3`
PREVIOUS_DO3SE_PHENOLOGY_VERSION=`cat SUB_VERSIONS.txt | grep "do3se_phenology" | cut -d " " -f 3`
PREVIOUS_DO3SE_MET_VERSION=`cat SUB_VERSIONS.txt | grep "do3se_met" | cut -d " " -f 3`

if [[ "$PREVIOUS_PYDO3SE_VERSION" == "$PYDO3SE_VERSION" ]]; then
  if [[ "$PREVIOUS_THERMAL_TIME_VERSION" != "$THERMAL_TIME_VERSION" ]]; then
    echo "thermal_time version has changed. Please update the version of pyDO3SE before continuing"
    exit 1
  fi
  if [[ "$PREVIOUS_DO3SE_PHENOLOGY_VERSION" != "$DO3SE_PHENOLOGY_VERSION" ]]; then
    echo "do3se_phenology version has changed. Please update the version of pyDO3SE before continuing"
    exit 1
  fi
  if [[ "$PREVIOUS_DO3SE_MET_VERSION" != "$DO3SE_MET_VERSION" ]]; then
    echo "do3se_met version has changed. Please update the version of pyDO3SE before continuing"
    exit 1
  fi
fi

# If the version of any of the dependencies have changed and PYDO3SE hasn't then we need to
# ask the user to update the version of pyDO3SE before continuing



# Store version in file named SUB_VERSIONS.txt
echo "pyDO3SE version: $PYDO3SE_VERSION" > SUB_VERSIONS.txt
echo "thermal_time version: $THERMAL_TIME_VERSION" >> SUB_VERSIONS.txt
echo "do3se_phenology version: $DO3SE_PHENOLOGY_VERSION" >> SUB_VERSIONS.txt
echo "do3se_met version: $DO3SE_MET_VERSION" >> SUB_VERSIONS.txt

bumpversion --new-version="$PYDO3SE_VERSION" patch

# Commit the changes
git add SUB_VERSIONS.txt
git add .bumpversion.cfg
git commit -m "Bump version to $PYDO3SE_VERSION"
git push


# Push tags
git tag -a "v$PYDO3SE_VERSION" -m "Version $PYDO3SE_VERSION"
git push --tags

