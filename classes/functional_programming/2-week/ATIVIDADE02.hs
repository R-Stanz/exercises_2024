atividade = "2"

-- 1 
-- Sejam as tuplas u e v de inteiros
-- tal que exista um inteiro k onde
-- u = kv ou v = ku  
-- então u e v são mútiplos. Construa 
-- função que determine se duas 
-- tuplas de inteiros  são múltiplas.
isMult :: (Int) -> (Int) -> Bool
isMult u v = if (((u `mod` v) == 0) || ((v `mod` u) == 0))
                then True
             else False
   
-- 2
-- Sejam todos os triângulos retângulos
-- de perímetro p e de lados inteiros.
--   representados por tuplas (a,b,c) 
-- com  a>=b>=c. Criar  
--  função que determine 
-- o total destes triângulos dado p .
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
