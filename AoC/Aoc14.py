puzzle_input = """10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL """

puzzle_input = """13 RXWQR => 4 JXCXB
7 FDGDX => 7 XRWJ
3 JBVN, 25 JFRXJ => 3 TPDSB
13 HZDWS, 11 RZNJR => 3 SVFT
5 FDGDX, 4 RZNJR, 41 ZGXGP => 8 LBVM
1 LJDRB => 9 RXWQR
2 RDPWQ => 8 JBVN
2 CZCB => 8 CXHK
4 JXCXB, 1 FPQRV => 5 TCBSQ
6 FDGDX => 8 TWGNB
1 RJBTL => 5 VRVDQ
2 XRWJ, 3 HZDWS, 12 LBVM => 6 KSJD
15 HPXST, 1 KMKR, 7 SLTX, 1 PRWD, 14 RCLB, 31 TPDSB, 3 GWXJP, 3 TPQZ => 8 XRLZR
1 RBLT, 2 RTFKN, 1 CZCB => 8 DNRP
131 ORE => 8 TFGJ
2 JFRXJ, 1 VRVDQ, 26 TWGNB => 5 CFPZ
2 SMPW, 1 TWGNB => 8 RZNJR
20 HRZP => 6 RDPWQ
1 RCLB, 4 GJNK, 4 QGJL => 4 HZDWS
7 CXHK, 2 XTMRV, 6 WSNPZ, 12 LQXCP, 19 PMWJ, 17 GJNK, 26 XRLZR, 36 LWFQ => 1 FUEL
131 ORE => 8 KMKR
1 LJDRB, 12 TFGJ, 10 RXWQR => 7 RPKZ
10 RVXT, 1 RDPWQ => 8 JFRXJ
1 QXBTX => 9 TPQZ
1 ZGXGP => 5 FZGF
1 RTFKN, 1 DNRP => 2 FDGDX
19 CZCB, 1 RBLT => 4 SMPW
2 DNRP, 1 SMPW => 9 RWSH
1 ZGXGP, 5 TCBSQ, 22 SMPW => 5 GWXJP
1 HBSKF => 3 LQXCP
1 ZGXGP, 2 KSJD, 9 CFPZ => 7 CLGXQ
186 ORE => 8 LJDRB
1 TPQZ, 2 HBSKF => 1 QGJL
8 FZGF, 6 FDGDX => 3 PMWJ
9 KMKR => 1 CZCB
21 TFGJ, 3 RVXT => 5 HRZP
39 FDGDX, 24 TPDSB => 2 RCLB
4 HRZP => 2 GJNK
6 RZNJR => 2 HBSKF
101 ORE => 8 RVXT
1 RCLB => 8 QXBTX
1 RJBTL => 7 RBLT
2 CFPZ, 2 JXCXB, 4 TPQZ => 1 LWFQ
1 QGJL, 24 GJNK, 6 TWGNB, 1 SLTX, 18 JFRXJ, 6 MSNM, 6 FDGDX, 2 JXCXB => 5 WSNPZ
4 RZNJR => 6 FPQRV
12 LJDRB, 10 JFRXJ, 1 ZGXGP => 5 TXZVH
13 KSJD, 11 FXGW => 9 PRWD
11 SVFT, 2 HZDWS, 1 CLGXQ, 1 LQXCP, 6 JXCXB, 11 PRWD => 5 XTMRV
27 TWGNB, 7 FPQRV => 2 SLTX
2 HRZP, 6 RXWQR => 9 RJBTL
2 CXHK, 1 RPKZ => 1 RTFKN
7 RWSH, 12 JBVN, 6 FXGW => 2 ZGXGP
1 TXZVH, 4 FPQRV => 8 MSNM
16 TPDSB, 1 FXGW => 5 HPXST
1 VRVDQ => 2 FXGW"""

import math

class Factory:

    def __init__(self, _input):
        self.input = _input
        self.reactions = self.create_reactions(_input)

        self.have = {}
        self.ore_used = 0

    def create_reactions(self, _input):
        lines = _input.splitlines()
        d = {}
        for i in lines:
            left,right = i.split('=>')
            left = [self.one_item(i) for i in left.split(',')]
            chemical, amount = self.one_item(right)
            d[chemical] = {'amount': amount, 'requirement' : left}
        return d
        
    def one_item(self,s):
        amount, chemical = s.split()
        return chemical, int(amount)
            
    
    def produce(self, chem, amount):
        
        if chem == 'ORE':
            self.ore_used += amount
            return 

        amount_needed = amount - self.have.get(chem,0) 
        amount_one_reaction = self.reactions[chem]["amount"]
        times_reaction = math.ceil(amount_needed / amount_one_reaction)
        
        if amount_needed > 0:
            production_list = self.reactions[chem]["requirement"]
            for c, a in production_list:
                self.produce(c, a*times_reaction)            
            self.have[chem] = self.have.get(chem,0) + amount_one_reaction*times_reaction

        self.have[chem] -= amount



def f(n):
    fac = Factory(puzzle_input)
    fac.produce("FUEL",n)
    return fac.ore_used

def binarySearch (f, l, r, x): 

    # Check base case 
    if r >= l: 

        mid = l + (r - l)/2

        # If element is present at the middle itself 
        if f(mid) == x: 
            return mid 
            
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif f(mid) > x: 
            return binarySearch(f, l, mid-1, x) 

        # Else the element can only be present  
        # in right subarray 
        else: 
            return binarySearch(f, mid + 1, r, x) 

    else: 
        # Element is not present in the array 
        return l,r



if __name__ == '__main__':
    low = 1000000
    high = 10000000
    
    print(binarySearch(f, low,high, 10**12))
        
        


