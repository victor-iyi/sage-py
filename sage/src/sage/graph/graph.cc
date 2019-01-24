#include "sage/graph/graph.hpp"
#include "sage/utils/fs.hpp"

namespace sage {

  namespace graph {

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
          // It's either an array or object (Another Scope).
          this->load(content.value()); // Recurse.
        } else {
          // It's part of current scope.
        }
      }

    }
  }

}  // namespace sage