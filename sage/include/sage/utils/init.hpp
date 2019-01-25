#ifndef SAGE_INIT_HPP
#define SAGE_INIT_HPP

#include "sage/core.hpp"

namespace sage {
  // Initialization code for sage.
  int SAGE_API init();

}  // namespace sage

#define SAGE_INIT_SUCCESS 1
#define SAGE_INIT_FAILURE 0

#endif  // !SAGE_INIT_HPP