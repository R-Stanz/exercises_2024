main = do
	a <- getLine
	b <- getLine
	putStrLn ("X = " ++ (show ((read a) + (read b))))
