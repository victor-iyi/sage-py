include_directories("include/" "vendor/spdlog/include")

# Third-party libraries. add_subdirectory("vendor/spdlog")
find_package(spdlog CONFIG REQUIRED)
find_package(Threads REQUIRED)

file(GLOB_RECURSE SAGE_SRC "src/*.cc")
add_library(sage ${SAGE_SRC})
target_link_libraries(sage spdlog::spdlog Threads::Threads)
