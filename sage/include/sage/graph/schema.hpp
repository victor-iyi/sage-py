#ifndef SAGE_SCHEMA_HPP
#define SAGE_SCHEMA_HPP

#include "sage_pch.hpp"

namespace sage {

  namespace graph {

    struct Edge {
      // Edge's primary key.
      int id;

      // Vertex which the edge is connected to.
      std::string vertex_id;

      // Describing the connection `vertex` has with `vertex_id`.
      std::string predicate;

      // Source vertex (`vertex`) is connected to `vertex_id`.
      // Vertex vertex;

      Edge(const std::string& vertex_id, const std::string& predicate = "");

      bool operator==(const std::string& other);
    };

    struct Vertex {
      // Unique 8-bit token assigned to each Vertex.
      std::string id;
      // Vertex label.
      std::string label;
      // Vertex schema.
      std::string schema;
      // Payload which current vertex carries. Contains information about
      // Vertex.
      std::map<std::string, std::string> payload;
      // Connection of Vertex to other Vertex in the Graph.
      std::vector<Edge> edges;

      Vertex(const std::string& label = "Unknown",
             const std::string& schema = "Thing")
          : label("Unknown"), schema("Thing") {}

      // Comparision eq operator overload.
      bool operator==(const Vertex& other);
      // Comparision eq operator overload.
      bool operator==(const char* other);
      // Comparision eq operator overload.
      bool operator==(const std::pair<std::string, std::string>& other);

      // Add new connection to the current Vertex object with predicate.
      Edge* add_neighbor(const Vertex& nbr, const std::string& predicate = "");

      // Add payload to current Vertex. Appends if not already exists.
      void add_payload(const std::map<std::string, std::string> payload);

      // Get connection of current Vertex with a neighboring Vertex.
      const std::string& get_predicate(const Vertex& nbr) const;

      // Retrieve immediate connection to target vertex.
      Edge* get_connection(const Vertex& nbr) const;
    };

    class SAGE_API Graph {
     public:
      // Graph name.
      std::string name;

      // List of all vertex objects in Graph.
      std::vector<Vertex> vertices;

     public:
      Graph(const char* name) : name(name) {}

      // Add a new vertex/Node to the Graph if it doesn't already exist.
      Vertex* add_vertex(const std::string& label);
      Vertex* add_vertex(const std::string& label, const std::string& schema);

      // Retrieve a named vertex from the graph.
      Vertex* get_vertex(const Vertex& v) const;
      Vertex* get_vertex(const std::string& v) const;
      Vertex* get_vertex(const std::pair<std::string, std::string>& v) const;

      void close();
    };
  }  // namespace graph

}  // namespace sage
#endif  // !SAGE_SCHEMA_HPP