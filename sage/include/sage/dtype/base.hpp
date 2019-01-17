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
      Type() = default;
      Type(const T& data) : _m_Data(data) {
        SAGE_CORE_WARN("Initialzied datatype.");
      }
      virtual ~Type() {}

      const T& data() const { return _m_Data; }

      // bool operator<(const Type& lhs, const Type& rhs);
      // bool operator>(const Type& lhs, const Type& rhs);
      // bool operator<=(const Type& lhs, const Type& rhs);
      // bool operator>=(const Type& lhs, const Type& rhs);
      // bool operator==(const Type& lhs, const Type& rhs);
      // bool operator!=(const Type& lhs, const Type& rhs);
      // std::ostream& operator<<(std::ostream& out, const Type& t);
      // std::istream& operator>>(std::istream& in, const Type& t);
    };

    /*
     * +----------------------------------------------------------------------+
     * | +------------------------------------------------------------------+ |
     * | | Specializations.
     * | +------------------------------------------------------------------+ |
     * +----------------------------------------------------------------------+
     */
    template <>
    class SAGE_API Type<bool> {
     private:
      bool _m_Data;

     public:
      Type() = default;
      Type(bool data) : _m_Data(data) { SAGE_CORE_WARN("Initialzied datatype."); }
      bool data() const { return this->_m_Data; }
    };

    template <>
    class SAGE_API Type<double> {
     private:
      double _m_Data;

     public:
      Type() = default;
      Type(double data) : _m_Data(data) {}
      double data() const { return this->_m_Data; }
    };

    template <>
    class SAGE_API Type<int> {
     private:
      int _m_Data;

     public:
      Type() = default;
      Type(int data) : _m_Data(data) {}
      int data() const { return this->_m_Data; }
    };

    template <>
    class SAGE_API Type<std::string> {
     private:
      std::string _m_Data;

     public:
      Type() = default;
      Type(const std::string& data) : _m_Data(data) {}

      const std::string& data() const { return this->_m_Data; }
      const char* const c_str() const { return this->_m_Data.c_str(); }
    };

    template <>
    class SAGE_API Type<std::time_t> {
     private:
      std::time_t _m_Data;
      std::string _m_TimeStr;

     public:
      Type() = default;
      const std::string& toString() const { return this->_m_TimeStr; }
      const std::time_t& data() const { return this->_m_Data; }
    };

    /*
     * +----------------------------------------------------------------------+
     * | +------------------------------------------------------------------+
     * | | | Type defs. |
     * +------------------------------------------------------------------+ |
     * +----------------------------------------------------------------------+
     */
    typedef Type<bool> Boolean;        // Boolean.
    typedef Type<double> NumberFloat;  // NumberFloat.
    typedef Type<int> NumberInteger;   // NumberInteger.
    typedef Type<std::string> Text;    // Text.
    typedef Type<std::string> URL;     // URL.
    typedef Type<std::time_t> Time;    // Time.
    // typedef Type <?> Time;           // Date
    // typedef Type <?> Time;           // DateTime.

  }  // namespace dtype

}  // namespace sage

#endif  // !SAGE_DTYPE_HPP