#ifndef SAGE_GRAPH_HPP
#define SAGE_GRAPH_HPP

#include "sage/dtype/dtype.hpp"

namespace sage {

  namespace graph {

    class SAGE_API Node {
     public:
     Node(const char* const key, const char* const value, bool isScope) :  _m_IsScope(isScope), _m_Key(key) {
       if (isScope) {
         this->_m_Value = dtype::Scope(value);
       }else {
         this->_m_Value = dtype::Entity(value);
       }
     }

      bool isScope() const { return this->_m_IsScope; }
      const dtype::Text& key() const { return this->_m_Key; }
      const dtype::Entity& value() const { return this->_m_Value; }

     private:
      bool _m_IsScope;
      dtype::Text _m_Key;
      dtype::Entity _m_Value;
    };

    class SAGE_API KnowledgeGraph {
     public:
      void load(const char* const path);
      void load(const nlohmann::json& data);

     private:
    };

  }  // namespace graph

}  // namespace sage

#endif  // !SAGE_GRAPH_HPP