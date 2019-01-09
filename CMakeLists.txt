cmake_minimum_required(VERSION 3.9 FATAL_ERROR)

# Get rid of Cygwin warning. Has no effect if not using Cygwin.
set(CMAKE_LEGACY_CYGWIN_WIN32 0)

project(sage CXX)

# Set project name, version & description.
set(PROJECT_NAME "sage")
set(PROJECT_VERSION_MAJOR 1)
set(PROJECT_VERSION_MINOR 0)
set(PROJECT_VERSION_PATCH 0)
set(PROJECT_DESCRIPTION "A lightweight implementation of Knowledge Graph")

# ---------------------------------------------------------------------
# compiler config
# ---------------------------------------------------------------------
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Enables testing. (Enables `add_test()` cmd).
enable_testing()

# Project library dir.
set(SAGE_LIB_DIR "${PROJECT_SOURCE_DIR}/sage")
set(EXAMPLE_DIR "${PROJECT_SOURCE_DIR}/example")

# !----------------- Set warning & compiler flags.-----------------!#
if("${CMAKE_CXX_COMPILER_ID}" STREQUAL "gcc"
   OR "${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU"
   OR "${CMAKE_CXX_COMPILER_ID}" STREQUAL "clang")

  # # Use these warnings for gcc or clang compilers.
  add_compile_options("-Wall")
  add_compile_options("-Wextra")
  add_compile_options("-Wconversion")
  add_compile_options("-pedantic")
  add_compile_options("-Wfatal-errors")

  # # Use these warnings for gcc or clang compilers. set(warnings "-Wall -Wextra
  # -Werror -Wconversion -pedantic -Wfatal-errors")

  # Use these compiler flag for gcc or clang compilers.
  set(compiler_flags "${CMAKE_CXX_FLAGS} -std=c++17 -stdlib=libc++")

  # Microsoft Visual Studio Compiler.
elseif("${CMAKE_CXX_COMPILER_ID}" STREQUAL "MSVC")

  # Use these warnings for MSVC compiler.
  set(warnings "/W4 /WX /EHsc")

  # Use these compiler flag for gcc or clang compilers.
  set(compiler_flags "${CMAKE_CXX_FLAGS} /std:c++17 /stdlib:libc++")
endif()

# !----------------------- Set language flags -----------------------!#
if(NOT CONFIGURED_ONCE)
  # Make CMake Configurations to be available in source files.
  configure_file(# Where configurations are defined.
                 "${CMAKE_SOURCE_DIR}/config/config.hpp.in"
                 # Where CMake writes auto configuration @build time.
                 "${SAGE_LIB_DIR}/include/sage/config.hpp")

  # Setting warnings & compiler flags.
  set(CMAKE_CXX_FLAGS ${compiler_flags}
      CACHE STRING "Flags used by compiler during all build types."
      FORCE)
  set(CMAKE_C_FLAGS ${compiler_flags}
      CACHE STRING "Flags used by compiler during all build types."
      FORCE)
endif()

include_directories("sage/include")
add_subdirectory("sage")

file(GLOB_RECURSE SAGE_EXAMPLE "${EXAMPLE_DIR}/src/*cc")
add_executable(example ${SAGE_EXAMPLE})
target_link_libraries(example sage)

add_test(NAME example COMMAND example)
