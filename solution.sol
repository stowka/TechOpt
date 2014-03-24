Problem:    
Rows:       4
Columns:    7
Non-zeros:  8
Status:     UNBOUNDED
Objective:  obj = 5 (MAXimum)

   No.   Row name   St   Activity     Lower bound   Upper bound    Marginal
------ ------------ -- ------------- ------------- ------------- -------------
     1 r.5          B              5                           5 
     2 r.6          B              5                           6 
     3 r.7          B              0                           5 
     4 r.8          NU             5                           5             1 

   No. Column name  St   Activity     Lower bound   Upper bound    Marginal
------ ------------ -- ------------- ------------- ------------- -------------
     1 x1           B              5             0               
     2 x2           NL             0             0                       < eps
     3 x3           NL             0             0                       < eps
     4 x4           NL             0             0                           1 
     5 x5           NL             0             0                           1 
     6 x6           NL             0             0                           1 
     7 x7           NL             0             0                           1 

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

KKT.DB: max.abs.err = 1.00e+00 on column 4
        max.rel.err = 1.00e+00 on column 4
        DUAL SOLUTION IS INFEASIBLE

End of output
