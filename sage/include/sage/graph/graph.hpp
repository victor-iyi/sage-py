#ifndef SAGE_GRAPH_HPP
#define SAGE_GRAPH_HPP

#include "sage_pch.hpp"

namespace sage {

  namespace graph {

    class SAGE_API KG {
     public:
      std::string name;

     public:
      KG(const char* name);

      // Create KG instance from file.
      KG* fromfile(const char* path);

      // Read data from a given file.
      nlohmann::json read(const char* path);

      // Load knowledge data to Knowledge Graph.
      nlohmann::json load(nlohmann::json data);

      void close();
    };

  }  // namespace graph

}  // namespace sage

#endif  // !SAGE_GRAPH_HPP