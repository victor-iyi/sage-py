#include <iostream>
#include "sage.hpp"

int main() {

  if(sage::init() != SAGE_INIT_SUCCESS) {
    // Could not initialize sage.
    exit(1);
  }

  // So sage stuff here.

}
