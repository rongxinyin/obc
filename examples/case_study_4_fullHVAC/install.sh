#!/bin/bash
set -e
TMP=/tmp/$USER/obc_caseStudy_full_install
TMP_MBL=/tmp/${USER}_obc_caseStudy_full_install/modelica-buildings
TMP_BUP=/tmp/${USER}_obc_caseStudy_full_install/BuildingsPy

get_repo(){
    TMPDIR=$1
    REPO=$2
    HASH=$3
    if [ -d $TMPDIR ]; then
        cd $TMPDIR
        if [ -n "$(git status --porcelain)" ]; then
            # Local changes exist
            echo `pwd`
            echo "Error, aborting due to local changes in $TMPDIR"
            exit 1
        fi;
    else
      # Directory does not exist
      git clone $REPO $TMPDIR
    fi;
    cd $TMPDIR
    # Switch to specific commit (head of master as of Aug. 23, 2021)
    git fetch
    git checkout $HASH
    echo "Cloned repository into `pwd`"
}

echo "Updating Modelica Buildings Library"
get_repo $TMP_MBL https://github.com/lbl-srg/modelica-buildings.git de7086531d241bc074f0e74e3b26cf99eccee235
echo "Updating BuildingsPy"
get_repo $TMP_BUP https://github.com/lbl-srg/BuildingsPy.git 16ddd17cce0c802f82e0a138b1b0f3305cb4bcb0

echo "Don't forget to set export MODELICAPATH=$TMP_MBL"
echo "Don't forget to set export PYTHONPATH=$TMP_BUP:$PYTHONPATH"
