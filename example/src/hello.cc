#include "sage.hpp"

int main() {
  if (sage::init() != SAGE_INIT_SUCCESS) {
    // Could not initialize sage.
    std::cout << "Could not initialize sage\n";
    exit(1);
  }

  using json = nlohmann::json;

  const char* const filepath =
      "/Users/victor/Documents/Work/"
      "NioCraft/sage/build/test.jsonld";

  sage::File f(filepath);
  json contents = f.loadJSON();
  std::cout << contents.dump() << '\n';

  for (const auto& content : contents.items()) {
    std::cout << "Key: " << content.key();
    std::cout << "\tValue: " << content.value() << '\n';
  }

}
