atividade = "1"

-- 1
noVog :: String -> String
noVog s = [x | x <- s, not (x `elem` "aeiou")]

-- 2
num'divs :: Int -> Int -> Int
num'divs x n = do 
		if ((x `mod` n) /= 0)
			then 0
		else do
			let rest = x `div` n
			1 + (num'divs rest n)

-- 3
is'prime :: Int -> Bool
is'prime n = do
		if ((n /= 2) && ((n `mod` 2) == 0))
			then False
		else if ((n < 4) && (n > 0))
			then True
		else
			brute'force'prime n 3

brute'force'prime n iterable = do
			if (n == iterable)
				then True
			else if ((n `mod` iterable) == 0)
				then False
			else do
				brute'force'prime n (iterable + 2)

-- 4
int'inv :: Int -> Int
int'inv x = do
		let str_x = show x
		let rev_str_x = reverse str_x
		read rev_str_x
