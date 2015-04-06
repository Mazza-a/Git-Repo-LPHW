#assigning 4 place holders to insert 
formatter = "%r %r %r %r"

"""I run the formatter variable 5 times each time contains
four different format values the first time containing integers from 1 - 4
the second containing strings "one" - "four" and so on"""
print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
	"That you could type up right",
	"But it didn't sing",
	"So I said goodnight."
)

