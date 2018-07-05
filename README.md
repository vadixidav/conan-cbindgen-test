# conan-cbindgen-test
Demonstrates how to write a C++ API with automatically generated bindings using the Conan package manager

- See `src/lib.rs` to see the Rust code which has automatic C++ bindings generated for it.
- See `test_package/example.cpp` to see how the generated header is consumed in C++.
- See `build.rs` for how `cbindgen` is being used.
- See `conanfile.py` for how the build and consumption is set up.

## How to use

1. Clone this repository
2. Open `conanfile.py` and modify the following lines to use your project's information:
    ```
    class CbindgentestConan(ConanFile):
        name = "cbindgen_test"
        version = "0.2.0"
        description = "Test generated C++ bindings for Rust"
    ```
3. Open `Cargo.toml` and modify the following lines to use your project's information:
    ```
    [package]
    name = "cbindgen_test"
    version = "0.2.0"
    authors = ["Geordon Worley <vadixidav@gmail.com>"]
    ```
4. You can now run both `cargo test` and `conan create . user/channel` in this directory.

## Eventual plans
Eventually I intended to copy what Bincrafters did [here](https://github.com/bincrafters/conan-boost-package-tools) and create a package which depends on no settings that just has a python module in it which can be imported to implement the entire `conanfile.py`. For now all of the implementation is stored directly with the project and duplicated, but moving to that sort of implementation will allow the implementation to be updated independently with new versions from upstream.