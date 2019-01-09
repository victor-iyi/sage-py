#!/usr/bin/env bash

# Set Message Colors.
reset='\033[0m'  # Text Reset

# Regular Colors.
red='\033[0;31m' # Red
#green='\033[0;32m'  # Green

# Bold.
#bred='\033[1;31m'   # Red
#bgreen='\033[1;32m' # Green

# Run directory: "/scripts/build/*"
PROJECT_DIR="$(cd -P "$(dirname ${BASH_SOURCE[0]})/.." && pwd)"
BUILD_DIR="${PROJECT_DIR}/build"

# Pre-compiled header.
echo -e "${bgreen}Running pre-compiled header${reset}"
g++ -std=c++17 sage/include/sage_pch.hpp

# Create build directory if it doesn't exist.
mkdir -p ${BUILD_DIR}


# CMake Options
# Generator Options: "Xcode" | "Unix Makefiles" | "ninja" | ""
generator="Xcode"

# Change directory to "run/" directory.
cd "${BUILD_DIR}" || exit

# CMake..
cmake -G${generator} ${PROJECT_DIR}
