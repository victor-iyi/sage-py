#include "sage/utils/fs.hpp"
#include "sage/error/error.hpp"

namespace sage {

  // Constructors & destructor.
  File::~File() { this->close(); }

  // Instance methods.
  void File::close() {
    if (this->_m_FStream.is_open()) this->_m_FStream.close();
  }

  // TODO: Returned obj allocated on the stack. Lifecycle has ended.
  template <typename T>
  T File::load() {
    if (!this->_m_FStream.is_open())
      throw error::IOError("Could not open file stream.");

    T t;
    this->_m_FStream.read(reinterpret_cast<char*>(&t), sizeof(t));
    return t;
  }

  std::string File::load() {
    if (!this->_m_FStream.is_open())
      throw error::IOError("Could open file stream.");

    std::string line;
    std::stringstream ss;
    while (getline(this->_m_FStream, line)) ss << line;
    return ss.str();
  }

  nlohmann::json File::loadJSON() {
    const std::string text = this->load();
    return nlohmann::json::parse(text);
  }

  template <typename T>
  void File::dump(const T& obj) {
    if (!this->_m_FStream.is_open())
      throw error::IOError("Could not open file stream.");

    this->_m_FStream.write(reinterpret_cast<char*>(&obj), sizeof(obj));
  }

  void File::dumpJSON(const nlohmann::json& j) {
    if (!this->_m_FStream.is_open())
      throw error::IOError("Could not open file stream.");

    try {
      this->_m_FStream << j.dump();
    } catch (const nlohmann::json::type_error& e) {
      SAGE_CORE_ERROR(e.what());
    }
  }

  /*
   * +----------------------------------------------------------------------+
   * | +------------------------------------------------------------------+ |
   * | | Static methods.
   * | +------------------------------------------------------------------+ |
   * +----------------------------------------------------------------------+
   */
  std::string File::load(const std::string& path) {
    if (!File::exists(path)) {
      SAGE_CORE_ERROR("{} does not exist!", path);
      return NULL;
    }

    std::ifstream inStream(path);
    if (!inStream.is_open())
      throw error::IOError("Could not open file stream.");

    std::string line;
    std::stringstream ss;
    while (getline(inStream, line)) ss << line;
    inStream.close();

    return ss.str();
  }

  // TODO: Return life time.
  template <typename T>
  T load(const std::string& path) {
    if (!File::exists(path)) {
      SAGE_CORE_ERROR("{} does not exist!", path);
      return;
    }

    std::ifstream inStream(path);
    if (!inStream.is_open())
      throw error::IOError("Could not open file stream.");

    T t;
    inStream.read(reinterpret_cast<char*>(&t), sizeof(t));
    inStream.close();

    return t;
  }

  template <typename T>
  void File::dump(const T& obj, const std::string& path) {
    std::ofstream outStream(path);
    if (!outStream.is_open())
      throw error::IOError("Could not open file stream.");

    outStream.write(reinterpret_cast<char*>(&obj), sizeof(obj));
    outStream.close();
  }

  bool File::exists(const std::string& path) {
    std::ifstream __stream(path);
    return __stream.good();
  }

  bool File::isDir(const std::string& path) { return false; }

  bool File::isFile(const std::string& path) {
    std::ifstream __stream(path);
    return __stream.good();
  }

}  // namespace sage