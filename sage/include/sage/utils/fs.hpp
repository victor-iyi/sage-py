#ifndef SAGE_FS_HPP
#define SAGE_FS_HPP

#include "sage_pch.hpp"

namespace sage {

  /*
   * +----------------------------------------------------------------------+
   * | +------------------------------------------------------------------+ |
   * | | Base classes.
   * | +------------------------------------------------------------------+ |
   * +----------------------------------------------------------------------+
   */
  class _FS_Base {
   public:
    std::string path;

    _FS_Base(const std::string& path) : path(path) {}
    virtual ~_FS_Base();

    std::string& getPath() const;

    template <typename... T>
    std::string join(T... t) {
      using namespace std::string_literals;

      typename std::common_type<T...>::type result{};
      (void)std::initializer_list<std::string>{(result += t, ""s)...};
      return result;
      // return (t + ...);
    }

    void close();
    bool isFile() const;
    bool isDir() const;
    bool exists() const;
  };

  /*
   * +----------------------------------------------------------------------+
   * | +------------------------------------------------------------------+ |
   * | | File class.
   * | +------------------------------------------------------------------+ |
   * +----------------------------------------------------------------------+
   */
  class SAGE_API File : public _FS_Base {
    /* Example:
    ```cpp
      File f;
      json obj = f.load("path");
      f.close();

      File f2("path/to/file.jsonld");
      json obj = f2.load();
      f.dump<json>(obj, "path/to/file.jsonld");
      f2.close();
    ```
    */
   public:
    File() = default;
    File(const char* const path) : _FS_Base(path) {}
    virtual ~File() override;

    auto load();
    auto load(const char* const path);

    template <typename T>
    void dump(T obj);
    template <typename T>
    void dump(T obj, const char* const path);
  };

  // sage::mkdir("path/to/directory");
  inline void mkdir(const std::string& __dir) {
    using namespace std::string_literals;

#ifdef SAGE_PLATFORM_WINDOWS
    // Windows creation of directory.
    std::system(("mkdir -p "s + __dir).c_str());
#else
    // Unix way of creating directory.
    std::system(("mkdir -p "s + __dir).c_str());
#endif
  }

}  // namespace sage

#endif  // !SAGE_FS_HPP