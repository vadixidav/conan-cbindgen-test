#[no_mangle]
pub extern "C" fn hello(a: i32) {
    println!("Hello, {}!", a);
}
