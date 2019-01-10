#include "sage/datatype.hpp"

namespace sage {
// Boolean
DataType::Boolean::Boolean(bool _Boolean) : _Data(_Boolean) {}

// Text
DataType::Text::Text(std::string _Text) : _Data(_Text) {}
DataType::Text::Text(std::string& _Text) : _Data(_Text) {}
DataType::Text::Text(const char* _Text) : _Data(_Text) {}
}  // namespace SAGE