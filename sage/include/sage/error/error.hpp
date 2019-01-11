#ifndef SAGE_ERROR_HPP
#define SAGE_ERROR_HPP

#include "sage_pch.hpp"

namespace sage {

  namespace error {

    class SAGE_API UnknownValueError : public std::runtime_error {
     public:
      UnknownValueError(const std::string& name)
          : std::runtime_error("Unknown value" + name) {}

      UnknownValueError(int value)
          : std::runtime_error("Unknown name for enum value: " +
                               std::to_string(value)) {}
    };

  }  // namespace error

}  // namespace sage
#endif  // SAGE_ERROR_HPP
