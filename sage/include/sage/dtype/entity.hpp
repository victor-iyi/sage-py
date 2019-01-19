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
    class SAGE_API Entity {
     public:
      Entity() = default;

      explicit Entity(const Text& value) : _m_Value(value) {}
      explicit Entity(const std::string& value) : _m_Value(value) {}
      explicit Entity(const char* const value) : _m_Value(value) {}

      virtual ~Entity() {}

      const Text& value() const { return _m_Value; }

      friend bool operator<(const Entity& lhs, const Entity& rhs) {
        return lhs._m_Value < rhs._m_Value;
      }
      friend bool operator>(const Entity& lhs, const Entity& rhs) {
        return rhs < lhs;
      }
      friend bool operator<=(const Entity& lhs, const Entity& rhs) {
        return !(lhs > rhs);
      }
      friend bool operator>=(const Entity& lhs, const Entity& rhs) {
        return !(lhs < rhs);
      }
      friend bool operator==(const Entity& lhs, const Entity& rhs) {
        return lhs._m_Value == rhs._m_Value;
      }
      friend bool operator!=(const Entity& lhs, const Entity& rhs) {
        return !(lhs == rhs);
      }

      friend std::ostream& operator<<(std::ostream& out, const Entity& t) {
        out << t._m_Value;
        return out;
      }

     private:
      Text _m_Value;
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
    class SAGE_API Scope : public Entity {
     public:
      Scope(const std::map<Text, Entity>& properties)
          : _m_Property(properties) {}

      virtual ~Scope() override {}

      const std::map<Text, Entity>& getProperty() const { return _m_Property; }
      const Text& getID() const { return _m_MachineID; }
      const Text& getType() const { return _m_Type; }

      const std::map<Text, Entity>::const_iterator begin() const {
        return _m_Property.begin();
      }
      const std::map<Text, Entity>::const_iterator end() const {
        return _m_Property.end();
      }

      bool has(const Text& key) const {
        auto _found = _m_Property.find(key);
        return (_found != _m_Property.end());
      }

     private:
      // Unique identification of this scope in the graph.
      const Text _m_MachineID;
      // Should have a property of `"@type": "Text"`.
      const Text _m_Type;
      // Should have a property of dtype::Text: dtype::Entity`.
      std::map<Text, Entity> _m_Property;
    };

  }  // namespace dtype

}  // namespace sage

#endif  // !SAGE_GRAPH_HPP