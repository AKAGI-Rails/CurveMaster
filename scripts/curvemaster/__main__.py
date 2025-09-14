"""Curvemaster Main

"""
import sys
import argparse

description = """Curvemaster - 曲線計算機
緩和曲線を計算してベジエ曲線ハンドル座標を出力します。
"""

parser = argparse.ArgumentParser(description=description)

parser.add_argument("radius", help="curve radius", type=float)
parser.add_argument("angle", help="curve angle", type=float)
parser.add_argument("-b", "--base", help="base radius of transition curve calculation", type=float)
args = parser.parse_args()
print("argparse test")

print(args)
