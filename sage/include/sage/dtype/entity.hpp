#ifndef SAGE_DTYPE_ENTITY_HPP
#define SAGE_DTYPE_ENTITY_HPP

#include "sage/dtype/base.hpp"
#include "sage_pch.hpp"

namespace sage {

  namespace dtype {
    /**
     * Entity represents the value of property, which can be a Type or a Scope.
     * Example:
     * {
     *  "@context": "https://schema.org",
     *  "@type": "Movie",
     *  "cause": [
     *    {...},
     *  ],
     *  "director": {
     *    "@type": "Person",
     *    "name": "James Cameron",
     *    ...
     *  },
     * ...
     * }
     *
     * Entity in these cases are "Movie", [], { }
     * */
    template <typename T>
    class SAGE_API Entity {
     public:
      Entity(const T& value);
      virtual ~Entity() {}

     private:
      dtype::Type<T> _m_Value;
    };

    /**
     * Property is a mapping between a string and an Entity.
     * Example:
     * ```json
     * {
     *  "@type": "Movie",
     *  "name": "Avatar",
     *  "cause": [
     *    {...},
     *  ]
     * }
     * ```
     *  Each line represent a different property.
     * */
    template <typename V>
    class SAGE_API Property {
     public:
      Property() = default;
      ~Property();

     private:
      // `"@type": "Movie"`, `"name": "Avatar"`, etc...
      std::unordered_map<dtype::Text, Entity<V>> _m_Map;
    };

    /**
     * A Scope is simply an Entity of type Property i.e Entity<Property<Type>>
     * ```
     *  director: {
     *   "@type": "Person",                    # 1. Property<Text, Type<Text>>
     *   "name": "James Cameron",              # 2. Property<Text, Type<Text>>
     *   "trailer": "https://link/trailer.mp4" # 3. Property<Text, Type<URL>>
     *   ...
     * }
     * ```
     * */
    template <typename V>
    class SAGE_API Scope : public Entity<V> {
     public:
      Scope() {
        // Generates a unique machine code.
        // A map or a list of properties which can be constructed emplace.
      }
      virtual ~Scope() override {}

     private:
      const std::string _m_MachineID;
      // Should have a property of `"@type": "dtype::Text"`.
      std::vector<Property<V>> _m_Value;
    };

  }  // namespace dtype

}  // namespace sage

#endif  // !SAGE_GRAPH_HPP