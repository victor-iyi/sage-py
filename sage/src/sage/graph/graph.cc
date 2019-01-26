#include "sage/graph/graph.hpp"
#include "sage/utils/fs.hpp"

namespace sage {

  namespace graph {
    // template<typename Args&&...>
    void Scope::emplace(const char* const key, const char*const value, bool is_scope) {
      this->_m_Connections.emplace_back(key, value, is_scope);
    }
    void Scope::addNode(const char* key, const char* value) {
      this->_m_Connections.emplace_back(key, value, false);
    }
    void Scope::addScope(const char * key) {this->_m_Connections.emplace_back(key);}

    void KnowledgeGraph::load(const char* const path) {
      // TODO: Validate `path` is a JSON-LD file.
      sage::File f(path);
      // Read the JSON-LD data from disk.
      const nlohmann::json data = f.loadJSON();
      // Load the JSON data.
      this->load(data);
    }

    // A recursive method.
    void KnowledgeGraph::load(const nlohmann::json& data) {
      for (const auto& content : data.items()) {
        if (content.value().is_structured()) {
          // At this point, we're a scope.
          Scope scope(content.key().c_str());
        } else {
          // Just a node, no biggie.
          this->_m_Root.addNode(content.key().c_str(), content.key().c_str());
        }
      }
    }
  }  // namespace graph

}  // namespace sage