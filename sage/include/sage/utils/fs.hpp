#ifndef SAGE_FS_HPP
#define SAGE_FS_HPP

#include "sage_pch.hpp"

namespace sage {

  class SAGE_API File {
   private:
    std::string _m_Path;      // Path string.
    std::fstream _m_FStream;  // File stream object.

   public:
    // Constructors.
    File(const std::string& path) : _m_Path(path) {
      // Open file stream;
      _m_FStream.open(path, std::ios::in | std::ios::out);
    }
    virtual ~File();

    // Instance methods.
    void close();
    auto load();
    template <typename T>
    void dump(const T& obj);

    // Static (Class) methods.
    static auto load(const std::string& path);
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