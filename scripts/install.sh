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
bgreen='\033[1;32m'  # Green
# byellow='\033[1;33m' # Yellow
bwhite='\033[1;37m'  # White
bpurple='\033[1;35m' # Purple

# Underline.
ured='\033[4;31m' # Red

echo -e \
	"${cyan}
  #############################################################################
  # +-----------------------------------------------------------------------+ #
  # |                   Installing dependencies for Sage.                   | #
  # +-----------------------------------------------------------------------+ #
  #############################################################################
  Tasks:${reset}
    - [ ] Download & install Boost.
    - [ ] Download & install nlohomann/json.
    - [ ] Download & install spdlog.
"

# Sleep for half a second.
sleep .5s

################################################################################################
# +--------------------------------------------------------------------------------------------+
# | Download & install Boost on different platforms.
# +--------------------------------------------------------------------------------------------+
################################################################################################
# BOOST_WIN_URL="https://dl.bintray.com/boostorg/release/1.67.0/source/boost_1_67_0.zip"
# BOOST_WIN_SHA256="7e37372d8cedd0fd6b7529e9dd67c2cb1c60e6c607aed721f5894d704945a7ec"
PLATFORM="macos" # ubuntu, debian, centos, rhel.
INSTALL_PREFIX="${PROJECT_DIR}/sage/vendor"

# Boost URL & Sha256
BOOST_UNIX_URL="https://dl.bintray.com/boostorg/release/1.67.0/source/boost_1_67_0.tar.gz"
BOOST_UNIX_SHA256="8aa4e330c870ef50a896634c931adf468b21f8a69b77007e45c444151229f665"

echo
echo -e "${bwhite}Downloading Boost from \"${BOOST_UNIX_URL}\"${reset}"
if [ command -v wget ] >/dev/null 2>&1; then
	echo -e "${red}You don't have \"wget\" installed... ${reset}"
	echo -e "${yellow}Attempting to install...${reset}"
	# if the platform is macos
	# brew update && brew install wget
	# else if it is linux [Ubuntu or Debian]
	# sudo apt-get update && sudo apt-get install wget
	# else if it is linux [CentOS or RHEL]
	# sudo yum install wget
	# else
	# Cannot install wget
	# exit 1
fi

# Downloading Boost.
# wget -c ${BOOST_UNIX_URL} -P "${INSTALL_PREFIX}"
wget -c ${BOOST_UNIX_URL} -O "${INSTALL_PREFIX}/boost.tar.gz"
echo
echo -e "${bgreen}Download completed!${reset}"

# Verifying Boost.
echo -e "Verifying download..."
echo "TODO: Verifiy download with checksum tool."
echo -e "${bgreen}Verification completed!${reset}"
