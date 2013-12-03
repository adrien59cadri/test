message("Creation of project ${PROJECT_NAME}")

############################
# Set a default build type if none was specified
############################
if(NOT CMAKE_BUILD_TYPE)
  message(STATUS "Setting build type to 'Debug' as none was specified.")
  set(CMAKE_BUILD_TYPE Debug CACHE STRING "Choose the type of build." FORCE)
endif()


############################
# CXX compiler on MSVC neede to be MSVC12 November 2012 CTP for C++11 specific feature
# The Toolset Generator should be pass in command with '-T v120_CTP_Nov2012'
# If it isn't, we need to record the toolset, build the project and to re-run cmake to build correctly the MSVC project 
############################
if(WIN32)
  SET(CMAKE_CXX_FLAGS_RELEASE "/arch:SSE2 /fp:fast /MT /O2 /Ob2 /D NDEBUG")
  SET(CMAKE_CXX_FLAGS_RELWITHDEBINFO "/arch:SSE2 /fp:fast /MT /O2 /Ob2 /D NDEBUG")
  SET(CMAKE_CXX_FLAGS_DEBUG "/arch:SSE2 /fp:fast /MTd /DDEBUG /D_DEBUG /Zi /Ob0 /Od")

  # /RTC1 /RTCc as debug flags removed for now - too intrusive for others projects
  # Perhaps should we add them as an option

  if(CMAKE_GENERATOR  MATCHES "Visual Studio 11" OR CMAKE_GENERATOR  MATCHES "Visual Studio 11 Win64")
	  message (STATUS "Using " ${CMAKE_GENERATOR_TOOLSET} " toolset")
      if(NOT CMAKE_GENERATOR_TOOLSET MATCHES "v120_CTP_Nov2012")
        set(CMAKE_GENERATOR_TOOLSET "v120_CTP_Nov2012" CACHE STRING "" FORCE)
        message("---------------------------- WARNING ----------------------------------")
        message("MSVC needs C++11 features - please run cmake with the command parameter '-T v120_CTP_Nov2012'.")
        message("You can either just re-run cmake to build correctly the project (Toolset as been redefined)")
        message("-----------------------------------------------------------------------")
      endif()
  endif() 



  #enable multicore build on windows
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /MP")

  #fix error C1128: number of sections exceeded object file format limit
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /bigobj")

  #see warnig c4530
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /EHsc")
  
  #disable minmax defines, see http://support.microsoft.com/kb/143208
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /DNOMINMAX")
   

  # Detect64BitPortabilityProblems: /Wp64 - Deprecated since VC++ 2010 
  # WarningLevel: /W<level 0 to 4> or /Wall
  #set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /Wp64 /W3")

endif(WIN32)

############################
## unix makefiles compat
############################
if(APPLE)
  set(CMAKE_OSX_SYSROOT "macosx")
  set(CMAKE_OSX_DEPLOYMENT_TARGET "10.7")
  set(CMAKE_OSX_ARCHITECTURES "x86_64;i386")
  set(CMAKE_FORCE_C_COMPILER "clang")
  set(CMAKE_FORCE_CXX_COMPILER "clang++")
  set(CMAKE_XCODE_ATTRIBUTE_CLANG_CXX_LANGUAGE_STANDARD "c++11")
  set(CMAKE_XCODE_ATTRIBUTE_CLANG_CXX_LIBRARY "libc++")  
  set(CMAKE_CXX_FLAGS "-std=c++11 -stdlib=libc++ -fvisibility=hidden -fvisibility-inlines-hidden -fno-common")
  SET(CMAKE_CXX_FLAGS_RELEASE "-03 -DNDEBUG")
  SET(CMAKE_CXX_FLAGS_RELWITHDEBINFO "-03 -g -DNDEBUG")
  SET(CMAKE_CXX_FLAGS_DEBUG "-g -DDEBUG -D_DEBUG")
  set(CMAKE_SHARED_LINKER_FLAGS ${CMAKE_CXX_FLAGS})
  set(EXTRA_LIBS ${EXTRA_LIBS} c++)
endif(APPLE)

add_definitions(-DUNICODE -D_UNICODE)

  

###########################################################
## INCLUDES
###########################################################
include_directories(include)

###########################################################
## LIBRAIRIES
###########################################################
# if on OSX, these files are needed
IF(APPLE)
   FIND_LIBRARY(COREFOUNDATION_LIBRARY CoreFoundation )
   FIND_LIBRARY(FOUNDATION_LIBRARY Foundation )
   MARK_AS_ADVANCED (COREFOUNDATION_LIBRARY
                    FOUNDATION_LIBRARY)
   SET(EXTRA_LIBS ${EXTRA_LIBS}
		${COREFOUNDATION_LIBRARY}
                ${FOUNDATION_LIBRARY})
ENDIF (APPLE) 

###########################################################
## EXECUTABLE DEFINITION
###########################################################
set(EXECUTABLE_OUTPUT_PATH ../../build/)
set(LIBRARY_OUTPUT_PATH ../../build/)

###########################################################
## Post Build command 
###########################################################
if(APPLE)
add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD 
    COMMAND
    install_name_tool -id lib${PROJECT_NAME}.dylib ${LIBRARY_OUTPUT_PATH}/${CMAKE_BUILD_TYPE}/lib${PROJECT_NAME}.dylib
)
endif()
