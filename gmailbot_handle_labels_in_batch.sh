#!/bin/bash

#ERROR HANDLING
################################################################

# Exit on error. Append "|| true" if you expect an error.
set -o errexit
# Exit on error inside any functions or subshells.
set -o errtrace
# Do not allow use of undefined vars. Use ${VAR:-} to use an undefined VAR
#set -o nounset
# Catch the error in case mysqldump fails (but gzip succeeds) in `mysqldump |gzip`
set -o pipefail
# Turn on traces, useful while debugging but commented out by default
#set -o xtrace

# keep track of the last executed command
trap 'last_command=$current_command; current_command=$BASH_COMMAND' DEBUG
# echo an error message before exiting
trap 'echo "\"${last_command}\" command filed with exit code $?."' EXIT
#SOURCE: https://intoli.com/blog/exit-on-errors-in-bash-scripts/
#SOURCE2: https://kvz.io/blog/2013/11/21/bash-best-practices
################################################################


SCRIPTPATH="/home/uad/apps/gmail-organizer"


cd $SCRIPTPATH

python3 $SCRIPTPATH/handle_labels_multiple_query.py \
--account alihandikel \
--query reddit \
--query stackoverflow \
--query medium \
--query quora \
--label Informative

python3 $SCRIPTPATH/handle_labels_multiple_query.py \
--account averneus \
--query reddit \
--query stackoverflow \
--query medium \
--query quora \
--label Informative

python3 $SCRIPTPATH/handle_labels_multiple_query.py \
--account averneus \
--query neuvoo \
--query glassdoor \
--query linkedin \
--label JobApp

python3 $SCRIPTPATH/handle_labels_multiple_query.py \
--account alihandikel \
--query neuvoo \
--query glassdoor \
--query linkedin \
--label JobApp

python3 $SCRIPTPATH/handle_labels_multiple_query.py \
--account averneus \
--query dailycodingproblem \
--label DailyCode

python3 $SCRIPTPATH/handle_labels_multiple_query.py \
--account averneus \
--query pythonweekly \
--query elementalselenium \
--query jsw \
--label Notes

