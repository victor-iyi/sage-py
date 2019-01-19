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
      Type(const T& data) : _m_Data(data) {}
      Type(const Type<T>& other) : _m_Data(other.data()) {}

      virtual ~Type() {}

      const T& data() const { return _m_Data; }

      Type<T> operator=(const T& rhs) {
        Type<T> temp(rhs);
        return temp;
      }

      Type<T> operator+=(const T& rhs) {
        this->_m_Data += rhs;
        return *this;
      }
      Type<T> operator+=(const Type<T>& rhs) {
        this->_m_Data += rhs._m_Data;
        return *this;
      }

      friend Type<T> operator+(Type<T> lhs, const Type<T>& rhs) {
        lhs += rhs;
        return lhs;
      }
      friend bool operator<(const Type<T>& lhs, const Type<T>& rhs) {
        return lhs._m_Data < rhs._m_Data;
      }
      friend bool operator>(const Type<T>& lhs, const Type<T>& rhs) {
        return rhs < lhs;
      }
      friend bool operator<=(const Type<T>& lhs, const Type<T>& rhs) {
        return !(lhs > rhs);
      }
      friend bool operator>=(const Type<T>& lhs, const Type<T>& rhs) {
        return !(lhs < rhs);
      }
      friend bool operator==(const Type<T>& lhs, const Type<T>& rhs) {
        return lhs._m_Data == rhs._m_Data;
      }
      friend bool operator!=(const Type<T>& lhs, const Type<T>& rhs) {
        return !(lhs == rhs);
      }
      friend std::ostream& operator<<(std::ostream& out, const Type<T>& t) {
        out << t._m_Data;
        return out;
      }
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
      Type(bool data) : _m_Data(data) {}
      Type(Type<bool>& other) : _m_Data(other.data()) {}

      bool data() const { return this->_m_Data; }

      Type<bool> operator=(bool rhs) {
        Type<bool> temp(rhs);
        return temp;
      }
      Type<bool> operator+=(bool rhs) {
        this->_m_Data += rhs;
        return *this;
      }
      Type<bool> operator+=(const Type<bool>& rhs) {
        this->_m_Data += rhs._m_Data;
        return *this;
      }

      friend Type<bool> operator+(Type<bool> lhs, const Type<bool>& rhs) {
        lhs += rhs;
        return lhs;
      }
      friend bool operator<(const Type<bool>& lhs, const Type<bool>& rhs) {
        return lhs._m_Data < rhs._m_Data;
      }
      friend bool operator>(const Type<bool>& lhs, const Type<bool>& rhs) {
        return rhs < lhs;
      }
      friend bool operator<=(const Type<bool>& lhs, const Type<bool>& rhs) {
        return !(lhs > rhs);
      }
      friend bool operator>=(const Type<bool>& lhs, const Type<bool>& rhs) {
        return !(lhs < rhs);
      }
      friend bool operator==(const Type<bool>& lhs, const Type<bool>& rhs) {
        return lhs._m_Data == rhs._m_Data;
      }
      friend bool operator!=(const Type<bool>& lhs, const Type<bool>& rhs) {
        return !(lhs == rhs);
      }

      friend std::ostream& operator<<(std::ostream& out, const Type<bool>& t) {
        out << t._m_Data;
        return out;
      }
    };

    template <>
    class SAGE_API Type<double> {
     private:
      double _m_Data;

     public:
      Type() = default;
      Type(double data) : _m_Data(data) {}
      Type(Type<double>& other) : _m_Data(other.data()) {}
      double data() const { return this->_m_Data; }

      Type<double> operator=(double rhs) {
        Type<double> temp(rhs);
        return temp;
      }
      Type<double> operator+=(double rhs) {
        this->_m_Data += rhs;
        return *this;
      }
      Type<double> operator+=(const Type<double>& rhs) {
        this->_m_Data += rhs._m_Data;
        return *this;
      }

      friend Type<double> operator+(Type<double> lhs, const Type<double>& rhs) {
        lhs += rhs;
        return lhs;
      }
      friend bool operator<(const Type<double>& lhs, const Type<double>& rhs) {
        return lhs._m_Data < rhs._m_Data;
      }
      friend bool operator>(const Type<double>& lhs, const Type<double>& rhs) {
        return rhs < lhs;
      }
      friend bool operator<=(const Type<double>& lhs, const Type<double>& rhs) {
        return !(lhs > rhs);
      }
      friend bool operator>=(const Type<double>& lhs, const Type<double>& rhs) {
        return !(lhs < rhs);
      }
      friend bool operator==(const Type<double>& lhs, const Type<double>& rhs) {
        return lhs._m_Data == rhs._m_Data;
      }
      friend bool operator!=(const Type<double>& lhs, const Type<double>& rhs) {
        return !(lhs == rhs);
      }

      friend std::ostream& operator<<(std::ostream& out,
                                      const Type<double>& t) {
        out << t._m_Data;
        return out;
      }
    };

    template <>
    class SAGE_API Type<int> {
     private:
      int _m_Data;

     public:
      Type() = default;
      Type(int data) : _m_Data(data) {}
      Type(Type<int>& other) : _m_Data(other.data()) {}

      int data() const { return this->_m_Data; }

      Type<int> operator=(int rhs) {
        Type<int> temp(rhs);
        return temp;
      }
      Type<int> operator+=(int rhs) {
        this->_m_Data += rhs;
        return *this;
      }
      Type<int> operator+=(const Type<int>& rhs) {
        this->_m_Data += rhs._m_Data;
        return *this;
      }

      friend Type<int> operator+(Type<int> lhs, const Type<int>& rhs) {
        lhs += rhs;
        return lhs;
      }
      friend bool operator<(const Type<int>& lhs, const Type<int>& rhs) {
        return lhs._m_Data < rhs._m_Data;
      }
      friend bool operator>(const Type<int>& lhs, const Type<int>& rhs) {
        return rhs < lhs;
      }
      friend bool operator<=(const Type<int>& lhs, const Type<int>& rhs) {
        return !(lhs > rhs);
      }
      friend bool operator>=(const Type<int>& lhs, const Type<int>& rhs) {
        return !(lhs < rhs);
      }
      friend bool operator==(const Type<int>& lhs, const Type<int>& rhs) {
        return lhs._m_Data == rhs._m_Data;
      }
      friend bool operator!=(const Type<int>& lhs, const Type<int>& rhs) {
        return !(lhs == rhs);
      }

      friend std::ostream& operator<<(std::ostream& out, const Type<int>& t) {
        out << t._m_Data;
        return out;
      }
    };

    template <>
    class SAGE_API Type<std::string> {
     private:
      std::string _m_Data;

     public:
      Type() = default;
      Type(const std::string& data) : _m_Data(data) {}
      Type(const Type<std::string>& other) : _m_Data(other.data()) {}

      const std::string& data() const { return this->_m_Data; }
      const char* const c_str() const { return this->_m_Data.c_str(); }

      Type<std::string> operator=(const std::string& rhs) {
        Type<std::string> temp(rhs);
        return temp;
      }
      Type<std::string> operator+=(const std::string& rhs) {
        this->_m_Data += rhs;
        return *this;
      }
      Type<std::string> operator+=(const Type<std::string>& rhs) {
        this->_m_Data += rhs._m_Data;
        return *this;
      }

      friend Type<std::string> operator+(Type<std::string> lhs, const Type<std::string>& rhs) {
        lhs += rhs;
        return lhs;
      }
      friend bool operator<(const Type<std::string>& lhs,
                            const Type<std::string>& rhs) {
        return lhs._m_Data < rhs._m_Data;
      }
      friend bool operator>(const Type<std::string>& lhs,
                            const Type<std::string>& rhs) {
        return rhs < lhs;
      }
      friend bool operator<=(const Type<std::string>& lhs,
                             const Type<std::string>& rhs) {
        return !(lhs > rhs);
      }
      friend bool operator>=(const Type<std::string>& lhs,
                             const Type<std::string>& rhs) {
        return !(lhs < rhs);
      }
      friend bool operator==(const Type<std::string>& lhs,
                             const Type<std::string>& rhs) {
        return lhs._m_Data == rhs._m_Data;
      }
      friend bool operator!=(const Type<std::string>& lhs,
                             const Type<std::string>& rhs) {
        return !(lhs == rhs);
      }

      friend std::ostream& operator<<(std::ostream& out,
                                      const Type<std::string>& t) {
        out << t._m_Data;
        return out;
      }
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