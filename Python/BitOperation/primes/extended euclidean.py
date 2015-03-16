__author__ = 'bozeng'
""" extended GCD algorithm that returns multipliers s_i*a+t_i*b=r_i, and in the end if r_(i+1)=0, r_i=gcd(a,b)
so that the s_i and t_i is the integer multipliers we seek to find """

def extended_gcd(a,b):
    '''
    :param a: the first integer,
    :param b: the second integer, a<=b
    :return: (gcd(a,b),s,t) so that s*a+t*b=gcd(a,b)
    '''

    if a>b:
        answer=extended_gcd(b,a)
        return (answer[0],answer[2],answer[1])

    def extended_helper(r0,r1,s0,s1,t0,t1):

        if r0==0:
            return (r1,s1,t1)
        q=r1//r0
        r2=r1%r0
        s2=s1-q*s0
        t2=t1-q*t0
        return extended_helper(r2,r0,s2,s0,t2,t0)

    return extended_helper(a,b,1,0,0,1)

print(extended_gcd(180,788),extended_gcd.__doc__)