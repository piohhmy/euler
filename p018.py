""" By starting at the top of the triangle below and moving to adjacent numbers
on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.


Find the maximum total from top to bottom of the triangle below:

               75
              95 64
             17 47 82
            18 35 87 10
           20 04 82 47 65
          19 01 23 75 03 34
         88 02 77 73 07 63 67
        99 65 04 28 06 16 70 92
       41 41 26 56 83 40 80 70 33
      41 48 72 33 47 32 37 16 94 29
     53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
   91 71 52 38 17 14 91 43 58 50 27 29 48
  63 66 04 68 89 53 67 30 73 16 69 87 40 31
 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

Find the maximum total from top to bottom of the triangle below:
"""


from nose.tools import *

test_tri = """    
   3
  7 4
 2 4 6
8 5 9 3"""

full_tri = """
               75
              95 64
             17 47 82
            18 35 87 10
           20 04 82 47 65
          19 01 23 75 03 34
         88 02 77 73 07 63 67
        99 65 04 28 06 16 70 92
       41 41 26 56 83 40 80 70 33
      41 48 72 33 47 32 37 16 94 29
     53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
   91 71 52 38 17 14 91 43 58 50 27 29 48
  63 66 04 68 89 53 67 30 73 16 69 87 40 31
 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

def test_example_tri_is_23():
  assert_equal(solve_p018(test_tri), 23)

def split_tri_string(tri):
  tri_lines = tri.strip().splitlines()
  return [map(int, line.split()) for line in tri_lines]

def solve_p018(tri=full_tri):
  tri = split_tri_string(tri) 
  paths = []
  def build_tree_paths(line, index, cur_path):
      cur_path = cur_path + [tri[line][index]]
      if line == len(tri) - 1:
        paths.append(cur_path)
      else:
        build_tree_paths(line+1,index, cur_path)
        build_tree_paths(line+1,index+1, cur_path)

  build_tree_paths(0,0,[])
  return max(([sum(path) for path in paths]))
