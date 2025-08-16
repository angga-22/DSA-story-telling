def loopArr(arr: list[int]) -> list[int]:
    res: list[int] = [] 
    resAsDict: dict = {} 
    for i, el in enumerate(arr):
        print(f"index {i}: {el}")
        res.append(el)
        resAsDict[i] = el
    print(resAsDict, '<< res as dict')
    return res
