from conans import ConanFile, VisualStudioBuildEnvironment, CMake, tools


class CbindgenTestConan(ConanFile):
    name = "cbindgen_test"
    version = "0.1.0"
    description = "cbindgen, Cargo, and Conan demo package"
    settings = "os", "compiler", "build_type", "arch"
    no_copy_source = True
    exports_sources = "src/*", "build.rs", "Cargo.toml"

    def cargo_target(self):
        if self.settings.os == "Windows":
            return "i686-pc-windows-msvc" if self.settings.arch == "x86" else "x86_64-pc-windows-msvc"
        if self.settings.os == "Linux":
            return "i686-unknown-linux-gnu" if self.settings.arch == "x86" else "x86_64-unknown-linux-gnu"

    def build(self):
        flags = []
        if self.settings.os == "Windows":
            flags.append("-C target-feature={}crt-static".format(
                "+" if self.settings.compiler.runtime in ["MT", "MTd"] else "-"))
        with tools.environment_append({"CARGO_TARGET_DIR": self.build_folder, "RUSTFLAGS": " ".join(flags)}):
            with tools.chdir(self.source_folder):
                debrel = "--release" if self.settings.build_type == "Release" else ""
                if self.settings.compiler == "Visual Studio":
                    env_build = VisualStudioBuildEnvironment(self)
                    with tools.environment_append(env_build.vars):
                        vcvars = tools.vcvars_command(self.settings)
                        self.run(
                            "{} && cargo build --features=headers {} --target={}".format(vcvars, debrel, self.cargo_target()))
                else:
                    self.run(
                        "cargo build --features=headers {} --target={}".format(debrel, self.cargo_target()))

    def package(self):
        # This assumes your header goes into the root of the include path.
        self.copy("{}.h".format(self.name), dst="include")
        for post in ["_c", ""]:
            for ext in ["lib", "a", "so"]:
                self.copy("*{}{}.{}".format(self.name, post, ext), dst="lib", keep_path=False)
            if self.settings.os == "Windows":
                    self.copy("*{}{}.dll".format(self.name, post), dst="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        if self.settings.os == "Windows":
            self.cpp_info.libs += ["Ws2_32", "Userenv", "Dwmapi", "Dbghelp"]
        if self.settings.os == "Linux":
            self.cpp_info.libs += ["pthread", "dl", "rt"]
            self.cpp_info.cppflags = ["-pthread"]
