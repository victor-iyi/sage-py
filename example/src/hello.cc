#include "sage.hpp"

int main() {

  if(sage::init() != SAGE_INIT_SUCCESS) {
    std::cout << "Could not initialize sage\n";
    // Could not initialize sage.
    exit(1);
  }

  using json = nlohmann::json;

  const char* const filepath = "/Users/victor/Documents/Work/NioCraft/sage/build/test.jsonld";

  sage::File f(filepath);
  json content = f.loadJSON();
  std::cout << content.dump() << '\n';

  // So sage stuff here.
  // SAGE_WARN("This is fun!");
}
