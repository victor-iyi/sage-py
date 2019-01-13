#include "sage/utils/fs.hpp"

namespace sage {

  // Constructors & destructor.
  File::~File() { this->close(); }

  // Instance methods.
  void File::close() { this->_m_FStream.close(); }
  auto File::load() { return NULL; }
  template <typename T>
  void File::dump(const T& obj) {}

  // Static methods.
  auto File::load(const std::string& path) { return NULL; }

  template <typename T>
  void File::dump(const T& obj, const std::string& path) {}

  bool File::exists(const std::string& path) { return false; }

  bool File::isDir(const std::string& path) { return false; }

  bool File::isFile(const std::string& path) { return false; }

}  // namespace sage