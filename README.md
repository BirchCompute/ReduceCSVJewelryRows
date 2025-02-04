I was sitting in a computer lab when someone said "Is anyone here really good at Excel macros?" I asked what the problem was and realized it was something something I already knew how to do in Python. 

A row would have all the information about a jewelry product, but then it would put any extra image links in empty rows beneath it. 

They also wanted me to try to give each entry a "type" keyword based on something written in the product description. 

I realized how much coding it would actually take, but they said it would save them a lot of time, so they offered to pay me. 

So this program goes through all the rows. It preserves the header row. It grabs a full row. It gives itself a keyword. Then, it checks the rows under it for extra imagesrc links and adds it to its own imagescr string.  If the next row that it grabs is a new full row, it packs the last full row into our output data. Once we are out of rows, it parses it back into a csv and saves it to the same path as your starter file. 
