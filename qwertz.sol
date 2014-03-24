Problem:    
Rows:       6
Columns:    6
Non-zeros:  20
Status:     UNBOUNDED
Objective:  obj = 3 (MAXimum)

   No.   Row name   St   Activity     Lower bound   Upper bound    Marginal
------ ------------ -- ------------- ------------- ------------- -------------
     1 r.5          NU             3                           3             1 
     2 r.6          B              3                           3 
     3 r.7          B              3                           4 
     4 r.8          B              3                           4 
     5 r.9          B              3                           6 
     6 r.10         B              0                           6 

   No. Column name  St   Activity     Lower bound   Upper bound    Marginal
------ ------------ -- ------------- ------------- ------------- -------------
     1 x1           B              3             0               
     2 x2           NL             0             0                       < eps
     3 x3           NL             0             0                       < eps
     4 x4           NL             0             0                       < eps
     5 x5           NL             0             0                       < eps
     6 x6           NL             0             0                           1 

Karush-Kuhn-Tucker optimality conditions:

KKT.PE: max.abs.err = 0.00e+00 on row 0
        max.rel.err = 0.00e+00 on row 0
        High quality

KKT.PB: max.abs.err = 0.00e+00 on row 0
        max.rel.err = 0.00e+00 on row 0
        High quality

KKT.DE: max.abs.err = 0.00e+00 on column 0
        max.rel.err = 0.00e+00 on column 0
        High quality

KKT.DB: max.abs.err = 1.00e+00 on column 6
        max.rel.err = 1.00e+00 on column 6
        DUAL SOLUTION IS INFEASIBLE

End of output
