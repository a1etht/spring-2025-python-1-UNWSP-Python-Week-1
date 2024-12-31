import program_1

def test_hello(capfd):
    program_1.hello_world()
    out, err = capfd.readouterr()
    assert out == "Hello World\n"