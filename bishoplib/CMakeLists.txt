cmake_minimum_required(VERSION 3.10)

project(bishoplib VERSION 1.0.1 DESCRIPTION "mylib description")

add_library(bishoplib SHARED
    src/bishop.cpp
)
include(GNUInstallDirs)
set_target_properties(bishoplib PROPERTIES VERSION ${PROJECT_VERSION})
set(CMAKE_INSTALL_DEFAULT_DIRECTORY_PERMISSIONS
     OWNER_READ
     OWNER_WRITE
     OWNER_EXECUTE
     GROUP_READ
   )

target_include_directories(bishoplib PUBLIC include)
target_include_directories(bishoplib PUBLIC src)

configure_file(bishoplib.pc.in bishoplib.pc @ONLY)
find_package (Eigen3 3.3 REQUIRED NO_MODULE)
target_link_libraries(bishoplib Eigen3::Eigen)

install(TARGETS bishoplib
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
    

install(FILES ${CMAKE_BINARY_DIR}/bishoplib.pc DESTINATION ${CMAKE_INSTALL_DATAROOTDIR}/pkgconfig)
