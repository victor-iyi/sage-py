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

    template <typename T>
    class SAGE_API Type : public _Base<T> {};

    // Specializations.
    typedef Type<bool> Boolean;      // Boolean.
    typedef Type<double> Number;     // Number.
    typedef Type<std::string> Text;  // Text.
    typedef Type<std::time_t> Time;  // Time.

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