tls :: String -> [(Char, Int)]
tls s = whipe (s, [])
        where whipe (remain, result) = if (null remain)
                                        then result
                                    else
                                        whipe (reduce remain result)
              reduce remain result = (no'head'char remain, result ++ count'head'char remain)
              count'head'char remain = [(head remain, length [x | x <- remain, x == head remain])]
              no'head'char remain = [x | x <- remain, x /= head remain]

sfq :: String -> (String, Int)
sfq s = test'words (words [x | x <- s, not (x `elem` "!@#$%^&*()-_=+[]'`~.:;,<>|?{}/")]) ("", 0)
        where test'words list result = if (null list)
                                           then result
                                       else if (snd result < count'word list)
                                           then test'words (reduce'list list) (head list, count'word list)
                                       else test'words (reduce'list list) result
              reduce'list list = [x | x <- list, x /= head list]
              count'word list = length [x | x <- list, x == head list]
