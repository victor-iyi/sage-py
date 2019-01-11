#ifndef SAGE_DTYPE_HPP
#define SAGE_DTYPE_HPP

#include "sage_pch.hpp"

namespace sage {

// sage::dtype supported in "https://schema.org/DataType"
namespace dtype {

template <typename T>
class _Base {
 public:
  _Base() = default;
  _Base(const T& _T) : _m_T(_T) {}

  // virtual ~_Base();

 private:
  T _m_T;
};

// Specializations.
typedef _Base<bool> Boolean;      // Boolean.
typedef _Base<double> Number;     // Number.
typedef _Base<std::string> Text;  // Text.
typedef _Base<std::time_t> Time;  // Time.

/*
Boolean
Date
DateTime
`
Text
Time
*/
}  // namespace dtype

}  // namespace sage
#endif  // !SAGE_DTYPE_HPP