TOC_HW4
=======
This homework is related to homework 3 as it also is made by parsing a JSON file with real data on housing in Taiwan. In this particular case, we were asked to input the JSON file as an argument during compilation, just as we did in the previous assignment.
In case the URL does not exist or the JSON file being read is empty, the program will throw an error informing the problem, or in case the user forgets to input the URL, it'll also remind them the correct way to compile and execute it.
In this homework, the URL received will be read and completely scanned, and after that, it will choose the streets of a certain city with most records and print it, along with that street's highest and lowest price.
Within this homework, I used the re library, which allows us to use regular expressions, used to fing the strings for street names and matching them in order the count and know which street got the highest rate of records.
