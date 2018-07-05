from conans import ConanFile, CMake, tools


class CbindgentestConan(ConanFile):
    name = "cbindgen_test"
    version = "0.2.0"
    description = "Test generated C++ bindings for Rust"
    settings = "os", "compiler", "build_type", "arch"
    no_copy_source = True
    exports_sources = "src/*", "build.rs", "Cargo.toml"

    def cargo_target(self):
        return "i686-pc-windows-msvc" if self.settings.arch == "x86" else "x86_64-pc-windows-msvc"

    def build(self):
        flags = "-C target-feature={}crt-static".format(
            "+" if self.settings.compiler.runtime in ["MT", "MTd"] else "-")
        with tools.environment_append({"CARGO_TARGET_DIR": self.build_folder, "RUSTFLAGS": flags}):
            with tools.chdir(self.source_folder):
                debrel = "--release" if self.settings.build_type == "Release" else ""
                self.run(
                    "cargo build {} --target={}".format(debrel, self.cargo_target()))

    def package(self):
        mode = "debug" if self.settings.build_type == "Debug" else "release"
        out_dir = "{}/{}".format(self.cargo_target(), mode)
        # This assumes your header goes into the root of the include path.
        self.copy("{}.h".format(self.name), dst="include")
        self.copy("{}.dll".format(self.name), dst="bin",
                  src=out_dir, keep_path=False)
        self.copy("{}.lib".format(self.name), dst="lib",
                  src=out_dir, keep_path=False)
        self.copy("{}.so".format(self.name), dst="lib",
                  src=out_dir, keep_path=False)
        self.copy("{}.dylib".format(self.name), dst="lib",
                  src=out_dir, keep_path=False)
        self.copy("{}.a".format(self.name), dst="lib",
                  src=out_dir, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        # TODO: This is probably incorrect and needs to be expanded.
        if self.settings.os == "Windows":
            self.cpp_info.libs += ["Ws2_32", "Userenv"]
