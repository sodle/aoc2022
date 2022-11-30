#!/bin/bash
MODULE="$1"

if [[ -z $MODULE ]]
then
  poetry run pytest --cov
else
  poetry run pytest "$MODULE" --cov="$MODULE"
fi
