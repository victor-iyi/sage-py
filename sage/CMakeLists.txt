include_directories("include/")

# Third-party libraries.
# add_subdirectory("vendor/spdlog")

file(GLOB_RECURSE SAGE_SRC "src/*.cc")
add_library(sage ${SAGE_SRC})
# target_link_libraries(sage spdlog)
