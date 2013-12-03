cmake_minimum_required(VERSION 2.8.11)

############################
# Project Declaration 
############################
project(cpp11_dojo)

###########################################################
## Set Directory value
###########################################################
set(SRC_DIR ../../src)

###########################################################
## Basics Setup Import
###########################################################
include(../cmake/BasicsSetup.cmake)

###########################################################
## INCLUDES
###########################################################
include_directories(${SRC_DIR})

###########################################################
## SOURCES DEFINITIONS
###########################################################
SET(src_files 
  ${SRC_DIR}/main.cpp
)

source_group("src" FILES ${src_files})

###########################################################
## EXECUTABLE DEFINITION
###########################################################
MESSAGE("Build type is ${CMAKE_BUILD_TYPE}")
MESSAGE("Src dir is ${CMAKE_SOURCE_DIR}")
MESSAGE("PROJECT_NAME is ${PROJECT_NAME}")
add_executable(${PROJECT_NAME} 
  ${src_files} 
)

#Configuration de l'édition de liens
target_link_libraries(
  ${PROJECT_NAME}
  ${EXTRA_LIBS}
)
