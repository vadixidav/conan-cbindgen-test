#include "cbindgen-test.h"

int main(int argc, char *argv[]) {
    // Foo
    cbindgen_test::TestEnum a;
    a.tag = cbindgen_test::TestEnum::Tag::Foo;
    a.foo._0 = 5;
    cbindgen_test::hello(a);

    // Bar
    cbindgen_test::TestEnum b;
    b.tag = cbindgen_test::TestEnum::Tag::Bar;
    b.bar.x = 1;
    b.bar.y = 2;
    cbindgen_test::hello(b);

    // Baz
    cbindgen_test::TestEnum c;
    c.tag = cbindgen_test::TestEnum::Tag::Baz;
    cbindgen_test::hello(c);

    return 0;
}
