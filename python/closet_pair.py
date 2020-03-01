"""
Divide and Conquer Algorithm for determinning the closet pair of point in plane R^2

Assume : No Ties in either x or y coordinates.
"""

import math
import random


def euclidean_dist(p1, p2):
  return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calc_dist_brute(ax):
  mi = euclidean_dist(ax[0], ax[1])
  p1 = ax[0]
  p2 = ax[1]
  ln_ax = len(ax)
  if ln_ax == 2:
    return p1, p2, mi
  for i in range(ln_ax-1):
    for j in range(i + 1, ln_ax):
      if i != 0 and j != 1:
        d = euclidean_dist(ax[i], ax[j])
        if d < mi:  # Update min_dist and points
          mi = d
          p1, p2 = ax[i], ax[j]
  return p1, p2, mi


def closest_split_pair(p_x, p_y, delta, best_pair):
  ln_x = len(p_x)
  mx_x = p_x[ln_x // 2][0]  # select midpoint on x-sorted array
  # Create a subarray of points not further than delta from
  # midpoint on x-sorted array
  s_y = [x for x in p_y if mx_x - delta <= x[0] <= mx_x + delta]
  best = delta  # assign best value to delta
  ln_y = len(s_y)
  for i in range(ln_y - 1):
    for j in range(i+1, min(i + 7, ln_y)):
      p, q = s_y[i], s_y[j]
      dst = euclidean_dist(p, q)
      if dst < best:
        best_pair = p, q
        best = dst
  return best_pair[0], best_pair[1], best

def closest_pair(ax, ay):
  ln_ax = len(ax)
  # Base Case
  if ln_ax <= 3:
    return calc_dist_brute(ax)
  
  mid = ln_ax // 2
  Qx = ax[:mid]
  Rx = ax[mid:]
  # Determine midpoint on x-axis
  midpoint = ax[mid][0]  
  Qy = list()
  Ry = list()
  for x in ay:  # split ay into 2 arrays using midpoint
    if x[0] <= midpoint:
      Qy.append(x)
    else:
      Ry.append(x)
  # Call recursively both arrays after split
  (p1, q1, mi1) = closest_pair(Qx, Qy) # Left Part
  (p2, q2, mi2) = closest_pair(Rx, Ry) # Right Part
  # Determine smaller distance between points of 2 arrays
  if mi1 <= mi2:
    d = mi1
    mn = (p1, q1)
  else:
    d = mi2
    mn = (p2, q2)
  # Call function to account for points on the boundary
  (p3, q3, mi3) = closest_split_pair(ax, ay, d, mn)
  # Determine smallest distance for the array
  if d <= mi3:
    return mn[0], mn[1], d
  else:
    return p3, q3, mi3


def run(x, y):
  a = list(zip(x, y))  # This produces list of tuples
  ax = sorted(a, key=lambda x: x[0])  # Presorting x-wise
  ay = sorted(a, key=lambda x: x[1])  # Presorting y-wise
  p1, p2, mi = closest_pair(ax, ay)
  return p1, p2, mi


def test_case(length: int = 10000):
  lst1 = [random.randint(-10**9, 10**9) for i in range(length)]
  lst2 = [random.randint(-10**9, 10**9) for i in range(length)]
  return lst1, lst2


l1, l2 = test_case(5)
p1, p2, min_dst = run(l1, l2)
print('Minimum Distance Is : ', min_dst)
print('\n')
print('Between These Two Points: ', p1, p2)
print('\n')
print('From This List Of Points: ', list(zip(l1, l2)))
print('\n')
