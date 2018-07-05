#[repr(C)]
#[derive(Debug)]
pub enum TestEnum {
    Foo(u16),
    Bar { x: u8, y: i16 },
    Baz,
}

#[no_mangle]
pub extern "C" fn hello(test_enum: TestEnum) {
    println!("Hello, {:?}!", test_enum);
}
