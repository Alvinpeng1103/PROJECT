#include <unistd.h>
#include <stdarg.h>
#include <stddef.h>
#include <stdint.h>
#include <setjmp.h>
#include <cmocka.h>



// int chef_cook(const char *order, char **dish_out)
// {
//     check_expected(order);
// }

static void test_driver(void **state)
{
    expect_string(chef_cook, order, "hotdog");
}

static void test1(void **state){

    int i = 5;
    assert_int_equal(i, 5);
}

int main() {
    //Your own testing code here
    const struct CMUnitTest tests[] = { 
        cmocka_unit_test(test1),
};

return cmocka_run_group_tests(tests, NULL, NULL);

}

