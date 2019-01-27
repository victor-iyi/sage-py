#include "sage/graph/graph.hpp"
#include "sage/utils/fs.hpp"

namespace sage {

  namespace graph {
    // template<typename Args&&...>
    void Scope::addNode(const char* const key, const char* const value) {
      this->_m_Connections.emplace_back(key, value, false);
    }
    void Scope::addScope(const char* const key) {
      this->_m_Connections.push_back(std::move(Scope(key)));
    }

    void KnowledgeGraph::load(const char* const path) {
      // TODO: Validate `path` is a JSON-LD file.
      sage::File f(path);
      // Read the JSON-LD data from disk.
      const nlohmann::json data = f.loadJSON();
      // Load the JSON data.
      this->load(this->_m_Root, data);
    }

    // A recursive method.
    void KnowledgeGraph::load(Scope& base, const nlohmann::json& data) {
      for (const auto& content : data.items()) {
        if (content.value().is_structured()) {
          // At this point, we're a scope.
          base.addScope(content.key().c_str());
          // this->load(base, content.value());
        } else {
          // Just a node, no biggie.
          // Remove quotes (") from begining & end of the string.
          std::string value = content.value().dump();
          // TODO: Find a better way to do this.
          value.erase(std::find(value.begin(), value.end(), '"'));
          value.erase(std::find(value.begin(), value.end(), '"'));
          // Add node to "base".
          base.addNode(content.key().c_str(), value.c_str());
        }
      }
    }
  }  // namespace graph

}  // namespace sage