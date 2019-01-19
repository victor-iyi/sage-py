#include "sage.hpp"

int main() {
  if (sage::init() != SAGE_INIT_SUCCESS) {
    // Could not initialize sage.
    std::cout << "Could not initialize sage\n";
    exit(1);
  }

  using json = nlohmann::json;

  const char* const filepath =
      "/Users/victor/Documents/Work/NioCraft/sage/build/test.jsonld";

  sage::File f(filepath);
  json content = f.loadJSON();
  std::cout << content.dump() << '\n';

  // TODO: Not working. Assignment lifetype.
  // Create a copy constructor.
  sage::dtype::Text text;
  text = "Victor I. Afolabi";
  std::cout << "Name: " << text << '\n';

  // So sage stuff here.
  // SAGE_WARN("This is fun!");
}
