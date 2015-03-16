__author__ = 'bozeng'

def minWindow( S, T):
        if not S:
            return ""
        if not T:
            return ""

        lenS=len(S)
        lenT=len(T)

        record={}
        scanned={}


        if lenS<lenT:
            return ""

        # split can not split strings without " ". just do the conventional way


        for each in T:
            if each not in record:
                record[each]=1
            else:
                record[each]+=1

        # sliding window technique
        print(record)
        start=0

        while start<len(S) and S[start] not in record:
            start+=1

        minlength=len(S)+1
        end=start
        count=0

        result=""

        while end<lenS:
            print("c:",count)
            thischar=S[end]
            if thischar not in record:
                end+=1

            else:
                if thischar not in scanned:
                    scanned[thischar]=1
                    count+=1
                    end+=1
                elif scanned[thischar]<record[thischar]:
                    scanned[thischar]+=1
                    count+=1
                    end+=1
                else:
                    scanned[thischar]+=1
                    print("deleting")
                    while start<=end:
                        if S[start] not in scanned:
                            start+=1
                        elif scanned[S[start]]>record[S[start]]:
                            scanned[S[start]]-=1
                            start+=1
                        elif scanned[S[start]]<=record[S[start]]:
                            break
                    print(scanned,start,end)
                    print("deleting end")
                    end+=1

            if count==lenT:
                print("c:",end, start)
                if end-start<minlength:
                    minlength=end-start
                    result=S[start:end]

                if S[start] in scanned:
                    scanned[S[start]]-=1
                    if scanned[S[start]]<record[S[start]]:
                        count-=1
                    if scanned[S[start]]==0:
                        scanned.pop(S[start])
                start+=1

                while start<=end and end<lenS:
                    if S[start] not in scanned:
                        start+=1
                    elif scanned[S[start]]>record[S[start]]:
                        scanned[S[start]]-=1
                        start+=1
                    else:
                        break
                print("stop at:",start,S[start])
                print("end at:",end,S[end-1])
                print(scanned)




        return result


print(minWindow("adobecodebancbbcaa","abc"))