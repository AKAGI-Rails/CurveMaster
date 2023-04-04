"""Circular Bezier Curve Calculator"""

import numpy as np

kappa = 4 / 3 * (np.sqrt(2)-1)

class BezierCirc:
    def __init__(self, radius, angle):
        """Circular Bezier curve calculation.

        center at (0, radius)
        BCC at (0,0)
        ECC at (r*cos(angle), r*sin(angle)+r)

        Args:
            radius: Radius of circular curve.
            angle: Angle of circular curve in degrees.
        """
        self.radius = float(radius)
        self.angle = float(angle)
        self._calc()

    def _calc(self):
        r = self.radius
        angrad = self.angle * np.pi / 180.0  # angle in radians
        arclen = r * angrad  # length of arc
        x0 = np.array([0,0])
        x1 = np.array([r * kappa * angrad / (np.pi/2), 0])
        
        rot = np.matrix([[np.cos(angrad), -np.sin(angrad)],
                          [np.sin(angrad), np.cos(angrad)]])

        x3 = np.array([r*np.sin(angrad), r*(1-np.cos(angrad))])


        x2 = x3 - rot @ x1.T

        self._cps = np.vstack([x0, x1, x2, x3])

        return self._cps

    @property
    def cps(self):
        """Control points"""
        return self._cps

if __name__ == '__main__':
    import sys
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("radius", help="curve radius", type=float)
    parser.add_argument("angle", help="curve angle", type=float)

    args = parser.parse_args()

    bez = BezierCirc(args.radius, args.angle)
    #print(bez.cps)
    np.savetxt(sys.stdout, bez.cps, fmt='%8.4f', delimiter=', ')
