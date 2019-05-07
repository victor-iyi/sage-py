#ifndef SAGE_GRAPH_HPP
#define SAGE_GRAPH_HPP

#include "sage_pch.hpp"

namespace sage {

  namespace graph {

    struct Graph {
      int V;
      std::set<int, std::greater<int> >* adjList;
    };

    // A utility function that creates a graph of V vertices
    Graph* createGraph(int V);

    // To add an edge
    void addEdge(std::vector<std::pair<int, int> > adj[], int u, int v, int wt);

    // Adds an edge to an undirected graph
    void addEdge(Graph* graph, int src, int dest);

    void printGraph(std::vector<std::pair<int, int> > adj[], int V);

    void searchEdge(Graph* graph, int src, int dest);

  }  // namespace graph
}  // namespace sage

#endif  // !SAGE_GRAPH_HPP