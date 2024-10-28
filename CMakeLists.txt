cmake_minimum_required(VERSION 3.10)
project(titan)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)  # Ensure that the standard is required

# Include directories for header files
include_directories(include)

# Gather all source files
file(GLOB_RECURSE SOURCES "src/*.cpp" "src/Engine/**/*.cpp")

# Add the executable target
add_executable(titan ${SOURCES})

# Optionally, link any libraries here if needed
# target_link_libraries(titan your_library_name)
