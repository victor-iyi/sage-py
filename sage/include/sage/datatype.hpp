#ifndef SAGE_DATATYPE_HPP
#define SAGE_DATATYPE_HPP

#include "sage_pch.hpp"

namespace sage {
// DataTypes supported in "https://schema.org/DataType"
namespace DataType {
/*
 * +----------------------------------------------------------------------+
 * | +------------------------------------------------------------------+ |
 * | | Boolean: True or False.
 * | +------------------------------------------------------------------+ |
 * +----------------------------------------------------------------------+
 */
struct Boolean {
  Boolean() = default;
  Boolean(bool _Boolean);

 private:
  bool _Data;
};

/*
 * +----------------------------------------------------------------------+
 * | +------------------------------------------------------------------+ |
 * | | A date value in [ISO 8601 date
 * | | format](http://en.wikipedia.org/wiki/ISO_8601). |
 * | +------------------------------------------------------------------+ |
 * +----------------------------------------------------------------------+
 */
struct Date {
  Date() = default;
};

/*
 * +----------------------------------------------------------------------+
 * | +------------------------------------------------------------------+ |
 * | | A combination of date and time of day in the form
 * | | [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] (see Chapter 5.4 of ISO 8601).
 * | +------------------------------------------------------------------+ |
 * +----------------------------------------------------------------------+
 */
struct DateTime {
  // Constructors.
  DateTime() = default;
  DateTime(const std::time_t& _DateTime);
  DateTime(const char* _DateTime);

  std::string dateTimeToString(const std::tm& t, const char* format);
  std::ostream& formatDateTime(std::ostream& out, const std::tm& t,
                               const char* fmt);
  std::tm now();

 private:
  std::string _Data;
};

/*
 * +----------------------------------------------------------------------+
 * | +------------------------------------------------------------------+ |
 * | | Data type: Number.
 * | +------------------------------------------------------------------+ |
 * +----------------------------------------------------------------------+
 */

struct Number {
  Number() = default;
  Number(int _Number);
  Number(float _Number);
  Number(double _Number);
};

/*
 * +----------------------------------------------------------------------+
 * | +------------------------------------------------------------------+ |
 * | | Data type: Text.
 * | +------------------------------------------------------------------+ |
 * +----------------------------------------------------------------------+
 */
struct Text {
  Text() = default;
  Text(std::string _Text);
  Text(std::string& _Text);
  Text(const char* _Text);

 private:
  std::string _Data;
};

/*
 * +----------------------------------------------------------------------+
 * | +------------------------------------------------------------------+ |
 * | | A point in time recurring on multiple days in the form
 * | | hh:mm:ss[Z|(+|-)hh:mm] (see [XML schema for
 * | | details](http://www.w3.org/TR/xmlschema-2/#time)).
 * | +------------------------------------------------------------------+ |
 * +----------------------------------------------------------------------+
 */
struct Time {
  Time() = default;
};

}  // namespace DataType
}  // namespace sage
#endif  // !SAGE_DATATYPE_HPP