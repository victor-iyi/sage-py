#include "sage.hpp"

int main() {
  if (sage::init() != SAGE_INIT_SUCCESS) {
    // Could not initialize sage.
    std::cout << "Could not initialize sage\n";
    exit(1);
  }


  const char* const filepath =
      "/Users/victor/Documents/Work/"
      "NioCraft/sage/build/test.jsonld";
  sage::graph::KnowledgeGraph g;
  g.load(filepath);
  std::cout << g.scope() << '\n';
  // using json = nlohmann::json;
  // sage::File f(filepath);
  // json contents = f.loadJSON();
  // std::cout << contents.dump() << '\n';

  // for (const auto& content : contents.items()) {
  //   std::cout << "Key: " << content.key();
  //   std::cout << "\tValue: " << content.value() << '\n';
  // }

}
