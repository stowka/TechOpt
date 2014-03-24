Problem:    
Rows:       7
Columns:    7
Non-zeros:  14
Status:     OPTIMAL
Objective:  obj = 13 (MAXimum)

   No.   Row name   St   Activity     Lower bound   Upper bound    Marginal
------ ------------ -- ------------- ------------- ------------- -------------
     1 r.5          NU             2                           2             1 
     2 r.6          NU             3                           3             1 
     3 r.7          NU             5                           5             1 
     4 r.8          B              2                           5 
     5 r.9          B              3                           3 
     6 r.10         NU             3                           3             1 
     7 r.11         B              0                           4 

   No. Column name  St   Activity     Lower bound   Upper bound    Marginal
------ ------------ -- ------------- ------------- ------------- -------------
     1 x1           B              2             0               
     2 x2           NL             0             0                          -1 
     3 x3           B              5             0               
     4 x4           NL             0             0                       < eps
     5 x5           B              3             0               
     6 x6           B              3             0               
     7 x7           NL             0             0                       < eps

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

KKT.DB: max.abs.err = 0.00e+00 on row 0
        max.rel.err = 0.00e+00 on row 0
        High quality

End of output
