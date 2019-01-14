#ifndef SAGE_ERROR_HPP
#define SAGE_ERROR_HPP

#include "sage_pch.hpp"

namespace sage {

  namespace error {

    class SAGE_API UnknownValueError : public std::runtime_error {
     public:
      UnknownValueError(const std::string& name)
          : std::runtime_error("Unknown value " + name) {}

      UnknownValueError(int value)
          : std::runtime_error("Unknown name for enum value: " +
                               std::to_string(value)) {}
    };

    class SAGE_API IOError : public std::ios_base::failure {
     public:
      IOError(const std::string& message)
          : std::ios_base::failure("IOError: " + message,
                                   std::io_errc::stream) {}

      IOError(const std::string& message, const std::error_code& ec)
          : std::ios_base::failure("IOError: " + message, ec) {}
    };

  }  // namespace error

}  // namespace sage
#endif  // SAGE_ERROR_HPP
