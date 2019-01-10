#include "sage/datatype.hpp"

namespace sage {

namespace DataType {
/*
 * +----------------------------------------------------------------------+
 * | +------------------------------------------------------------------+ |
 * | | Boolean: True or False.
 * | +------------------------------------------------------------------+ |
 * +----------------------------------------------------------------------+
 */
Boolean::Boolean(bool _Boolean) : _Data(_Boolean) {}

/*
 * +----------------------------------------------------------------------+
 * | +------------------------------------------------------------------+ |
 * | | A combination of date and time of day in the form
 * | | [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] (see Chapter 5.4 of ISO 8601).
 * | +------------------------------------------------------------------+ |
 * +----------------------------------------------------------------------+
 */
DateTime::DateTime(const std::time_t& _DateTime) {
  const std::tm t = *std::localtime(&_DateTime);
  this->_Data = this->dateTimeToString(t, "");
}
DateTime::DateTime(const char* _DateTime) : _Data(_DateTime) {}

std::string DateTime::dateTimeToString(const std::tm& t, const char* format) {
  std::stringstream s;
  this->formatDateTime(s, t, format);
  return s.str();
}

std::ostream& DateTime::formatDateTime(std::ostream& out, const std::tm& t,
                                       const char* fmt) {
  const std::time_put<char>& dateWriter =
      std::use_facet<std::time_put<char> >(out.getloc());
  size_t n = strlen(fmt);
  if (dateWriter.put(out, out, ' ', &t, fmt, fmt + n).failed()) {
    SAGE_CORE_ERROR("Failure to format datetime");
  }
  return out;
}

std::tm DateTime::now() {
  std::time_t now = std::time(0);
  return *std::localtime(&now);
}

/*
 * +----------------------------------------------------------------------+
 * | +------------------------------------------------------------------+ |
 * | | Data type: Text.
 * | +------------------------------------------------------------------+ |
 * +----------------------------------------------------------------------+
 */
Text::Text(std::string _Text) : _Data(_Text) {}
Text::Text(std::string& _Text) : _Data(_Text) {}
Text::Text(const char* _Text) : _Data(_Text) {}
}  // namespace DataType
}  // namespace sage