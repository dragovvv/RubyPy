class Ruby():

    def ruby_print(text):

        script = open("script.rb","a")

        script.write(f'print "{text}" ')

        script.close()
        
    def ruby_print_Line(text):

        script = open("script.rb","a")

        script.write(f'puts "{text}" ')

        script.close()
