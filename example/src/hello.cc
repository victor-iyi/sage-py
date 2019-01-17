#include <iostream>
#include "sage.hpp"

int main() {

  if(sage::init() != SAGE_INIT_SUCCESS) {
    std::cout << "Could not initialize sage\n";
    // Could not initialize sage.
    exit(1);
  }

  // So sage stuff here.
  SAGE_INFO("This is fun!");
}
