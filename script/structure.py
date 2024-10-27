import os

def create_directory_structure(base_dir="../../titan"):
    # Define the directory structure
    directories = [
        f"{base_dir}/src/Engine/ECS",
        f"{base_dir}/src/Engine/Renderer",
        f"{base_dir}/src/Engine/Core",
        f"{base_dir}/include/Engine/ECS",
        f"{base_dir}/include/Engine/Renderer",
        f"{base_dir}/include/Engine/Core"
    ]

    # Create each directory in the list
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")

    # Create main.cpp and CMakeLists.txt
    main_cpp_path = os.path.join(base_dir, "src", "main.cpp")
    cmake_lists_path = os.path.join(base_dir, "CMakeLists.txt")

    # Write placeholder content for main.cpp
    with open(main_cpp_path, "w") as main_cpp_file:
        main_cpp_file.write("// main.cpp\nint main() {\n    return 0;\n}\n")
    print(f"Created file: {main_cpp_path}")

    # Write placeholder content for CMakeLists.txt
    with open(cmake_lists_path, "w") as cmake_file:
        cmake_file.write("# CMakeLists.txt\ncmake_minimum_required(VERSION 3.10)\n")
    print(f"Created file: {cmake_lists_path}")

# Run the function
create_directory_structure()
