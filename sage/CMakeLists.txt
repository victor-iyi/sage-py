# Set Boost Environment vars.
# if(NOT DEFINED BOOST_ROOT
#    AND NOT DEFINED ENV{BOOST_ROOT}
#    AND NOT DEFINED BOOST_INCLUDEDIR
#    AND NOT DEFINED ENV{BOOST_INCLUDEDIR}
#    AND NOT DEFINED BOOST_LIBRARYDIR
#    AND NOT DEFINED ENV{BOOST_LIBRARYDIR})
#   if(APPLE)
#     set(BOOST_ROOT "vendor/boost")
#   elseif(WIN32)
#     set(BOOST_INCLUDEDIR "C:/local/boost_1_55_0")
#     set(BOOST_LIBRARYDIR "C:/local/boost_1_55_0/lib32-msvc-10.0")
#   endif()
# endif()
# if(APPLE OR WIN32)
#   set(Boost_USE_STATIC_LIBS TRUE)
# endif()

# Third-party libraries. add_subdirectory("vendor/spdlog")
find_package(spdlog CONFIG REQUIRED)
# find_package(Threads REQUIRED)
# find_package(Boost 1.32 REQUIRED COMPONENTS program_options)
find_package(Boost 1.32 REQUIRED)

if(SAGE_USE_EXTERNAL_JSON)
  # Use external JSON
  find_package(nlohmann_json 3.2.0 REQUIRED)
else()
  # Use JSON in submodule.
  set(JSON_BuildTests OFF CACHE INTERNAL "")
  add_subdirectory("vendor/json")
endif()

include_directories(SYSTEM
                    "include/"
                    "vendor/spdlog/include"
                    "vendor/json/include"
                    "${Boost_INCLUDE_DIRS}")

file(GLOB_RECURSE SAGE_SRC "src/*.cc")
add_library(sage ${SAGE_SRC})
target_link_libraries(sage
                      spdlog::spdlog
                      # Threads::Threads
                      nlohmann_json::nlohmann_json
                      ${Boost_LIBRARIES})
