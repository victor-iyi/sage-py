cmake_minimum_required(VERSION 3.9 FATAL_ERROR)

# Get rid of Cygwin warning. Has no effect if not using Cygwin.
set(CMAKE_LEGACY_CYGWIN_WIN32 0)

# Set project name, version & description.
set(PROJECT_NAME "sage")
set(PROJECT_VERSION_MAJOR 1)
set(PROJECT_VERSION_MINOR 0)
set(PROJECT_VERSION_PATCH 0)
set(PROJECT_DESCRIPTION "A lightweight implementation of Knowledge Graph")

project(
  "${PROJECT_NAME}"
  VERSION
    "${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}.${PROJECT_VERSION_PATCH}"
    DESCRIPTION "${PROJECT_DESCRIPTION}")

# Enables testing. (Enables `add_test()` cmd). enable_testing()

# Project library dir.
set(SAGE_LIB_DIR "${PROJECT_SOURCE_DIR}/sage")
set(EXAMPLE_DIR "${PROJECT_SOURCE_DIR}/example")

include_directories("sage/include")
add_subdirectory("sage")

file(GLOB_RECURSE SAGE_EXAMPLE "${EXAMPLE_DIR}/src/*cc")
add_executable(example ${SAGE_EXAMPLE})
target_link_libraries(example sage)
