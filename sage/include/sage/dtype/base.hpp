#ifndef SAGE_DTYPE_BASE_HPP
#define SAGE_DTYPE_BASE_HPP

#include "sage_pch.hpp"

namespace sage {

  /* Type, Boolean, Number, Text, Time, Date & DateTime */
  // sage::dtype supported in "https://schema.org/DataType"
  namespace dtype {

    /*
     * +----------------------------------------------------------------------+
     * | +------------------------------------------------------------------+ |
     * | | Base DType.
     * | +------------------------------------------------------------------+ |
     * +----------------------------------------------------------------------+
     */
    template <typename T>
    class SAGE_API Type {
     private:
      T _m_Data;

     public:
      Type() = default;
      Type(const T& data) : _m_Data(data) {}
      Type(const Type<T>& other) { this->_m_Data = other._m_Data; }

      const T& data() const { return this->_m_Data; }

      Type<T> operator=(const T& rhs) {
        this->_m_Data = rhs;
        return *this;
      }
      Type<T> operator+=(const T& rhs) {
        this->_m_Data += rhs;
        return *this;
      }
      Type<T> operator+=(const Type<T>& rhs) { return *this += rhs._m_Data; }
      Type<T> operator+(const Type<T>& rhs) { return *this += rhs; }
      bool operator<(const Type<T>& rhs) const {
        return this->_m_Data < rhs._m_Data;
      }
      bool operator>(const Type<T>& rhs) const { return *this < rhs; }
      bool operator<=(const Type<T>& rhs) const { return !(*this > rhs); }
      bool operator>=(const Type<T>& rhs) const { return !(*this < rhs); }
      bool operator==(const Type<T>& rhs) const {
        return this->_m_Data == rhs._m_Data;
      }
      bool operator!=(const Type<T>& rhs) const { return !(*this == rhs); }

      friend std::ostream& operator<<(std::ostream& out, const Type<T>& t) {
        out << t._m_Data;
        return out;
      }
    };

    /*
     * +----------------------------------------------------------------------+
     * | +------------------------------------------------------------------+ |
     * | | Specialization: Boolean<bool>.
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
      Type(const Type<bool>& other) { this->_m_Data = other._m_Data; }

      inline bool data() const { return this->_m_Data; }

      Type<bool> operator=(bool rhs) {
        this->_m_Data = rhs;
        return *this;
      }
      bool operator<(const Type<bool>& rhs) const {
        return this->_m_Data < rhs._m_Data;
      }
      bool operator>(const Type<bool>& rhs) const { return *this < rhs; }
      bool operator<=(const Type<bool>& rhs) const { return !(*this > rhs); }
      bool operator>=(const Type<bool>& rhs) const { return !(*this < rhs); }
      bool operator==(const Type<bool>& rhs) const {
        return this->_m_Data == rhs._m_Data;
      }
      bool operator!=(const Type<bool>& rhs) const { return !(*this == rhs); }

      friend std::ostream& operator<<(std::ostream& out, const Type<bool>& t) {
        out << t._m_Data;
        return out;
      }
    };

    /*
     * +----------------------------------------------------------------------+
     * | +------------------------------------------------------------------+ |
     * | | Spcialization: Float<double>
     * | +------------------------------------------------------------------+ |
     * +----------------------------------------------------------------------+
     */
    template <>
    class SAGE_API Type<double> {
     private:
      double _m_Data;

     public:
      Type() = default;
      Type(double data) : _m_Data(data) {}
      Type(const Type<double>& other) { this->_m_Data = other._m_Data; }

      inline double data() const { return this->_m_Data; }

      Type<double> operator=(double rhs) {
        this->_m_Data = rhs;
        return *this;
      }
      Type<double> operator+=(double rhs) {
        this->_m_Data += rhs;
        return *this;
      }
      Type<double> operator+=(const Type<double>& rhs) {
        return *this += rhs._m_Data;
      }
      Type<double> operator+(const Type<double>& rhs) { return *this += rhs; }
      bool operator<(const Type<double>& rhs) const {
        return this->_m_Data < rhs._m_Data;
      }
      Type<double> operator-=(double rhs) {
        this->_m_Data -= rhs;
        return *this;
      }
      Type<double> operator-=(const Type<double>& rhs) {
        return *this -= rhs._m_Data;
      }
      Type<double> operator-(const Type<double>& rhs) { return *this -= rhs; }
      Type<double> operator*=(double rhs) {
        this->_m_Data *= rhs;
        return *this;
      }
      Type<double> operator*=(const Type<double>& rhs) {
        return *this *= rhs._m_Data;
      }
      Type<double> operator*(const Type<double>& rhs) { return *this *= rhs; }
      Type<double> operator/=(double rhs) {
        this->_m_Data /= rhs;
        return *this;
      }
      Type<double> operator/=(const Type<double>& rhs) {
        return *this /= rhs._m_Data;
      }
      Type<double> operator/(const Type<double>& rhs) { return *this /= rhs; }
      bool operator>(const Type<double>& rhs) const { return *this < rhs; }
      bool operator<=(const Type<double>& rhs) const { return !(*this > rhs); }
      bool operator>=(const Type<double>& rhs) const { return !(*this < rhs); }
      bool operator==(const Type<double>& rhs) const {
        return this->_m_Data == rhs._m_Data;
      }
      bool operator!=(const Type<double>& rhs) const { return !(*this == rhs); }

      friend std::ostream& operator<<(std::ostream& out,
                                      const Type<double>& t) {
        out << t._m_Data;
        return out;
      }
    };

    /*
     * +----------------------------------------------------------------------+
     * | +------------------------------------------------------------------+ |
     * | | Specialization: Integer<int>
     * | +------------------------------------------------------------------+ |
     * +----------------------------------------------------------------------+
     */
    template <>
    class SAGE_API Type<int> {
     private:
      int _m_Data;

     public:
      Type() = default;
      Type(int data) : _m_Data(data) {}
      Type(const Type<int>& other) { this->_m_Data = other._m_Data; }

      inline int data() const { return this->_m_Data; }

      Type<int> operator=(int rhs) {
        this->_m_Data = rhs;
        return *this;
      }
      Type<int> operator+=(int rhs) {
        this->_m_Data += rhs;
        return *this;
      }
      Type<int> operator+=(const Type<int>& rhs) {
        return *this += rhs._m_Data;
      }
      Type<int> operator+(const Type<int>& rhs) { return *this += rhs; }
      Type<int> operator-=(int rhs) {
        this->_m_Data -= rhs;
        return *this;
      }
      Type<int> operator-=(const Type<int>& rhs) {
        return *this -= rhs._m_Data;
      }
      Type<int> operator-(const Type<int>& rhs) { return *this -= rhs; }
      Type<int> operator*=(int rhs) {
        this->_m_Data *= rhs;
        return *this;
      }
      Type<int> operator*=(const Type<int>& rhs) {
        return *this *= rhs._m_Data;
      }
      Type<int> operator*(const Type<int>& rhs) { return *this *= rhs; }
      Type<int> operator/=(int rhs) {
        this->_m_Data /= rhs;
        return *this;
      }
      Type<int> operator/=(const Type<int>& rhs) {
        return *this /= rhs._m_Data;
      }
      Type<int> operator/(const Type<int>& rhs) { return *this /= rhs; }
      Type<int> operator%=(int rhs) {
        this->_m_Data %= rhs;
        return *this;
      }
      Type<int> operator%=(const Type<int>& rhs) {
        return *this %= rhs._m_Data;
      }
      Type<int> operator%(const Type<int>& rhs) { return *this %= rhs; }
      bool operator<(const Type<int>& rhs) const {
        return this->_m_Data < rhs._m_Data;
      }
      bool operator>(const Type<int>& rhs) const { return *this < rhs; }
      bool operator<=(const Type<int>& rhs) const { return !(*this > rhs); }
      bool operator>=(const Type<int>& rhs) const { return !(*this < rhs); }
      bool operator==(const Type<int>& rhs) const {
        return this->_m_Data == rhs._m_Data;
      }
      bool operator!=(const Type<int>& rhs) const { return !(*this == rhs); }

      friend std::ostream& operator<<(std::ostream& out, const Type<int>& t) {
        out << t._m_Data;
        return out;
      }
    };

    /*
     * +----------------------------------------------------------------------+
     * | +------------------------------------------------------------------+ |
     * | | Specialization: Text<std::string>.
     * | +------------------------------------------------------------------+ |
     * +----------------------------------------------------------------------+
     */
    template <>
    class SAGE_API Type<std::string> {
     private:
      std::string _m_Data;

     public:
      Type() = default;
      Type(const char* const data) : _m_Data(data) {}
      Type(const std::string& data) : _m_Data(data) {}
      Type(const Type<std::string>& other) { this->_m_Data = other._m_Data; }

      const std::string& data() const { return this->_m_Data; }
      const char* const c_str() const { return this->_m_Data.c_str(); }

      Type<std::string> operator=(const std::string& rhs) {
        this->_m_Data = rhs;
        return *this;
      }
      Type<std::string> operator=(const char* const rhs) {
        this->_m_Data = rhs;
        return *this;
      }
      Type<std::string> operator+=(const std::string& rhs) {
        this->_m_Data += rhs;
        return *this;
      }
      Type<std::string> operator+=(const Type<std::string>& rhs) {
        return *this += rhs._m_Data;
      }
      Type<std::string> operator+(const Type<std::string>& rhs) {
        return *this += rhs;
      }
      bool operator<(const Type<std::string>& rhs) const {
        return this->_m_Data < rhs._m_Data;
      }
      bool operator>(const Type<std::string>& rhs) const { return *this < rhs; }
      bool operator<=(const Type<std::string>& rhs) const {
        return !(*this > rhs);
      }
      bool operator>=(const Type<std::string>& rhs) const {
        return !(*this < rhs);
      }
      bool operator==(const Type<std::string>& rhs) const {
        return this->_m_Data == rhs._m_Data;
      }
      bool operator!=(const Type<std::string>& rhs) const {
        return !(*this == rhs);
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
     * | +------------------------------------------------------------------+ |
     * | | TypeDefs.
     * | +------------------------------------------------------------------+ |
     * +----------------------------------------------------------------------+
     */
    typedef Type<bool> Boolean;      // Boolean.
    typedef Type<double> Float;      // Float.
    typedef Type<int> Integer;       // Integer.
    typedef Type<std::string> Text;  // Text.
    typedef Type<std::string> URL;   // URL.
    typedef Type<std::time_t> Time;  // Time.
    // typedef Type <?> Date;           // Date
    // typedef Type <?> DateTime;       // DateTime.

  }  // namespace dtype

}  // namespace sage

#endif  // !SAGE_DTYPE_HPP