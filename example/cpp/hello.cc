#include "sage.hpp"

int main() {
  if (sage::init() != SAGE_INIT_SUCCESS) {
    // Could not initialize sage.
    std::cout << "Could not initialize sage\n";
    exit(1);
  }
  // Path to a JSON-LD file.
  const char* const filepath =
      "/Users/victor/Documents/Work/NioCraft"
      "/sage/resources/cache/examples/avatar.jsonld";

  sage::graph::KnowledgeGraph g;
  g.load(filepath);
  std::cout << g.scope() << '\n';
}
