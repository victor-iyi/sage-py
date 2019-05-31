#ifndef SAGE_GRAPH_HPP
#define SAGE_GRAPH_HPP

#include "sage_pch.hpp"

namespace sage {

  namespace graph {

    class SAGE_API KnowledgeGraph {
     public:
      std::string name;

     public:
      KnowledgeGraph(const char* name);

      // Create KnowledgeGraph instance from file.
      KnowledgeGraph* fromfile(const char* path);

      // Read data from a given file.
      nlohmann::json read(const char* path);

      // Load knowledge data to Knowledge Graph.
      nlohmann::json load(nlohmann::json data);

      void close();
    };

  }  // namespace graph

}  // namespace sage

#endif  // !SAGE_GRAPH_HPP