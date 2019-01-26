#ifndef SAGE_GRAPH_HPP
#define SAGE_GRAPH_HPP

#include "sage/dtype/dtype.hpp"

namespace sage {

  namespace graph {
    /**
     * Node class
     *
     * */
    class SAGE_API Node {
     public:
      Node(const char* const key, bool isScope = false)
          : _m_IsScope(isScope), _m_Key(key), _m_Value(nullptr) {}
      Node(const char* const key, const char* const value, bool isScope = false)
          : _m_IsScope(isScope), _m_Key(key), _m_Value(value) {}

      Node(const Node& other) : _m_IsScope(other._m_IsScope), _m_Key(other._m_Key), _m_Value(other._m_Value) {}

      bool isScope() const { return this->_m_IsScope; }
      const dtype::Text& key() const { return this->_m_Key; }
      const dtype::Text& value() const { return this->_m_Value; }

     private:
      bool _m_IsScope;  // If this node is a Scope, it has children.
      dtype::Text _m_Key;
      dtype::Text _m_Value;  // Could be empty at times.
    };

    /**
     * Scope class
     * */
    class SAGE_API Scope : public Node {
     public:
      Scope(const char* const key) : Node(key, true) {}

      void emplace(const char* const key, const char* const value, bool is_scope);
      void addNode(const char* const key, const char* const value);
      void addScope(const char* const key);

      const std::vector<Node*>& getConnections() const {
        return this->_m_Connections;
      }
      const dtype::Text& id() const { return this->_m_MachineID; }

     private:
      dtype::Text _m_MachineID;
      std::vector<Node*> _m_Connections;
    };

    /**
     * Knowledge Graph.
     * */
    class SAGE_API KnowledgeGraph {
     public:
      KnowledgeGraph() = default;
      void load(const char* const path);
      void load(const nlohmann::json& data);

     private:
      Scope _m_Root;
    };

  }  // namespace graph

}  // namespace sage

#endif  // !SAGE_GRAPH_HPP