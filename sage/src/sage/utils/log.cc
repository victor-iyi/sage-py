#include "sage/utils/log.hpp"
#include "spdlog/sinks/stdout_color_sinks.h"

namespace sage {

  std::shared_ptr<spdlog::logger> Log::s_CoreLogger;
  std::shared_ptr<spdlog::logger> Log::s_ClientLogger;

  void Log::init() {
    // Log pattern.
    spdlog::set_pattern("%^[%T] %n: %v%$");

    // Core logger.
    s_CoreLogger = spdlog::stdout_color_mt("SAGE_CORE");
    s_CoreLogger->set_level(spdlog::level::trace);

    // Client logger.
    s_ClientLogger = spdlog::stdout_color_mt("SAGE");
    s_ClientLogger->set_level(spdlog::level::trace);
  }

}  // namespace sage