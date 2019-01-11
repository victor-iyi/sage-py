#ifndef SAGE_ENTITY_HPP
#define SAGE_ENTITY_HPP

#include "sage/dtype/dtype.hpp"
#include "sage_pch.hpp"

namespace sage {

  namespace entity {
    /*
      Entity represents the value of a property.
      Example:
      {
        "@context": "https://schema.org"
        "@type": "Movie",
        "cause": [
          {...},
        ],
        "director": {
          "@type": "Person",
          "name": "James Cameron",
          ...
        },
        ...
      }

      Entity in these cases are: "Movie", [], { }...
    */
    template <typename T>
    class SAGE_API Entity {
     public:
      Entity(const T& value);
      virtual ~Entity() {}

     private:
      dtype::Type<T> _m_Value;
    };

    template <typename V>
    class SAGE_API Property {
     public:
      Property() = default;
      ~Property();

     private:
      // `"@type": "Movie"`, `"name": "Avatar"`, etc...
      std::unordered_map<dtype::Text, Entity<V>> _m_Map;
    };

    /*
      A Scope is simply an Entity of type Property i.e Entity<Property<Type>>
      ```
      director: {
        "@type": "Person",                      # 1. Property<Text, Type<Text>>
        "name": "James Cameron",                # 2. Property<Text, Type<Text>>
        "trailer": "https://link/trailer.mp4",  # 3. Property<Text, Type<URL>>
        ...
      }
      ```
    */
    template <typename V>
    class SAGE_API Scope : public Entity<V> {
     public:
      Scope() {
        // generates a unique machine code.
        // a map or a list of properties which can be constructed emplace.
      }
      virtual ~Scope() override {}

     private:
      const std::string _m_MachineID;
      // Should have a property of `"@type": "..."`.
      std::vector<Property<V>> _m_Value;
      // Entity<std::vector<Property<dtype::Type<V>>>> _m_Scope;
    };

  }  // namespace entity

}  // namespace sage

#endif  // !SAGE_GRAPH_HPP