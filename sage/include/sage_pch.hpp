#ifndef SAGE_PCH_HPP
#define SAGE_PCH_HPP

// C-standard library.
#include <cstdlib>
#include <ctime>

// C++ standard library.
#include <algorithm>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <memory>
#include <sstream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

// C++ 17
// #include <experimental/filesystem>

// Boost libraries.
// #include <boost/date_time/posix_time/posix_time_types.hpp>
// #include <boost/filesystem.hpp>
// #include <boost/regex.hpp>
// namespace fs = boost::filesystem;

// Win32 API.
#ifdef SAGE_PLATFORM_WINDOWS
#include <Windows.h>
#endif  // SAGE_PLATFORM_WINDOWS

// Sage "static" includes.
#include "sage/config.hpp"
#include "sage/core.hpp"
#include "sage/utils/log.hpp"

#endif  // !SAGE_PCH_HPP
