"""Curvemaster - Transition curve solver.
"""
import numpy as np
from scipy.optimize import minimize

class BezierTrans(object):
    def __init__(self, radius, angle, baseradius=None):
        self.radius = radius
        self.angle = angle
        if baseradius is None:
            self.baseradius = radius
        else:
            self.baseradius = baseradius

        self.difradius = self.radius - self.baseradius
        # 基準のサイン半波長逓減曲線の原点は [0, difradius]
        # y = f(x) + difradius
        # X = 2R*tan(theta)

        # ベジエ曲線の端点を決定
        # 始点
        self.p0 = np.array([0,0])
        
        # 終点は、サイン半波長逓減曲線の終点から距離difradiusだけずれた点
        X = 2*radius*np.tan(angle)
        Y = sinehalftrans(X, radius, angle)
        X_ = X + self.difradius*np.sin(angle)
        Y_ = Y - self.difradius*np.cos(angle)
        self.p3 = np.array([X_,Y_])

        # p1, p2は未定（最適化しないとわからない）
        self.p1 = np.array([np.nan, np.nan])
        self.p2 = np.array([np.nan, np.nan])

    def solve(self, section=10):
        """ベジエ曲線を最適化
        
        変数: ハンドル倍率
        目的関数: 基準サイン半波長逓減曲線との誤差の累積

        初期解は、p2=[X/3, 0], p3=[2X/3,??]におく
        """
        # 基準ハンドルベクトル
        _X, _ = self.p3
        h1 = self.p3 * np.array([1/3, 0])
        h2 = -(_X /3)* np.array([1, np.tan(self.angle)])

        # ハンドル倍率の初期値セット
        s0 = np.array([1,1])

        # 目的関数
        def optf(x,):
            raise NotImplemented
        
        res = minimize(optf, s0, method='Powell')
        if not res.success:
            raise RuntimeError(res.message)

        s = res.x

    @property
    def cps(self):
        """Control Points"""
        return np.vstack((self.p0, self.p1, self.p2, self.p3)) 

    def besier_locus(self, n:int):
        """ベジエ曲線の軌跡
        
        ベジエ曲線の軌跡のn分割点を求める。

        Parameter:
            n: 分割数

        Returns:
            x: (n+1) d array of x pos
            y: (n+1) d array of y pos
        """
        t = np.linspace(0.0, 1.0, num=n+1)


def GeneralBezier(self):
    def __init__(self, p0, p1, p2, p3):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def pos(t):
        """position where t=t"""
        assert 0 <= t <= 1
        p_ = [self.p0, self.p1, self.p2, self.p3]
        t_ = [t**3, 3 * t**2 * (1-t), 3*t * (1-t)**2, (1-t)**3]
        x = sum([t*p for t,p in zip(t_, p_)])

    def normal(t):
        """normal vector where t=t"""
        assert 0 <= t <= 1
        

def sinehalftrans(x, R, theta):
    X = 2*R * np.tan(theta)
    pi = np.pi
    return x*x/R/4 - X*X/R/pi/pi/2*(1 - np.cos(x*pi/X))
