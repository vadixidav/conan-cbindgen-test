fn main() {
    if std::env::var_os("CARGO_FEATURE_HEADERS").is_some() {
        let crate_dir = env!("CARGO_MANIFEST_DIR");
        let crate_name = env!("CARGO_PKG_NAME");
        let base_name = crate_name.find("_c").map(|pos| &crate_name[0..pos]).unwrap_or(&crate_name[..]);
        cbindgen::Builder::new()
            .with_crate(crate_dir)
            .with_language(cbindgen::Language::Cxx)
            .with_namespace(base_name)
            .with_include_guard(format!("{}_H", base_name.to_uppercase()))
            .generate()
            .expect("Unable to generate bindings")
            .write_to_file(format!("{}.h", base_name));
    }
}
