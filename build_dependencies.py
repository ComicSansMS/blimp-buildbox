import os
import subprocess
import sys

def call(args, cwd=os.getcwd()):
    p = subprocess.Popen(args, cwd=cwd)
    if p.wait() != 0:
        raise RuntimeError("Error in subprocess.")

do_run_tests = False
cmake_generator = "Visual Studio 16 2019"
cmake_architecture = "x64"
cwd = os.getcwd()
install_dir = os.path.join(cwd, "install")
configs = ["Debug", "MinSizeRel", "Release", "RelWithDebInfo"]

print("*******************************************************************************")
print("***  aws-c-common                                                           ***")
print("*******************************************************************************")
sys.stdout.flush()

build_dir = os.path.join(cwd, "aws-c-common-build")
source_dir = os.path.join(cwd, "aws-c-common")
call(["cmake", "-G", cmake_generator, "-A", cmake_architecture,
      "-DCMAKE_INSTALL_PREFIX=" + install_dir, source_dir],
    cwd=build_dir)
for c in configs:
    call(["cmake", "--build", build_dir, "--config", c, "-j"])
    if(do_run_tests): call(["cmake", "--build", build_dir, "--config", c, "--target", "RUN_TESTS"])
    call(["cmake", "--build", build_dir, "--config", c, "--target", "INSTALL"])

print("*******************************************************************************")
print("***  aws-checksums                                                          ***")
print("*******************************************************************************")
sys.stdout.flush()

build_dir = os.path.join(cwd, "aws-checksums-build")
source_dir = os.path.join(cwd, "aws-checksums")
call(["cmake", "-G", cmake_generator, "-A", cmake_architecture,
      "-DCMAKE_INSTALL_PREFIX=" + install_dir, source_dir],
    cwd=build_dir)
for c in configs:
    call(["cmake", "--build", build_dir, "--config", c, "-j"])
    if (do_run_tests): call(["cmake", "--build", build_dir, "--config", c, "--target", "RUN_TESTS"])
    call(["cmake", "--build", build_dir, "--config", c, "--target", "INSTALL"])

print("*******************************************************************************")
print("***  aws-c-event-stream                                                     ***")
print("*******************************************************************************")
sys.stdout.flush()

build_dir = os.path.join(cwd, "aws-c-event-stream-build")
source_dir = os.path.join(cwd, "aws-c-event-stream")
call(["cmake", "-G", cmake_generator, "-A", cmake_architecture,
      "-DCMAKE_INSTALL_PREFIX=" + install_dir, "-DCMAKE_PREFIX_PATH=" + install_dir, source_dir],
    cwd=build_dir)
for c in configs:
    call(["cmake", "--build", build_dir, "--config", c, "-j"])
    if (do_run_tests): call(["cmake", "--build", build_dir, "--config", c, "--target", "RUN_TESTS"])
    call(["cmake", "--build", build_dir, "--config", c, "--target", "INSTALL"])

print("*******************************************************************************")
print("***  aws-cpp-sdk                                                            ***")
print("*******************************************************************************")
sys.stdout.flush()

build_dir = os.path.join(cwd, "aws-sdk-cpp-build")
source_dir = os.path.join(cwd, "aws-sdk-cpp")
call(["cmake", "-G", cmake_generator, "-A", cmake_architecture,
      "-DCMAKE_INSTALL_PREFIX=" + install_dir, "-DCMAKE_PREFIX_PATH=" + install_dir,
      "-DBUILD_DEPS=OFF", "-DBUILD_SHARED_LIBS=OFF", "-DENABLE_UNITY_BUILD=ON", "-DSIMPLE_INSTALL=OFF",
      "-DENABLE_TESTING=OFF", "-DBUILD_ONLY=core;glacier", source_dir],
    cwd=build_dir)
for c in configs:
    call(["cmake", "--build", build_dir, "--config", c, "-j"])
    #if (do_run_tests): call(["cmake", "--build", build_dir, "--config", c, "--target", "RUN_TESTS"])
    call(["cmake", "--build", build_dir, "--config", c, "--target", "INSTALL"])

print("*******************************************************************************")
print("AWS_DEPENDENCIES_ROOT=", install_dir)
