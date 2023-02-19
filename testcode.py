def testunit(testsample,ans,Programname):
    tt=0
    for i,j in zip(testsample,ans):
        if j==Programname(i):
            print(f"Test{tt} Pass")
        else:
            print(f"Test{tt} FAIL, result= {Programname(i)}, ans={j}")
        tt+=1
        
if __name__=="__main__":
    print(" try try")
    