# - Try to find EML
# Once done this will define
#  EML_FOUND - System has EML
#  EML_INCLUDE_DIRS - The EML include directories
#  EML_LIBRARIES - The libraries needed to use EML
#  EML_DEFINITIONS - Compiler switches required for using EML

find_path(EML_INCLUDE_DIR al/ethercat_master.h)

find_library(EML_LIBRARY NAMES eml)

set(EML_LIBRARIES ${EML_LIBRARY} )
set(EML_INCLUDE_DIRS ${EML_INCLUDE_DIR} )

include(FindPackageHandleStandardArgs)
# handle the QUIETLY and REQUIRED arguments and set EML_FOUND to TRUE
# if all listed variables are TRUE
find_package_handle_standard_args(EML  DEFAULT_MSG
   EML_LIBRARY EML_INCLUDE_DIR)

mark_as_advanced(EML_INCLUDE_DIR EML_LIBRARY )

