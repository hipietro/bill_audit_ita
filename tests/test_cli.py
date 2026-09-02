from bill_audit.cli import main

def test_main_prints(capsys):
    """test that the main function prints the expected output"""
    exit_code = main()
    captured=capsys.readouterr()
    assert exit_code==0
    assert captured.out=="bill audit is ready\n" #first automated test, capsys is a tool provided by pytest to capture what the program prints to the console. 
    #the program as of now asserts that the exit code is 0 so the program ran succeffully and that the output is exactly "bill audit is ready\n" which is what the main function prints. 