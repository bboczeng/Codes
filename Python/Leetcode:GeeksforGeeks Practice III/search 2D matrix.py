__author__ = 'bozeng'


def searchMatrix(matrix, target):
        if not matrix:
            return False

        row=len(matrix)
        col=len(matrix[0])
        rlow=0
        rmax=row-1
        clow=0
        cmax=col-1

        while True:
            if rmax<rlow or cmax<clow:
                return False
            if rmax==rlow:
                if cmax==clow:
                    return matrix[rmax][cmax]==target
                midc=(clow+cmax)//2
                if matrix[rmax][midc]==target:
                    return True
                elif matrix[rmax][midc]>target:
                    cmax=midc
                else:
                    clow=midc+1
            else:
                midr=(rlow+rmax)//2
                if matrix[midr][col-1]==target:
                    return True
                elif matrix[midr][col-1]>target:
                    rmax=midr
                else:
                    rlow=midr+1

        return False

print(searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
],4))