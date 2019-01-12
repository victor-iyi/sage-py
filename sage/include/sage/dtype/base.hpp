#ifndef SAGE_DTYPE_BASE_HPP
#define SAGE_DTYPE_BASE_HPP

#include "sage_pch.hpp"

namespace sage {

  /* Type, Boolean, Number, Text, Time, Date & DateTime */
  // sage::dtype supported in "https://schema.org/DataType"
  namespace dtype {

    template <typename T>
    class _DTypeBase {
     public:
      _DTypeBase(const T& _T) : _m_T(_T) {}
      virtual ~_DTypeBase();

     private:
      T _m_T;
    };

    template <typename T>
    class SAGE_API Type : public _DTypeBase<T> {
     public:
      Type() = default;
      virtual ~Type() override;
    };

    // Specializations.
    typedef Type<bool> Boolean;      // Boolean.
    typedef Type<double> Number;     // Number.
    typedef Type<std::string> Text;  // Text.
    typedef Type<std::time_t> Time;  // Time.

  }  // namespace dtype

}  // namespace sage
#endif  // !SAGE_DTYPE_HPP