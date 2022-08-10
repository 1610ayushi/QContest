#!/bin/sh
# Author : Yakshit Jain
# Copyright (c) Crio.Do
# Script follows here:

PS3="Select your programming language please: "

select opt in Java Python; do

  case $opt in
    Java)
    python3 setup.py ./__CRIO__/metadata.json JAVA
    rm -rf ./python
      break
      ;;
    Python)
    python3 setup.py ./__CRIO__/metadata.json PYTHON
    rm -rf ./java
      break
      ;;
    *) 
      echo "Invalid option $REPLY"
      ;;
  esac
done

