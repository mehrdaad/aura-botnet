cmake_minimum_required (VERSION 2.6)
project (Aura)

set(BIN aura)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O2 -g")

if(UNIX AND NOT APPLE)
    set(LIBS curl)
    add_definitions(-DCURL_STATICLIB)
    add_executable(${BIN} aura.cc)
    target_link_libraries(${BIN} ${LIBS})
endif()

if(WIN32)
	set(LIBS urlmon wininet)
	add_definitions(-D_CRT_SECURE_NO_WARNINGS)
	add_executable(${BIN} aura.cc aura.hh constants.hh win-components.hh win-request.hh)
	target_link_libraries(${BIN} ${LIBS})
endif()
