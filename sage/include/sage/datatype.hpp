#ifndef SAGE_DATATYPE_HPP
#define SAGE_DATATYPE_HPP

#include "sage_pch.hpp"

namespace SAGE {
// DataTypes supported in "https://schema.org/DataType"
namespace DataType {
struct Boolean {
  // Boolean: True or False.
  Boolean(bool _Boolean);

 private:
  bool _Data;
};

struct Date {
  // A date value in [ISO 8601 date
  // format](http://en.wikipedia.org/wiki/ISO_8601).
};

struct DateTime {
  // A combination of date and time of day in the form
  // [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] (see Chapter 5.4 of ISO 8601).
};

struct Number {
  // Data type: Number.
  Number(int _Number);
  Number(float _Number);
  Number(double _Number);
};

struct Text {
  // Data type: Text.
  Text(std::string _Text);
  Text(std::string& _Text);
  Text(const char* _Text);

 private:
  std::string _Data;
};

struct Time {
  // A point in time recurring on multiple days in the form
  // hh:mm:ss[Z|(+|-)hh:mm] (see [XML schema for
  // details](http://www.w3.org/TR/xmlschema-2/#time)).
};

}  // namespace DataType
}  // namespace SAGE
#endif  // !SAGE_DATATYPE_HPP