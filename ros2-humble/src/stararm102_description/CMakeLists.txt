cmake_minimum_required(VERSION 3.22)
project(stararm102_description)

find_package(ament_cmake REQUIRED)

ament_package()

if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/launch")
  install(
    DIRECTORY launch
    DESTINATION share/${PROJECT_NAME}
    PATTERN "setup_assistant.launch" EXCLUDE)
endif()

# The package exports ament_python; keep this alternative install layout aligned.
set(MODEL_RESOURCES "${CMAKE_CURRENT_SOURCE_DIR}/../../../hardware/robot-description")
install(DIRECTORY "${MODEL_RESOURCES}/urdf" "${MODEL_RESOURCES}/meshes" rviz
  DESTINATION share/${PROJECT_NAME})
