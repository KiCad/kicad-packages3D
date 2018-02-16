project( kicad-packages3d NONE )

cmake_minimum_required( VERSION 2.6.1 FATAL_ERROR )


#================================================
# Locations for install targets.
#================================================
if( APPLE )
    # Like all variables, CMAKE_INSTALL_PREFIX can be over-ridden on the command line.
    set( CMAKE_INSTALL_PREFIX "/Library/Application Support/kicad/" CACHE PATH "" )
    # Everything without leading / is relative to CMAKE_INSTALL_PREFIX.
    set( KICAD_PACKAGES_3D modules/packages3d )
else()
    # Everything without leading / is relative to CMAKE_INSTALL_PREFIX.
    set( KICAD_DATA share/kicad
        CACHE PATH "Location of KiCad data files." )
    set( KICAD_PACKAGES_3D ${KICAD_DATA}/modules/packages3d )
endif()

mark_as_advanced( KICAD_DATA KICAD_MODULES )


#================================================
# "make uninstall" rules
#
# The uninstaller does not remove folders only files.
#================================================
configure_file(
    "${PROJECT_SOURCE_DIR}/CMakeModules/cmake_uninstall.cmake.in"
    "${CMAKE_CURRENT_BINARY_DIR}/cmake_uninstall.cmake"
    IMMEDIATE @ONLY
)

add_custom_target( uninstall
    "${CMAKE_COMMAND}" -P "${CMAKE_CURRENT_BINARY_DIR}/cmake_uninstall.cmake"
)


#================================================
# Installed files.
#================================================

# Install the contents of all of the .pretty folders in to the modules path.
install( DIRECTORY ./
    DESTINATION ${KICAD_PACKAGES_3D}
    COMPONENT resources
    FILES_MATCHING PATTERN "*.wrl"
    PATTERN ".git" EXCLUDE
)

install( DIRECTORY ./
    DESTINATION ${KICAD_PACKAGES_3D}
    COMPONENT resources
    FILES_MATCHING PATTERN "*.step"
    PATTERN ".git" EXCLUDE
)
