from SkyScannerTest import *

def main():
    
    d = (("GDN", "MNL", "10.07.2013", "10.08.2013"), ("GDN", "CGK", "10.07.2013", "10.08.2013"))
    test = SkyScannerTest()
    
    test.setUp()
    r1 = test.test(d[0])
    test.tearDown()
    
    test.setUp()
    r2 = test.test(d[1])
    test.tearDown()
    
    print r1
    print r2

if __name__ == '__main__':
    main()