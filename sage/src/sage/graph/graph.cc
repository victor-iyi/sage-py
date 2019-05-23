#include "sage.hpp"

namespace sage {

  namespace graph {

    // A utility function that creates a graph of V vertices
    Graph* createGraph(int V) {
      Graph* graph = new Graph;
      graph->V = V;

      // Create an array of sets representing
      // adjacency lists.  Size of the array will be V
      graph->adjList = new std::set<int, std::greater<int> >[V];

      return graph;
    }

    // Adds an edge to an undirected graph
    void addEdge(Graph* graph, int src, int dest) {
      // Add an edge from src to dest.  A new
      // element is inserted to the adjacent
      // list of src.
      graph->adjList[src].insert(dest);

      // Since graph is undirected, add an edge
      // from dest to src also
      graph->adjList[dest].insert(src);
    }
    // To add an edge
    void addEdge(std::vector<std::pair<int, int> > adj[], int u, int v,
                 int wt) {
      adj[u].push_back(std::make_pair(v, wt));
      adj[v].push_back(std::make_pair(u, wt));
    }

    // Print adjacency list representation of graph
    void printGraph(std::vector<std::pair<int, int> > adj[], int V) {
      int v, w;
      for (int u = 0; u < V; u++) {
        SAGE_CORE_TRACE("Node {0} makes an edge with \n", u);
        for (auto it = adj[u].begin(); it != adj[u].end(); it++) {
          v = it->first;
          w = it->second;
          SAGE_CORE_TRACE("\tNode {0} with edge weight {1}", v, w);
        }
        std::cout << "\n";
      }
    }

    // Searches for a given edge in the graph
    void searchEdge(Graph* graph, int src, int dest) {
      auto itr = graph->adjList[src].find(dest);
      if (itr == graph->adjList[src].end())
        SAGE_CORE_ERROR("Edge from {0} to {1} not found.", src, dest);
      else
        SAGE_CORE_TRACE("Edge from {0} to {1} not found.", src, dest);
    }

  }  // namespace graph

}  // namespace sage