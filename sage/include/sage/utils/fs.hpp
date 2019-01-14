#ifndef SAGE_FS_HPP
#define SAGE_FS_HPP

#include "sage_pch.hpp"

namespace sage {

  class SAGE_API File {
   private:
    std::string _m_Path;      // Path string.
    std::fstream _m_FStream;  // File stream object.
    bool _m_Binary;           // Write & read file as binary.

   public:
    // Constructors.
    File(const std::string& path)
        : _m_Path(path), _m_FStream(path), _m_Binary(false) {}
    File(const std::string& path, bool binary)
        : _m_Path(path),
          _m_FStream(path, std::ios::in | std::ios::out | std::ios::binary),
          _m_Binary(binary) {}
    virtual ~File();

    // Instance methods.
    void close();

    template <typename T>
    T load();
    std::string load();
    nlohmann::json loadJSON();

    template <typename T>
    void dump(const T& obj);

    // void dumpJSON(const );

    // Static (Class) methods.
    static std::string load(const std::string& path);
    template <typename T>
    static T load(const std::string& path);

    template <typename T>
    static void dump(const T& obj, const std::string& path);

    static bool exists(const std::string& path);
    static bool isDir(const std::string& path);
    static bool isFile(const std::string& path);

    inline static void mkdir(std::string& path) {
      using namespace std::string_literals;
#ifdef SAGE_PLATFORM_WINDOWS
// Create directory the windows way...
#else
      // Create directory the UNIX way...
      std::system(("mkdir -p "s + path).c_str());
#endif
    }
  };

}  // namespace sage

#endif  // !SAGE_FS_HPP