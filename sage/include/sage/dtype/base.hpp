#ifndef SAGE_DTYPE_BASE_HPP
#define SAGE_DTYPE_BASE_HPP

#include "sage_pch.hpp"

namespace sage {

  /* Type, Boolean, Number, Text, Time, Date & DateTime */
  // sage::dtype supported in "https://schema.org/DataType"
  namespace dtype {

    template <typename T>
    class SAGE_API Type {
     private:
      T _m_Data;

     public:
      virtual ~Type() {}
    };

    typedef Type<bool> Boolean;      // Boolean.
    typedef Type<double> Number;     // Number.
    typedef Type<std::string> Text;  // Text.
    typedef Type<std::time_t> Time;  // Time.
    // typedef Type <?> Time;         // Date
    // typedef Type <?> Time;         // DateTime.

  }  // namespace dtype

}  // namespace sage
#endif  // !SAGE_DTYPE_HPP