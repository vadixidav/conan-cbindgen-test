extern crate cbindgen;

fn main() {
    let crate_dir = env!("CARGO_MANIFEST_DIR");
    let crate_name = env!("CARGO_PKG_NAME");

    cbindgen::Builder::new()
        .with_crate(crate_dir)
        .with_namespace(crate_name)
        .with_language(cbindgen::Language::Cxx)
        .generate()
        .expect("Unable to generate bindings")
        .write_to_file(format!("{}.h", crate_name));
}
