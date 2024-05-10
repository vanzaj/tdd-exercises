from loc import count_lines
from textwrap import dedent


def test_count_empty_source():
    assert count_lines("") == 0
    assert count_lines("  ") == 0


def test_count_single_line():
    src = 'public class Hello { System.out.println("Hello"); };'
    assert count_lines(src) == 1


def test_count_no_comments():
    src = dedent("""\
    public class Hello {
        System.out.println("Hello");
    };""")
    assert count_lines(src) == 3


def test_count_ignore_empty_lines():
    src = dedent("""\

    public class Hello {

        System.out.println("Hello");

    };
    """)
    assert count_lines(src) == 3
