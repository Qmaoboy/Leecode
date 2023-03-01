from tqdm import tqdm
import time

def testunit(testsample,ans,Programname):
    start=time.time()
    if len(testsample)!=len(ans):
        raise ValueError("測資異常，請確認資料正確。")
        
    for i in tqdm(range(len(testsample))):
        if ans[i]==Programname(testsample[i]):
            time.sleep(0.05)
            end=time.time()
            print(f"Test NO.{i} Pass, 執行時間: {end-start}")
        else:
            time.sleep(0.05)
            print(f"Test NO.{i} FAIL, result= {Programname(testsample[i])}, ans={ans[i]}")


def testunit_two_para(testsample,para,ans,Programname):
    start=time.time()
    if len(testsample)!=len(ans):
        raise ValueError("測資異常，請確認資料正確。")
        
    for i in tqdm(range(len(testsample))):
        if ans[i]==Programname(testsample[i],para[i]):
            time.sleep(0.05)
            end=time.time()
            print(f"Test NO.{i} Pass, 執行時間: {end-start}")
        else:
            time.sleep(0.05)
            print(f"Test NO.{i} FAIL, result= {Programname(testsample[i])}, ans={ans[i]}")

if __name__=="__main__":
    print("請用import 方式使用")
    