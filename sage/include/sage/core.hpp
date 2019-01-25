#ifndef SAGE_CORE_HPP
#define SAGE_CORE_HPP

#include "sage/config.hpp"

// SAGE_API
#ifdef SAGE_PLATFORM_WINDOWS
  #ifdef SAGE_BUILD_DLL
    #define SAGE_API __declspec(dllexport)
  #elif SAGE_BUILD_STATIC
    #define SAGE_API __declspec(dllexport)
  #else
    #define SAGE_API __declspec(dllimport)
  #endif
#else
  #define SAGE_API
#endif

// ASSERTIONS.
#ifdef SAGE_ENABLE_ASSERTS
  #define SAGE_ASSERT(x, ...)                             \
    {                                                     \
      if (!(x)) {                                         \
        SAGE_ERROR("Assertion Failed: {0}", __VA_ARGS__); \
        __debugbreak();                                   \
      }                                                   \
    }

  #define SAGE_CORE_ASSERT(x, ...)                             \
    {                                                          \
      if (!(x)) {                                              \
        SAGE_CORE_ERROR("Assertion Failed: {0}", __VA_ARGS__); \
        __debugbreak();                                        \
      }                                                        \
    }
#else
  #define SAGE_ASSERT(x, ...)
  #define SAGE_CORE_ASSERT(x, ...)
#endif

#endif  // !SAGE_CORE_HPP
