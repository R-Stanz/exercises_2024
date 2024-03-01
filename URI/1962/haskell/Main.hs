select_year year = do 
		if (year < 2015) then putStrLn (show (2015 - year) ++ " D.C.")
		else putStrLn (show (year - 2014) ++ " A.C.")


operate 0 = return()
operate runtime = do
		str_year <- getLine
		let year = read str_year :: Integer
		select_year year
		operate (runtime - 1)

main = do 
	n <- getLine
	let repetitions = (read n :: Integer)
	operate repetitions
