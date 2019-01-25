#include "sage/utils/init.hpp"
#include "sage/utils/log.hpp"
#include "sage/dtype/dtype.hpp"

namespace sage {

  int init() {
    try {
      // Initialize logging.
      Log::init();
      SAGE_CORE_INFO("Initialized logger!");

    } catch (...) {
      // Initialization failed.
      return SAGE_INIT_FAILURE;
    }

    return SAGE_INIT_SUCCESS;
  }

}  // namespace sage