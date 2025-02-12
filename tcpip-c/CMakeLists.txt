cmake_minimum_required (VERSION 3.13)

configure_file(demo_config.h.in demo_config.h)

project (tcpip_demo C)

# Set names and variables
set(TARGET_NAME ${CMAKE_PROJECT_NAME}) 

# Add executable
add_executable(${TARGET_NAME})

target_sources(${TARGET_NAME} PRIVATE
	main.c
	utility.c
)


add_subdirectory(oneshot_demo)

if(WIN32)
    target_sources(${TARGET_NAME} PRIVATE
        win.c
    )
    target_link_libraries(${TARGET_NAME}
	   ws2_32
    )
elseif(UNIX)
    target_sources(${TARGET_NAME} PRIVATE
        unix.c
    )
    find_package(Threads REQUIRED)

    target_link_libraries(${TARGET_NAME} PRIVATE
        ${CMAKE_THREAD_LIBS_INIT}
        rt
    )
endif()

# Add include paths for all sources.
target_include_directories(${TARGET_NAME} PRIVATE
	${CMAKE_CURRENT_BINARY_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}
)

include (${CMAKE_CURRENT_SOURCE_DIR}/BuildType.cmake)
set_build_type()