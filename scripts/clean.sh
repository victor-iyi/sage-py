#!/usr/bin/env bash

# Set Message Colors.
reset='\033[0m'      # Text Reset

# Regular Colors.
red='\033[0;31m'     # Red
green='\033[0;32m'   # Green
cyan='\033[0;36m'    # Cyan
purple='\033[0;35m'  # Purple
yellow='\033[0;33m'  # Yellow
#white='\033[0;37m'  # White

# Bold.
#bred='\033[1;31m'   # Red
#bgreen='\033[1;32m' # Green
# byellow='\033[1;33m' # Yellow
bwhite='\033[1;37m'  # White
bpurple='\033[1;35m' # Purple

# Underline.
ured='\033[4;31m' # Red

echo -e \
	"${cyan}
  #############################################################################
  # +-----------------------------------------------------------------------+ #
  # |       Clean Python, CMake and Cython generated and build files.       | #
  # +-----------------------------------------------------------------------+ #
  #############################################################################
  Tasks:${reset}
    - [ ] Clean __pycache__ & *.py[co] files.
    - [ ] Clean CMake build files.
    - [ ] Clean Cython build & generated C++ files.
"

# Sleep for half a second.
sleep .5s

################################################################################################
# +--------------------------------------------------------------------------------------------+
# | Workout the calling directory.
# +--------------------------------------------------------------------------------------------+
################################################################################################
# Run directory: "/scripts/build/*"
PROJECT_DIR="$(cd -P "$(dirname ${BASH_SOURCE[0]})/.." && pwd)"
BUILD_DIR="${PROJECT_DIR}/build"
SAGE_DIR="${PROJECT_DIR}/sage"

# Go to the project directory or stop.
cd ${PROJECT_DIR} || exit 1

# Clean .DS_Store files.
find . -type f -name '.DS_Store' -delete

echo -e "${bwhite}Removing __pycache__ & *.py[co] files...${reset}"

# Clean all __pycache__ files.
py_clean() {
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
}

py_clean && echo -e "${cyan}
  Tasks:${green}
    - [x] Clean __pycache__ & *.py[co] files.${reset}
    - [ ] Clean CMake & Cython temp build files.
    - [ ] Clean Cython build & generated C++ files.
"

################################################################################################
# +--------------------------------------------------------------------------------------------+
# | CMake & Cython build directory.
# +--------------------------------------------------------------------------------------------+
################################################################################################
if [[ -d "${BUILD_DIR}" ]] >/dev/null 2>&1; then
	echo -e "${bwhite}Removing CMake & Cython temp build files...${reset}"
	# Sleep for half a second.
	sleep .5s

	# Change directory to the build directory.
	cd ${BUILD_DIR} || exit 1
	# To remove all files except certain files...
	#   $ GLOBIGNORE=*.zip:*.iso:*.txt
	#   $ rm -v *
	#   $ unset GLOBIGNORE

	# DO NOT remove these files (separated by colons) => "e.g: *.json:*.gz:*.txt".
	GLOBIGNORE=compile_commands.json:argparse.sh:test.json

	# Remove everything in this directory except GLOBIGNORE
	rm -rf -v *

	# Unset the GLOBIGNORE flag.
	unset GLOBIGNORE

	echo -e "${cyan}
  Tasks:${green}
    - [x] Clean __pycache__ & *.py[co] files.
    - [x] Clean CMake & Cython temp build files.${reset}
    - [ ] Clean Cython build & generated C++ files.
  "
else
	echo
	echo -e "${red}No such directory: ${ured}\"${BUILD_DIR}\"${reset}"
fi

# Sleep for half a second.
sleep .5s

################################################################################################
# +--------------------------------------------------------------------------------------------+
# | Cython lib & src files.
# +--------------------------------------------------------------------------------------------+
################################################################################################
# AVATAR_CORE_DIR="${AVATAR_DIR}/core"
# if [[ -d ${AVATAR_CORE_DIR} ]]; then
# 	# Change directory to Cython dir.
# 	cd ${AVATAR_CORE_DIR} || exit

# 	echo -e "${bwhite}Removing Cython shared objects & DLLs...${reset}"

# 	# Remove everything in this directory except GLOBIGNORE
#   rm **.so

# 	echo -e "${cyan}
#   Tasks:${green}
#     - [x] Clean __pycache__ & *.py[co] files.
#     - [x] Clean CMake & Cython temp build files.
#     - [x] Clean Cython build & generated C++ files.${reset}
# "

# 	# Go back to the project directory.
# 	cd ${PROJECT_DIR} || exit

# else
# 	echo
# 	echo -e "${red}No such file or directory: ${ured}\"${AVATAR_CORE_DIR}\"${reset}"
# fi

echo
echo "✨ Done."
