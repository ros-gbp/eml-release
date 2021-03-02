cmake_minimum_required(VERSION 2.8.3)

add_subdirectory(eml-svn)

install( FILES package.xml EMLConfig.cmake DESTINATION share/eml )

