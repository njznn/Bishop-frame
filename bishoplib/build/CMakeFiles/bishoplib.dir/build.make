# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ziga/Desktop/FMF_delo/bishoplib

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ziga/Desktop/FMF_delo/bishoplib/build

# Include any dependencies generated for this target.
include CMakeFiles/bishoplib.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/bishoplib.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/bishoplib.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/bishoplib.dir/flags.make

CMakeFiles/bishoplib.dir/src/bishop.cpp.o: CMakeFiles/bishoplib.dir/flags.make
CMakeFiles/bishoplib.dir/src/bishop.cpp.o: ../src/bishop.cpp
CMakeFiles/bishoplib.dir/src/bishop.cpp.o: CMakeFiles/bishoplib.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ziga/Desktop/FMF_delo/bishoplib/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/bishoplib.dir/src/bishop.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/bishoplib.dir/src/bishop.cpp.o -MF CMakeFiles/bishoplib.dir/src/bishop.cpp.o.d -o CMakeFiles/bishoplib.dir/src/bishop.cpp.o -c /home/ziga/Desktop/FMF_delo/bishoplib/src/bishop.cpp

CMakeFiles/bishoplib.dir/src/bishop.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/bishoplib.dir/src/bishop.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/ziga/Desktop/FMF_delo/bishoplib/src/bishop.cpp > CMakeFiles/bishoplib.dir/src/bishop.cpp.i

CMakeFiles/bishoplib.dir/src/bishop.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/bishoplib.dir/src/bishop.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/ziga/Desktop/FMF_delo/bishoplib/src/bishop.cpp -o CMakeFiles/bishoplib.dir/src/bishop.cpp.s

# Object files for target bishoplib
bishoplib_OBJECTS = \
"CMakeFiles/bishoplib.dir/src/bishop.cpp.o"

# External object files for target bishoplib
bishoplib_EXTERNAL_OBJECTS =

libbishoplib.so.1.0.1: CMakeFiles/bishoplib.dir/src/bishop.cpp.o
libbishoplib.so.1.0.1: CMakeFiles/bishoplib.dir/build.make
libbishoplib.so.1.0.1: CMakeFiles/bishoplib.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/ziga/Desktop/FMF_delo/bishoplib/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library libbishoplib.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/bishoplib.dir/link.txt --verbose=$(VERBOSE)
	$(CMAKE_COMMAND) -E cmake_symlink_library libbishoplib.so.1.0.1 libbishoplib.so.1.0.1 libbishoplib.so

libbishoplib.so: libbishoplib.so.1.0.1
	@$(CMAKE_COMMAND) -E touch_nocreate libbishoplib.so

# Rule to build all files generated by this target.
CMakeFiles/bishoplib.dir/build: libbishoplib.so
.PHONY : CMakeFiles/bishoplib.dir/build

CMakeFiles/bishoplib.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/bishoplib.dir/cmake_clean.cmake
.PHONY : CMakeFiles/bishoplib.dir/clean

CMakeFiles/bishoplib.dir/depend:
	cd /home/ziga/Desktop/FMF_delo/bishoplib/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ziga/Desktop/FMF_delo/bishoplib /home/ziga/Desktop/FMF_delo/bishoplib /home/ziga/Desktop/FMF_delo/bishoplib/build /home/ziga/Desktop/FMF_delo/bishoplib/build /home/ziga/Desktop/FMF_delo/bishoplib/build/CMakeFiles/bishoplib.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/bishoplib.dir/depend
