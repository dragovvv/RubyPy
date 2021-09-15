class Ruby():

    def ruby_print(text):

        script = open("script.rb","a")

        script.write(f'print "{text} " ')

        script.close()
