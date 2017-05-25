class Point:

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def distanceFromPoint(self, point):
        return (((self.x - point.x) ** 2) + ((self.y - point.y) ** 2)) ** 0.5

    def reflect_x(self):
        return Point(self.x, self.y * -1)
        
    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

    def halfway(self, target):
         mx = (self.x + target.x) / 2
         my = (self.y + target.y) / 2
         return Point(mx, my)

    def get_line_to(self, point):
        m = (self.y - point.y) / (self.x - point.x)
        c = self.y - m * self.x
        return m, c
    
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        

p = Point(1, 2)
q = Point(3, 4)
r = Point(4, -1)

mid_pq = p.halfway(q)
mid_pr = p.halfway(r)
print(mid_pq, mid_pr)
mc_pq = p.get_line_to(q)
mc_pr = p.get_line_to(r)
print(mc_pq, mc_pr)
inv_mc_pq = -1/mc_pq[0],mid_pq.getY()+mid_pq.getX()/mc_pq[0]
inv_mc_pr = -1/mc_pr[0],mid_pr.getY()+mid_pr.getX()/mc_pr[0]
print(inv_mc_pq, inv_mc_pr)
# if y = mx + c  then  m_pq*xcen + c_pq = m_pr*xcen + c_pr
#  xcen = (c_pr - c_pq) / (m_pq - m_pr)
#
# x = (y - c) / m   so  (ycen - c_pq) / m_pq = (ycen - c_pr) / m_pr
#  ycemn*m_[1]pr m- c_[1]pq*m_pcr =[0] ycecn*m[0]_pq - c_pr*m_pq
# ycen = (c_pq*m_pr - c_pr*m_pq) / (m_pr - m_pq)
#

xcen = (inv_mc_pr[1] - inv_mc_pq[1]) / (inv_mc_pq[0] - inv_mc_pr[0])
ycen = (inv_mc_pq[1]*inv_mc_pr[0] - inv_mc_pr[1]*inv_mc_pq[0]) / (inv_mc_pr[0] - inv_mc_pq[0])

center = Point(xcen, ycen)
radius = p.distanceFromPoint(center)
print(center)

print("Three points: ", p, q, r)
print("form a circle of radius {} centered at".format(radius), center)
