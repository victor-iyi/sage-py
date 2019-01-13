#ifndef SAGE_MAPPING_HPP
#define SAGE_MAPPING_HPP

#include "sage/error/error.hpp"
#include "sage_pch.hpp"

namespace sage {

  template <typename T>
  struct NamedPair {
    using value_type = T;
    const T value;
    const char* const name;
  };

  // typename M: is some type of standard container that supports `find_if()`.
  // typename V: is the type of the enum whose value we wish to look up.
  template <typename M, typename V>
  std::string getNameForValue(M m, V value) {
    // pos is an iterator of M.
    auto pos = std::find_if(std::begin(m), std::end(m),
                            [&value](const typename M::value_type& t) {
                              return (t.value == value);
                            });

    if (pos != std::end(m)) return pos->name;

    throw error::UnknownValueError(static_cast<int>(value));
    // Or return some default value here.
    // return M::value_type::value_type();
  }

  template <typename M>
  typename M::value_type::value_type getValueForName(M m,
                                                     const std::string& name) {
    auto pos = std::find_if(
        std::begin(m), std::end(m),
        [&name](const typename M::value_type& t) { return (t.name == name); });

    if (pos != std::end(m)) return pos->value;

    throw error::UnknownValueError(name);
    // Or return an empty string (or default name).
  }

}  // namespace sage

#endif  // SAGE_MAPPING_HPP
