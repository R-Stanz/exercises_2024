atividade = "2"

-- 1 
isMult :: (Int, Int) -> (Int, Int) -> Bool
isMult u v = if ((u `ini'test` v) || (v `ini'test` u))
                then True
             else False
             where ini'test x y = if ((fst x) `mod` (fst y) == 0)
                                  then last'test (snd x) (snd y) ((fst x) `div` (fst y)) 
                              else False
                   last'test x y k = if (((x `mod` y) == 0) && ((x `div` y) == k))
                                    then True
                                else False
   
-- 2
tot'tri  :: Int -> Int
tot'tri p = test p (1,1,1) 0
            where is'tri'rec (a,b,c) = if (b*b+c*c-a*a == 0)
                                           then True
                                       else False
                  test p (a,b,c) sum = if ((a+b+c == p) && (is'tri'rec (a,b,c)))
                                           then if (c == b)
                                               then if (c == a)
                                                   then test p ((a+1),1,1) (sum+1)
                                               else test p (a,(b+1),1) (sum+1)
                                           else test p (a,b,(c+1)) (sum+1)
                                       else 
                                          if (b+c > p)
                                              then sum 
                                          else if (c == b)
                                              then if (c == a)
                                                  then test p ((a+1),1,1) sum
                                              else test p (a,(b+1),1) sum
                                          else test p (a,b,(c+1)) sum
