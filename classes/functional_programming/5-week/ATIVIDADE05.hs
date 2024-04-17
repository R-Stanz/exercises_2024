-- 1

bis :: Int -> Bool 
bis year | year == 0 = False
         | (abs (year)) `mod` 4 == 0 = True
         | otherwise = False
         where abs year
                       | year < 0 = year * (-1)
                       | otherwise = year
-- 2

temp :: Float -> Char -> Char -> Float
temp t fr to | (fr == 'F') && (to == 'C') = (5 / 9) * (t - 32)
             | (fr == 'C') && (to == 'F') = (9 * t / 5 ) + 32
             | (fr == 'K') && (to == 'C') = t - 273.15
             | (fr == 'C') && (to == 'K') = t + 273.15
             | (fr == 'K') && (to == 'F') = temp (temp t 'K' 'C') 'C' 'F'
             | (fr == 'F') && (to == 'K') = temp (temp t 'F' 'C') 'C' 'K'
             | otherwise = t

-- 3

coin :: String -> [(Char, Float)] -> Float 
coin s m = sum [(count_char s (fst i)) * (snd i) | i <- m]
           where count_char str c = sum [1 | x <- str, x == c]
