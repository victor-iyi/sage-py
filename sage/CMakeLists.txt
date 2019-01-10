include_directories("include/" "vendor/spdlog/include" "vendor/json/include")

# Third-party libraries. add_subdirectory("vendor/spdlog")
find_package(spdlog CONFIG REQUIRED)
find_package(Threads REQUIRED)
find_package(nlohmann_json 3.2.0 REQUIRED)

file(GLOB_RECURSE SAGE_SRC "src/*.cc")
add_library(sage ${SAGE_SRC})
target_link_libraries(sage
                      spdlog::spdlog
                      Threads::Threads
                      nlohmann_json::nlohmann_json)
