commands={
    'test-pattern-off':'(ITP 0)',
    'set-frame-delay-3f': '(FRD 3000)',
    'set-frame-delay-default':'(FRD 1000)',
    'test-pattern-grid': '(ITP 1)',
    'test-pattern-greyscale':'(ITP 2)',
    'test-pattern-white':'(ITP 3)',
    'test-pattern-grey':'(ITP 4)',
    'test-pattern-white':'(ITP 5)',
    'alignment-tests-go':'(ITP 1)',
    #TODO return lamda of cle_number = cle_number + 1 / ('%s %s'%('(CLE)', (cle_number%3)+1))
    'alignment-tests-stop': ['(CLE 0)', '(ITP 0)'],
    'shutter-projectors':'(SHU 0)',
    'unshutter-projectors':'(SHU 1)',
    'power-off':'(PWR 0)',
    'power-on':'(PWR 1)'
}

queries={}
