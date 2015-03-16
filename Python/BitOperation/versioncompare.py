__author__ = 'bozeng'


def compareVersion(version1, version2):
        vnum1=version1.split('.')
        vnum2=version2.split('.')

        length=max(len(vnum1),len(vnum2))

        for i in range(length):
            if i>len(vnum1)-1:
                if vnum2[i]=='0':
                    return 0
                return -1
            elif i>len(vnum2)-1:
                if vnum1[i]=='0':
                    return 0
                return 1
            s1=vnum1[i]
            s2=vnum2[i]
            if int(s1)>int(s2):
                return 1
            elif int(s1)<int(s2):
                return -1

        return 0

print(compareVersion('1.1','2.0'))