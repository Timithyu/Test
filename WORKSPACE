workspace(name = "test")

# register_toolchains("//src/tools/arm64_toolchain:arm64_toolchain_registration")

# load("//bazel_ros2_rules/tools:environ.bzl", "environment_repository")

# environment_repository(
#     name = "test_environ",
#     envvars = ["ROS2_DISTRO_PREFIX"],
# )

# load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# http_archive(
#     name = "bazel_skylib",
#     sha256 = "f7be3474d42aae265405a592bb7da8e171919d74c16f082a5457840f06054728",  # noqa
#     urls = [
#         "https://mirror.bazel.build/github.com/bazelbuild/bazel-skylib/releases/download/1.2.1/bazel-skylib-1.2.1.tar.gz",  # noqa
#         "https://github.com/bazelbuild/bazel-skylib/releases/download/1.2.1/bazel-skylib-1.2.1.tar.gz",  # noqa
#     ],
# )

# http_archive(
#     name = "rules_python",
#     sha256 = "0a8003b044294d7840ac7d9d73eef05d6ceb682d7516781a4ec62eeb34702578",  # noqa
#     strip_prefix = "rules_python-0.24.0",
#     url = "https://github.com/bazelbuild/rules_python/releases/download/0.24.0/rules_python-0.24.0.tar.gz",  # noqa
# )

# load("@bazel_skylib//:workspace.bzl", "bazel_skylib_workspace")

# bazel_skylib_workspace()

# local_repository(
#     name = "bazel_ros2_rules",
#     path = "bazel_ros2_rules",
# )

# load("@bazel_ros2_rules//deps:defs.bzl", "add_bazel_ros2_rules_dependencies")

# add_bazel_ros2_rules_dependencies()

# load(
#     "@bazel_ros2_rules//ros2:defs.bzl",
#     "ros2_local_repository",
# )
# load(
#     "@test_environ//:environ.bzl",
#     "ROS2_DISTRO_PREFIX",
# )
# load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

# git_repository(
#     name = "com_github_gflags_gflags",
#     remote = "https://github.com/gflags/gflags.git",
#     tag = "v2.2.2",
# )

# # Please keep this list sorted
# ROS2_PACKAGES = [
#     "plotjuggler",
#     "plotjuggler_ros",
#     "action_msgs",
#     "builtin_interfaces",
#     "console_bridge_vendor",
#     "rclcpp",
#     "rclcpp_action",
#     "rclpy",
#     "ros2cli",
#     "ros2cli_common_extensions",
#     "rosbag2",
#     "rosidl_default_generators",
#     "tf2_py",
# ] + [
#     # These are possible RMW implementations. Uncomment one and only one to
#     # change implementations
#     "rmw_cyclonedds_cpp",
#     # "rmw_fastrtps_cpp",
# ]

# RESOLVED_PREFIX = (
#     ROS2_DISTRO_PREFIX if ROS2_DISTRO_PREFIX else "/opt/ros/humble"
# )

# ros2_local_repository(
#     name = "ros2",
#     include_packages = ROS2_PACKAGES,
#     workspaces = [RESOLVED_PREFIX],
# )
