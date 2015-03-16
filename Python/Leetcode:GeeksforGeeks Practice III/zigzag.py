__author__ = 'bozeng'


def convert( s, nRows):
        if not s:
            return ""

        result=[[] for i in range(nRows)]
        row=0
        direction=0

        for char in s:
            print(row)
            result[row].append(char)

            if direction==0:
                if row==nRows-1:
                    direction=1
                    row=max(row-1,0)
                    continue
                else:
                    row=row+1
            elif direction==1:
                if row==0:
                    direction=0
                    row=min(1,nRows-1)
                    continue
                else:
                    row=row-1
        answer=""
        for item in result:
            answer=answer+"".join(item)

        return answer

print(convert( "PAYPALISHIRING", 3))