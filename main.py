print "Let us get started!"
spy_name = raw_input("Provide your name here :")
spy_salutation = raw_input("What should we call you Mr. or Ms?")
spy_name = spy_salutation + " " + spy_name   # CONCATENATION OF SALUTATION AND NAME.
# to check whether spy has input some name or not
if len(spy_name)>0:

 print 'Welcome '  + spy_name + '. Glad to have you back with us.'


