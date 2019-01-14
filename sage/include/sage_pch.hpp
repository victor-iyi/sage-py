#ifndef SAGE_PCH_HPP
#define SAGE_PCH_HPP

// Sage "static" includes.
#include "sage/config.hpp"
#include "sage/core.hpp"
#include "sage/utils/log.hpp"

#ifdef SAGE_USE_SYSTEM_INCLUDES

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
#endif  // SAGE_USE_SYSTEM_INCLUDES

// Win32 API.
#ifdef SAGE_PLATFORM_WINDOWS
#include <Windows.h>
#endif  // SAGE_PLATFORM_WINDOWS

// External libs.
// JSON library.
#include "nlohmann/json.hpp"

// Boost libraries.
#include <boost/lambda/lambda.hpp>
// #include <boost/filesystem.hpp>
#include <boost/date_time/posix_time/posix_time_types.hpp>

#endif  // !SAGE_PCH_HPP
