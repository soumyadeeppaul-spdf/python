#SOUMYADEEP PAUL, ROLL NO- 2311182

import lib5

# --- Question 1 ---
a1, b1 = 1.5, 3.0
tol = 1e-6

print("========== Question 1 ==========")
root_bisect = lib5.bisection(lib5.f1, a1, b1, tol)
root_regula = lib5.regula_falsi(lib5.f1, a1, b1, tol)

print("\nQ1 Final Results:")
print(f"  Bisection Root ≈ {root_bisect}")
print(f"  Regula Falsi Root ≈ {root_regula}")

# --- Question 2 ---
a2, b2 = 2, 4
print("\n========== Question 2 ==========")
interval = lib5.find_interval(lib5.f2, a2, b2, step=0.1)

print("\nQ2 Final Result:")
if interval:
    print(f"  Root lies in interval: {interval}")
else:
    print("  No root found.")



"""
     
 ANSWERS::::
    ========== Question 1 ==========

--- Bisection Method ---
Iter    a       b       mid     f(mid)
1       1.500000        3.000000        2.250000        0.729465      
2       2.250000        3.000000        2.625000        -0.003763     
3       2.250000        2.625000        2.437500        0.386130      
4       2.437500        2.625000        2.531250        0.190642      
5       2.531250        2.625000        2.578125        0.092497      
6       2.578125        2.625000        2.601562        0.044032      
7       2.601562        2.625000        2.613281        0.020038      
8       2.613281        2.625000        2.619141        0.008112      
9       2.619141        2.625000        2.622070        0.002168      
10      2.622070        2.625000        2.623535        -0.000799     
11      2.622070        2.623535        2.622803        0.000684      
12      2.622803        2.623535        2.623169        -0.000058     
13      2.622803        2.623169        2.622986        0.000313      
14      2.622986        2.623169        2.623077        0.000127      
15      2.623077        2.623169        2.623123        0.000035      
16      2.623123        2.623169        2.623146        -0.000012     
17      2.623123        2.623146        2.623135        0.000012      
18      2.623135        2.623146        2.623140        0.000000      
19      2.623140        2.623146        2.623143        -0.000006     
20      2.623140        2.623143        2.623142        -0.000003     
21      2.623140        2.623142        2.623141        -0.000001     
Final Bisection Root ≈ 2.623141050338745 (after 22 iterations)        

--- Regula Falsi Method ---
Iter    a       b       c       f(c)
1       1.500000        3.000000        2.021572        0.952968      
2       2.021572        3.000000        2.649245        -0.052292     
3       2.021572        2.649245        2.616595        0.013287      
4       2.616595        2.649245        2.623210        -0.000142     
5       2.616595        2.623210        2.623141        -0.000000     
Final Regula Falsi Root ≈ 2.62314050689124 (after 6 iterations)       

Q1 Final Results:
  Bisection Root ≈ 2.623141050338745
  Regula Falsi Root ≈ 2.62314050689124

========== Question 2 ==========

--- Interval Finding ---
No root found in [2, 4]. Expanding search...
Root lies in interval: [-0.8000000000000187, -0.7000000000000187]     

Q2 Final Result:
  Root lies in interval: (-0.8000000000000187, -0.7000000000000187)
  
  """