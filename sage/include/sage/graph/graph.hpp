#ifndef SAGE_GRAPH_HPP
#define SAGE_GRAPH_HPP

#include "sage/dtype/dtype.hpp"

namespace sage {

  namespace graph {

    class SAGE_API Scope;
    std::ostream& operator<<(std::ostream& stream, const Scope& scope);

    /**
     * Node class
     *
     * */
    class SAGE_API Node {
     public:
      Node(const char* const key, bool isScope = false)
          : _m_IsScope(isScope), _m_Key(key), _m_Value("") {}
      Node(const char* const key, const char* const value, bool isScope = false)
          : _m_IsScope(isScope), _m_Key(key), _m_Value(value) {}

      Node(const Node& other)
          : _m_IsScope(other._m_IsScope),
            _m_Key(other._m_Key),
            _m_Value(other._m_Value) {}

      inline bool isScope() const { return this->_m_IsScope; }
      const dtype::Text& key() const { return this->_m_Key; }
      const dtype::Text& value() const { return this->_m_Value; }

      friend std::ostream& operator<<(std::ostream& stream, const Node& node) {
        // key : value
        // TODO: If node is a Scope: Call the scope operator<<.
        // if (node._m_IsScope) {
        //   graph::Scope* s = (graph::Scope*)&node;
        //   stream << s;
        // } else
        stream << '"' << node._m_Key << "\" : " << node._m_Value;
        return stream;
      }

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

      void addNode(const char* const key, const char* const value);
      void addScope(const char* const key);
      void addScope(const Scope& scope);

      const std::vector<Node>& getConnections() const {
        return this->_m_Connections;
      }
      const dtype::Text& id() const { return this->_m_MachineID; }

      friend std::ostream& operator<<(std::ostream& stream,
                                      const Scope& scope) {
        // key<ID> : {
        //  key:value
        // }
        stream << scope.key() << '<' << scope._m_MachineID << "> : {\n";
        for (const Node& node : scope._m_Connections) {
          // if (node.isScope()) {
          //   // print as a scope.
          //   stream << std::setw(4) << node.key() << '\n';
          // } else
          // Print as a node.
          stream << std::setw(4) << node << '\n';
        }
        stream << '}';
        return stream;
      }

     private:
      dtype::Text _m_MachineID;
      std::vector<Node> _m_Connections;
    };

    /**
     * Knowledge Graph.
     */
    class SAGE_API KnowledgeGraph {
     public:
      KnowledgeGraph() : _m_Root("ns") {}
      void load(const char* const path);
      void load(Scope& base, const nlohmann::json& data);

      const Scope& scope() const { return this->_m_Root; }

     private:
      Scope _m_Root;
    };

  }  // namespace graph

}  // namespace sage

#endif  // !SAGE_GRAPH_HPP